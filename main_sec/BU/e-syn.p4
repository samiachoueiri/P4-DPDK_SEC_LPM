
#include "registers.p4"

control SYNFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   
    //Register<bit<32>, bit<1>>(1) syn_counts_reg;
    Register<bit<7>, bit<1>>(1) percent_iterator_reg;


    apply {
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
                    drop_packet();
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