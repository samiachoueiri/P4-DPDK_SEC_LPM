#include "registers.p4"

control SYNACKFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   
    Register<bit<32>, bit<1>>(1) synack_counts_reg;
    Register<bit<7>, bit<1>>(1) synack_percent_iterator_reg;


    apply {
        attack.write(0,0x2);

        meta.synack_drop_percent = SYNACK_DROP_RATE;
        meta.synack_counts = 0;

        meta.synack_counts = synack_counts_reg.read(0);
        meta.synack_counts = meta.synack_counts +1;
        synack_counts_reg.write(0, meta.synack_counts);
    
        if(meta.synack_counts > THRESH_SYNACK){
            meta.synack_percent_iterator = synack_percent_iterator_reg.read(0);
            
            if(meta.synack_percent_iterator < meta.synack_drop_percent){
                meta.synack_percent_iterator = meta.synack_percent_iterator + 1;
                synack_percent_iterator_reg.write(0, meta.synack_percent_iterator);
                drop_packet();
            }
            else if (meta.synack_percent_iterator < 100) {
                meta.synack_percent_iterator = meta.synack_percent_iterator + 1;
                synack_percent_iterator_reg.write(0, meta.synack_percent_iterator);
            }
            else if (meta.synack_percent_iterator == 100) {
                meta.synack_percent_iterator = 0;
                synack_percent_iterator_reg.write(0, meta.synack_percent_iterator);
            }
        }
    }
}
