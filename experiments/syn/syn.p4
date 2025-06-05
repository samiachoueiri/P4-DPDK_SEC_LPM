#include <core.p4>
#include <dpdk/pna.p4>

//--------------------------------------------------------------------------------------- headers
/*Define the data type definitions below*/
typedef bit<48> EthernetAddress;
typedef bit<32> IP4Address;  
const bit<16> TYPE_IPV4 = 0x0800;
const bit<8> TYPE_TCP = 6;

/*Define the Ethernet header below*/
header ethernet_t {
    EthernetAddress dstAddr;
    EthernetAddress srcAddr;
    bit<16> etherType; }

/*Define the IPv4 header below*/
header ipv4_t {
    bit<4>  version;
    bit<4>  ihl;
    bit<8>  diffserv;
    bit<16> totalLen;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragOffset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> hdrChecksum;
    IP4Address srcAddr;
    IP4Address dstAddr; }

/*Define the TCP header below*/
header tcp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4>  dataOffset;
    bit<4>  res;
    bit<3>  ecn;
    bit<5>  flags;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr; }

/*Define the metadata struct below*/
struct metadata {
    bit<7> drop_percent;
    bit<32> syn_counts;
    bit<7> percent_iterator;
}

/*Define the headers struct below*/
struct headers {
    ethernet_t ethernet;
    ipv4_t ipv4;
    tcp_t tcp; }

//--------------------------------------------------------------------------------------- parser
parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                in pna_main_parser_input_metadata_t istd)
{

    /*Add the start state below*/
    state start {
        transition parse_ethernet;
    }

    /*Add the parse_ethernet state below*/
    state parse_ethernet {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            TYPE_IPV4: parse_ipv4;
            default: accept;
        }
    }

    /*Add the parse_ipv4 state below*/
    state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol) {
            TYPE_TCP: parse_tcp;
            default: accept;
        }
    }

    /*Add the parse_tcp state below*/
    state parse_tcp {
        packet.extract(hdr.tcp);
        transition accept;
    }
}

//--------------------------------------------------------------------------------------- precontrol
control PreControl(
    in    headers  hdr,
    inout metadata meta,
    in    pna_pre_input_metadata_t  istd,
    inout pna_pre_output_metadata_t ostd)
{
    apply {

    /* empty */

    }
}

//--------------------------------------------------------------------------------------- control
#define THRESH 1000000

control MainControl(
    inout headers hdr,
    inout metadata meta,
    in pna_main_input_metadata_t istd,
    inout pna_main_output_metadata_t ostd) {    

    Register<bit<7>, bit<1>>(1) drop_percent_reg;
    Register<bit<32>, bit<1>>(1) syn_counts_reg;
    Register<bit<7>, bit<1>>(1) percent_iterator_reg;

    action forward (EthernetAddress dstAddr, PortId_t port_id) {
        send_to_port(port_id);
        hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = dstAddr;
        hdr.ipv4.ttl = hdr.ipv4.ttl -1;
    }
    action drop () {
        drop_packet();
    }
    table forwarding {
        key = { 
            hdr.ipv4.dstAddr: exact; 
        }
        actions = { 
            forward;
            drop;
        }
        size = 1024;
        default_action = drop;
    }

    apply {

        if(hdr.ipv4.isValid()) {
            forwarding.apply();

             if(hdr.tcp.isValid()){
                meta.drop_percent = drop_percent_reg.read(0);

                if(hdr.tcp.flags == 2) {
                    meta.syn_counts = 0;

                    meta.syn_counts = syn_counts_reg.read(0);
                    meta.syn_counts = meta.syn_counts +1;
                    syn_counts_reg.write(0, meta.syn_counts);
                
                    if(meta.syn_counts > THRESH){
                        meta.percent_iterator = percent_iterator_reg.read(0);
                        
                        if(meta.percent_iterator < meta.drop_percent){
                            meta.percent_iterator = meta.percent_iterator + 1;
                            percent_iterator_reg.write(0, meta.percent_iterator);
                            drop();
                        }
                        else if (meta.percent_iterator < 100) {
                            meta.percent_iterator = meta.percent_iterator + 1;
                            percent_iterator_reg.write(0, meta.percent_iterator);
                        }
                        else if (meta.percent_iterator == 100) {
                            meta.percent_iterator = 0;
                            percent_iterator_reg.write(0, meta.percent_iterator);
                        }
                    }
                }
             }
        }
    }  
}

//--------------------------------------------------------------------------------------- deparser
control MyDeparser(
    packet_out packet,
    inout    headers hdr,
    in    metadata meta,
    in    pna_main_output_metadata_t ostd)
{
    apply {
        
        /*Emit the Ethernet Header below*/
        packet.emit(hdr.ethernet);
        /*Emit the IPv4 Header below*/
        packet.emit(hdr.ipv4);
        /*Emit the TCP Header below*/
        packet.emit(hdr.tcp);
    
    }
}

//--------------------------------------------------------------------------------------- main
PNA_NIC(
MyParser(),
PreControl(),
MainControl(),
MyDeparser()
) main;