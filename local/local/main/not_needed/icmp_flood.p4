#include "registers.p4"

control ICMPFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   
    // Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) h1;
    
    // action hf0_icmp() {
    //    meta.flow_icmp_id0 = h1.get_hash((bit<16>)0, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    // } 
    
    // action hf1_icmp() {
    //     meta.flow_icmp_id1 = h1.get_hash((bit<16>)100, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);   
    // }
    
    // action hf2_icmp() {
    //     meta.flow_icmp_id2 = h1.get_hash((bit<16>)200, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    // }
    
    // action hf3_icmp() {
    //     meta.flow_icmp_id3 = h1.get_hash((bit<16>)300, {hdr.ipv4.srcAddr,hdr.ipv4.dstAddr}, (bit<16>)32768);
    // }

    Register<bit<20>, bit<16>>(32768) ht_icmp_0;
    Register<bit<20>, bit<16>>(32768) ht_icmp_1;
    Register<bit<20>, bit<16>>(32768) ht_icmp_2;
    Register<bit<20>, bit<16>>(32768) ht_icmp_3;

    // Register<bit<16>, bit<1>>(1) flow_icmp_id0;
    // Register<bit<16>, bit<1>>(1) flow_icmp_id1;
    // Register<bit<16>, bit<1>>(1) flow_icmp_id2;
    // Register<bit<16>, bit<1>>(1) flow_icmp_id3;

    apply {
        attack.write(0,0x6);
        
        meta.minimum = 1048575;
        // hf0_icmp();
        // hf1_icmp();
        // hf2_icmp();
        // hf3_icmp();

        // flow_icmp_id0.write(0,meta.flow_icmp_id0);
        // flow_icmp_id1.write(0,meta.flow_icmp_id1);
        // flow_icmp_id2.write(0,meta.flow_icmp_id2);
        // flow_icmp_id3.write(0,meta.flow_icmp_id3);

        meta.count_icmp_0 = ht_icmp_0.read(meta.flow_icmp_id0);
        meta.count_icmp_1 = ht_icmp_1.read(meta.flow_icmp_id1);
        meta.count_icmp_2 = ht_icmp_2.read(meta.flow_icmp_id2);
        meta.count_icmp_3 = ht_icmp_3.read(meta.flow_icmp_id3);

        meta.dif_icmp = meta.minimum_icmp - meta.count_icmp_0;
        if(meta.dif_icmp > 0){
            meta.minimum_icmp = meta.count_icmp_0;
        }

        meta.dif_icmp = meta.minimum_icmp - meta.count_icmp_1;
        if(meta.dif_icmp > 0){
            meta.minimum_icmp = meta.count_icmp_1;
        }

        meta.dif_icmp = meta.minimum_icmp - meta.count_icmp_2;
        if(meta.dif_icmp > 0){
            meta.minimum_icmp = meta.count_icmp_2;
        }

        // meta.dif_icmp = meta.minimum_icmp - meta.count_icmp_3;
        // if(meta.dif_icmp > 0){
        //     meta.minimum_icmp = meta.count_icmp_3;
        // }
        
        if(meta.minimum_icmp > THRESH_ICMP){
            drop_packet();
        } 
        else {
            ht_icmp_0.write(meta.flow_icmp_id0,meta.count_icmp_0+1);
            ht_icmp_1.write(meta.flow_icmp_id1,meta.count_icmp_1+1);
            ht_icmp_2.write(meta.flow_icmp_id2,meta.count_icmp_2+1);
            ht_icmp_3.write(meta.flow_icmp_id3,meta.count_icmp_3+1);
        }

    }
}
