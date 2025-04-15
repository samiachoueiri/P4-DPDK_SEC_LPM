#include "registers.p4"

control FINFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   

    apply {
        attack.write(0,0x4);
        meta.add = 0; 
    }
}
