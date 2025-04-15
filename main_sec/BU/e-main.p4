#include <core.p4>
#include <dpdk/pna.p4>
#include "headers.p4"
#include "syn_flood.p4"
#include "registers.p4"


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
    /*
    Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) hf;
    
    action hash_fct0() {
       meta.flow_id0 = hf.get_hash((bit<16>)0, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    } 
    
    action hash_fct1() {
        meta.flow_id1 = hf.get_hash((bit<16>)100, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);   
    }
    
    action hash_fct2() {
        meta.flow_id2 = hf.get_hash((bit<16>)200, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    }
    
    action hash_fct3() {
        meta.flow_id3 = hf.get_hash((bit<16>)300, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    }

    */

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

    /*
    Register<bit<20>, bit<16>>(32768) ht0;
    Register<bit<20>, bit<16>>(32768) ht1;
    Register<bit<20>, bit<16>>(32768) ht2;
    Register<bit<20>, bit<16>>(32768) ht3;
    */
    SYNFlood() syn_flood;

    apply {
    
        if(hdr.ipv4.isValid()) {
            forwarding.apply();

            if(hdr.tcp.isValid()) {

                syn_flood.apply(hdr, meta);
                meta.syn_counts = syn_counts_reg.read(0);

                
                // else {

                //     meta.minimum = 1048575;
                //     hash_fct0();
                //     hash_fct1();
                //     hash_fct2();
                //     hash_fct3();

                //     get_interarrival_time ()

                //     meta.count_0 = ht0.read(meta.flow_id0);
                //     meta.count_1 = ht1.read(meta.flow_id1);
                //     meta.count_2 = ht2.read(meta.flow_id2);
                //     meta.count_3 = ht3.read(meta.flow_id3);

                //     meta.dif = meta.minimum - meta.count_0;
                //     if(meta.dif > 0){
                //         meta.minimum = meta.count_0;
                //     }

                //     meta.dif = meta.minimum - meta.count_1;
                //     if(meta.dif > 0){
                //         meta.minimum = meta.count_1;
                //     }

                //     meta.dif = meta.minimum - meta.count_2;
                //     if(meta.dif > 0){
                //         meta.minimum = meta.count_2;
                //     }

                //     meta.dif = meta.minimum - meta.count_3;
                //     if(meta.dif > 0){
                //         meta.minimum = meta.count_3;
                //     }
                    
                //     if(meta.minimum > THRESH_HH){
                //         drop();
                //     } 
                //     else {
                //         ht0.write(meta.flow_id0,meta.count_0+1);
                //         ht1.write(meta.flow_id1,meta.count_1+1);
                //         ht2.write(meta.flow_id2,meta.count_2+1);
                //         ht3.write(meta.flow_id3,meta.count_3+1);
                //     }
                // }
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