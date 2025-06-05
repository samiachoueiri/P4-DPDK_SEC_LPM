control GETICMPFlow(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   
    Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) h1;
    
    action hf0_icmp() {
       meta.flow_icmp_id0 = h1.get_hash((bit<16>)0, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    } 
    
    action hf1_icmp() {
        meta.flow_icmp_id1 = h1.get_hash((bit<16>)100, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);   
    }
    
    action hf2_icmp() {
        meta.flow_icmp_id2 = h1.get_hash((bit<16>)200, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    }
    
    action hf3_icmp() {
        meta.flow_icmp_id3 = h1.get_hash((bit<16>)300, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    }

    Register<bit<16>, bit<1>>(1) flow_icmp_id0;
    Register<bit<16>, bit<1>>(1) flow_icmp_id1;
    Register<bit<16>, bit<1>>(1) flow_icmp_id2;
    Register<bit<16>, bit<1>>(1) flow_icmp_id3;

    apply {

        hf0_icmp();
        hf1_icmp();
        hf2_icmp();
        hf3_icmp();

        flow_icmp_id0.write(0,meta.flow_icmp_id0);
        flow_icmp_id1.write(0,meta.flow_icmp_id1);
        flow_icmp_id2.write(0,meta.flow_icmp_id2);
        flow_icmp_id3.write(0,meta.flow_icmp_id3);

    }
}
