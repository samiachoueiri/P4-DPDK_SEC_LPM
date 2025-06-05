#include <core.p4>
#include <dpdk/pna.p4>

//--------------------------------------------------------------------------------------- headers
typedef bit<48> EthernetAddress;
typedef bit<32> IP4Address;  
const bit<16> TYPE_IPV4 = 0x0800;
const bit<8> TYPE_TCP = 6;

header ethernet_t {
    EthernetAddress dstAddr;
    EthernetAddress srcAddr;
    bit<16>         etherType;
}

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
    IP4Address dstAddr;
}

// header tcp_t {
//     bit<16> srcPort;
//     bit<16> dstPort;
//     bit<32> seqNo;
//     bit<32> ackNo;
//     bit<4>  dataOffset;
//     bit<3>  res;
//     bit<3>  ecn;
//     bit<6>  ctrl;
//     bit<16> window;
//     bit<16> checksum;
//     bit<16> urgentPtr;
// }

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
    bit<16> urgentPtr; 
}

struct main_metadata_t {
    bit<16> flow_id0;
    bit<16> flow_id1;
    bit<16> flow_id2;
    bit<16> flow_id3;
    bit<20> count_0;
    bit<20> count_1;
    bit<20> count_2;
    bit<20> count_3;
    bit<20> minimum;    
    bit<20> dif;

    bit<7> drop_percent;
    bit<32> syn_counts;
    bit<7> percent_iterator;   
}

struct headers_t {
    ethernet_t ethernet;
    ipv4_t ipv4;
    tcp_t tcp;
}

//--------------------------------------------------------------------------------------- parser
parser MainParserImpl( packet_in pkt,
    out   headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_parser_input_metadata_t istd)
{
    state start {
        pkt.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            TYPE_IPV4: parse_ipv4;
            default: accept;
        }
    }
    state parse_ipv4 {
        pkt.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol) {
            TYPE_TCP: parse_tcp;
            default: accept;
        }
    } 
    state parse_tcp {
        pkt.extract(hdr.tcp);
        transition accept;
    }
}

//--------------------------------------------------------------------------------------- precontrol
control PreControlImpl(
    in    headers_t  hdr,
    inout main_metadata_t meta,
    in    pna_pre_input_metadata_t  istd,
    inout pna_pre_output_metadata_t ostd)
{
    apply {
        }
}

//--------------------------------------------------------------------------------------- control
#define THRESH_HH 100000
#define THRESH_SYN 1000000
#define SYN_DROP_RATE 50

control MainControlImpl(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd,
    inout pna_main_output_metadata_t ostd)
{   

    Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) h0;
    
    action a1() {
       meta.flow_id0 = h0.get_hash((bit<16>)0, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    } 
    
    action a2() {
        meta.flow_id1 = h0.get_hash((bit<16>)100, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);   
    }
    
    action a3() {
        meta.flow_id2 = h0.get_hash((bit<16>)200, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    }
    
    action a4() {
        meta.flow_id3 = h0.get_hash((bit<16>)300, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    }
    
    action drop () {
        drop_packet();
    }

    action forward (EthernetAddress dstAddr, PortId_t port_id) {
        send_to_port(port_id);
        hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = dstAddr;
        hdr.ipv4.ttl = hdr.ipv4.ttl -1;
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
     
    Register<bit<20>, bit<16>>(32768) ht0;
    Register<bit<20>, bit<16>>(32768) ht1;
    Register<bit<20>, bit<16>>(32768) ht2;
    Register<bit<20>, bit<16>>(32768) ht3;

    // Register<bit<7>, bit<1>>(1) drop_percent_reg;
    Register<bit<32>, bit<1>>(1) syn_counts_reg;
    Register<bit<7>, bit<1>>(1) percent_iterator_reg;

    apply {
    
        if(hdr.ipv4.isValid()) {
            forwarding.apply();

            if(hdr.tcp.isValid()) {

                if(hdr.tcp.flags == 2) {
                    // meta.drop_percent = drop_percent_reg.read(0);
                    meta.drop_percent = SYN_DROP_RATE;
                    meta.syn_counts = 0;

                    meta.syn_counts = syn_counts_reg.read(0);
                    meta.syn_counts = meta.syn_counts +1;
                    syn_counts_reg.write(0, meta.syn_counts);
                
                    if(meta.syn_counts > THRESH_SYN){
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
                else {

                    meta.minimum = 1048575;
                    a1();
                    a2();
                    a3();
                    a4();

                    meta.count_0 = ht0.read(meta.flow_id0);
                    meta.count_1 = ht1.read(meta.flow_id1);
                    meta.count_2 = ht2.read(meta.flow_id2);
                    meta.count_3 = ht3.read(meta.flow_id3);

                    meta.dif = meta.minimum - meta.count_0;
                    if(meta.dif > 0){
                        meta.minimum = meta.count_0;
                    }

                    meta.dif = meta.minimum - meta.count_1;
                    if(meta.dif > 0){
                        meta.minimum = meta.count_1;
                    }

                    meta.dif = meta.minimum - meta.count_2;
                    if(meta.dif > 0){
                        meta.minimum = meta.count_2;
                    }

                    meta.dif = meta.minimum - meta.count_3;
                    if(meta.dif > 0){
                        meta.minimum = meta.count_3;
                    }
                    
                    if(meta.minimum > THRESH_HH){
                        drop();
                    } 
                    else {
                        ht0.write(meta.flow_id0,meta.count_0+1);
                        ht1.write(meta.flow_id1,meta.count_1+1);
                        ht2.write(meta.flow_id2,meta.count_2+1);
                        ht3.write(meta.flow_id3,meta.count_3+1);
                    }
                }
            }
        }
    }
}

//--------------------------------------------------------------------------------------- deparser
control MainDeparserImpl(
    packet_out pkt,
    inout    headers_t hdr,
    in    main_metadata_t meta,
    in    pna_main_output_metadata_t ostd)
{
    apply {
        pkt.emit(hdr.ethernet);
        pkt.emit(hdr.ipv4);
        pkt.emit(hdr.tcp);
    }
}

//--------------------------------------------------------------------------------------- main
PNA_NIC(
    MainParserImpl(),
    PreControlImpl(),
    MainControlImpl(),
    MainDeparserImpl()
    ) main;