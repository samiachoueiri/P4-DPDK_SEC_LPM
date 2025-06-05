#include "registers.p4"

control SYNFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   
    // Register<bit<7>, bit<1>>(1) drop_percent_reg;
    Register<bit<32>, bit<1>>(1) syn_counts_reg;
    Register<bit<7>, bit<1>>(1) syn_percent_iterator_reg;


    apply {
        attack.write(0,0x1);

        // meta.syn_drop_percent = drop_percent_reg.read(0);
        meta.syn_drop_percent = SYN_DROP_RATE;
        meta.syn_counts = 0;

        meta.syn_counts = syn_counts_reg.read(0);
        meta.syn_counts = meta.syn_counts +1;
        syn_counts_reg.write(0, meta.syn_counts);
    
        if(meta.syn_counts > THRESH_SYN){
            meta.syn_percent_iterator = syn_percent_iterator_reg.read(0);
            
            if(meta.syn_percent_iterator < meta.syn_drop_percent){
                meta.syn_percent_iterator = meta.syn_percent_iterator + 1;
                syn_percent_iterator_reg.write(0, meta.syn_percent_iterator);
                drop_packet();
            }
            else if (meta.syn_percent_iterator < 100) {
                meta.syn_percent_iterator = meta.syn_percent_iterator + 1;
                syn_percent_iterator_reg.write(0, meta.syn_percent_iterator);
            }
            else if (meta.syn_percent_iterator == 100) {
                meta.syn_percent_iterator = 0;
                syn_percent_iterator_reg.write(0, meta.syn_percent_iterator);
            }
        }
         
    }
}
