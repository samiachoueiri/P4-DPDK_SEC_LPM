control GETTCPFlow(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   
    Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) h0;
    
    action hf0() {
       meta.flow_id0 = h0.get_hash((bit<16>)0, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr,hdr.ipv4.protocol}, (bit<16>)32768);
    } 
    
    action hf1() {
        meta.flow_id1 = h0.get_hash((bit<16>)100, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr,hdr.ipv4.protocol}, (bit<16>)32768);   
    }
    
    action hf2() {
        meta.flow_id2 = h0.get_hash((bit<16>)200, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr,hdr.ipv4.protocol}, (bit<16>)32768);
    }
    
    action hf3() {
        meta.flow_id3 = h0.get_hash((bit<16>)300, {hdr.tcp.srcPort,hdr.tcp.dstPort,hdr.ipv4.srcAddr,hdr.ipv4.dstAddr,hdr.ipv4.protocol}, (bit<16>)32768);
    }

    Register<bit<16>, bit<1>>(1) flow_id0;
    Register<bit<16>, bit<1>>(1) flow_id1;
    Register<bit<16>, bit<1>>(1) flow_id2;
    Register<bit<16>, bit<1>>(1) flow_id3;

    apply {

        hf0();
        hf1();
        hf2();
        hf3();

        flow_id0.write(0,meta.flow_id0);
        flow_id1.write(0,meta.flow_id1);
        flow_id2.write(0,meta.flow_id2);
        flow_id3.write(0,meta.flow_id3);

    }
}
