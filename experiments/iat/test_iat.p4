#include <core.p4>
#include <dpdk/pna.p4>

//--------------------------------------------------------------------------------------- headers
/*Define the data type definitions below*/
typedef bit<48> EthernetAddress;
typedef bit<32> IP4Address;  
const bit<16> TYPE_IPV4 = 0x0800;
const bit<8> TYPE_CUSTOM = 0xFF;

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
    bit<3>  res;
    bit<3>  ecn;
    bit<6>  ctrl;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr; }

/*Define custom header below*/
header interarrival_t {
    bit<48> interarrival_value; }

/*Define the metadata struct below*/
struct metadata {
    bit<32> flow_id;
    bit<64> last_timestamp;
    bit<64> current_timestamp;
    bit<64> interarrival_value; }

/*Define the headers struct below*/
struct headers {
    ethernet_t ethernet;
    ipv4_t ipv4;
    interarrival_t interarrival; }

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
            TYPE_CUSTOM: parse_interarrival;
            default: accept;
        }
    }

    /*Add the parse_tcp state below*/
    state parse_interarrival {
        packet.extract(hdr.interarrival);
        transition accept;
    }
}


//--------------------------------------------------------------------------------------- precontrol
/*-----------------Pre-control-----------------*/
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

/*-----------------Control-----------------*/

control MainControl(
    inout headers hdr,
    inout metadata meta,
    in pna_main_input_metadata_t istd,
    inout pna_main_output_metadata_t ostd) {    

    action forward (PortId_t port_id) {
        send_to_port(port_id);
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

    Hash<bit<32>> (PNA_HashAlgorithm_t.CRC32) hash;

    action compute_flow_id(){
        meta.flow_id = hash.get_hash((bit<32>)0, {hdr.ipv4.srcAddr, hdr.ipv4.dstAddr}, 1024);
    }

    Register<bit<64>, bit<32>>(1024) reg_last_timestamp;
    Register<bit<32>, bit<1>>(1) reg_index;
    Register<bit<48>, bit<32>>(1024) reg_iat;

    action get_interarrival_time (){
       meta.last_timestamp = reg_last_timestamp.read((bit<32>) meta.flow_id); 
       meta.current_timestamp = ((bit<64>)istd.timestamp);

       if(meta.last_timestamp != 0){
            meta.interarrival_value = meta.current_timestamp - meta.last_timestamp;
       } else {
            meta.interarrival_value = 0;
       }
       reg_last_timestamp.write((bit<32>)meta.flow_id, meta.current_timestamp);
    }

    apply {
        if(hdr.ipv4.isValid()){
            if(hdr.interarrival.isValid()){
                compute_flow_id();
                get_interarrival_time();
                hdr.interarrival.interarrival_value = ((bit<48>)meta.interarrival_value);
                reg_index.write(0, (bit<32>)meta.flow_id);
                reg_iat.write((bit<32>)meta.flow_id, (bit<48>)meta.interarrival_value);
            }
            forwarding.apply();
        }
    }   
}


//--------------------------------------------------------------------------------------- deparser
/*-----------------Deparser-----------------*/
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
        /*Emit the CUSTOM Header below*/
        packet.emit(hdr.interarrival);
    
    }
}


//--------------------------------------------------------------------------------------- main
/*Insert the blocks below this comment*/
PNA_NIC(
MyParser(),
PreControl(),
MainControl(),
MyDeparser()
) main;
