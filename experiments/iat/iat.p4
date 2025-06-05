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
    // bit<16> flow_id1;
    // bit<16> flow_id2;
    // bit<16> flow_id3;
    bit<20> count_0;
    // bit<20> count_1;
    // bit<20> count_2;
    // bit<20> count_3;
    bit<64> last_timestamp;
    bit<64> current_timestamp;
    bit<64> interarrival_value; 
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

control MainControlImpl(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd,
    inout pna_main_output_metadata_t ostd)
{   

    Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) hf;

    Register<bit<32>, bit<1>>(1) reg_index;
    Register<bit<20>, bit<16>>(32768) ht0;
    // Register<bit<20>, bit<16>>(32768) ht1;
    // Register<bit<20>, bit<16>>(32768) ht2;
    // Register<bit<20>, bit<16>>(32768) ht3;

    Register<bit<64>, bit<32>>(32768) reg_last;
    Register<bit<64>, bit<32>>(32768) reg_curr;

    Register<bit<64>, bit<32>>(32768) reg_last_timestamp;
    Register<bit<64>, bit<32>>(32768) reg_iat;
    
    action hash_fct0() {
       meta.flow_id0 = hf.get_hash((bit<16>)0, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    } 
    
    // action hash_fct1() {
    //     meta.flow_id1 = hf.get_hash((bit<16>)100, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);   
    // }
    
    // action hash_fct2() {
    //     meta.flow_id2 = hf.get_hash((bit<16>)200, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    // }
    
    // action hash_fct3() {
    //     meta.flow_id3 = hf.get_hash((bit<16>)300, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    // }

    action get_interarrival_time (){
        meta.last_timestamp = reg_last_timestamp.read((bit<32>) meta.flow_id0);
        meta.current_timestamp = ((bit<64>)istd.timestamp);
        if(meta.last_timestamp != 0){
            reg_last.write((bit<32>)meta.flow_id0, meta.last_timestamp);
            reg_curr.write((bit<32>)meta.flow_id0, meta.current_timestamp);
            meta.interarrival_value = meta.current_timestamp - meta.last_timestamp;
        } else {
            meta.interarrival_value = 0;
        }
        reg_iat.write((bit<32>)meta.flow_id0, meta.interarrival_value);
        reg_last_timestamp.write((bit<32>)meta.flow_id0, meta.current_timestamp);
    }
    
    action drop () {
        drop_packet();
    }

    // action forward (EthernetAddress dstAddr, PortId_t port_id) {
    //     send_to_port(port_id);
    //     hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
    //     hdr.ethernet.dstAddr = dstAddr;
    //     hdr.ipv4.ttl = hdr.ipv4.ttl -1;
    // }

    // table forwarding {
    //     key = { 
    //         hdr.ipv4.dstAddr: exact; 
    //     }
    //     actions = { 
    //         forward;
    //         drop;
    //     }
    //     size = 1024;
    //     default_action = drop;
    // }

    apply {
    
        if(hdr.ipv4.isValid()) {
            // forwarding.apply();

            hash_fct0();
            // // hash_fct1();
            // // hash_fct2();
            // // hash_fct3();
            reg_index.write(0, (bit<32>)meta.flow_id0);

            get_interarrival_time ();
            // reg_iat.write((bit<32>)meta.flow_id0, (bit<64>)istd.timestamp);

            meta.count_0 = ht0.read(meta.flow_id0);
            // // meta.count_1 = ht1.read(meta.flow_id1);
            // // meta.count_2 = ht2.read(meta.flow_id2);
            // // meta.count_3 = ht3.read(meta.flow_id3);

            ht0.write(meta.flow_id0,meta.count_0+1);
            // // ht1.write(meta.flow_id1,meta.count_1+1);
            // // ht2.write(meta.flow_id2,meta.count_2+1);
            // // ht3.write(meta.flow_id3,meta.count_3+1);



            bit<32> tmp_ip = hdr.ipv4.srcAddr;
            hdr.ipv4.srcAddr = hdr.ipv4.dstAddr;
            hdr.ipv4.dstAddr = tmp_ip;
            
            bit<48> tmp_mac = hdr.ethernet.srcAddr;
            hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
            hdr.ethernet.dstAddr = tmp_mac;
            
            if (istd.input_port == (PortId_t) 0){
                send_to_port((PortId_t) 0);
            }
            else if (istd.input_port == (PortId_t) 1){
                send_to_port((PortId_t) 1);
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
