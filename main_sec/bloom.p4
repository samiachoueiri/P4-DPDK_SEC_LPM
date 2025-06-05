#include "registers.p4"

#define SKETCH_REGISTER(num) Register<bit<SKETCH_WIDTH>, bit<16>>(SKETCH_LENGTH) sketch##num

#define SKETCH_APPLY(num) meta.index_sketch##num = h2.get_hash((bit<16>)##num,\
                                                    { \
                                                        hdr.ipv4.srcAddr, \
                                                        hdr.ipv4.dstAddr \
                                                    }, \
                                                    (bit<16>)SKETCH_LENGTH); \
            meta.value_sketch##num = sketch##num.read(meta.index_sketch##num); \
            if(meta.value_sketch##num == 1) { \
                meta.new_flow = 0; } \
            meta.value_sketch##num = 1; \
            sketch##num.write(meta.index_sketch##num, meta.value_sketch##num);
Register<bit<1>, bit<1>>(1) test;
control UDPFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   

    Hash<bit<16>> (PNA_HashAlgorithm_t.CRC16) h2;

    SKETCH_REGISTER(0);
    SKETCH_REGISTER(1);
    SKETCH_REGISTER(2);

    apply {
        attack.write(0,0x7);
        meta.new_flow = 1;

        SKETCH_APPLY(0)
        SKETCH_APPLY(1)
        SKETCH_APPLY(2)

        test.write(0, meta.new_flow); 

    }
}
