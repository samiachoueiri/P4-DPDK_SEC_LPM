#include "registers.p4"

control ACKFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta)
{   
    Register<bit<32>, bit<1>>(1) ack_counts_reg;
    Register<bit<7>, bit<1>>(1) ack_percent_iterator_reg;


    apply {
        attack.write(0,0x3);

        meta.add = 1;
        
        meta.ack_drop_percent = ACK_DROP_RATE;
        meta.ack_counts = 0;

        meta.ack_counts = ack_counts_reg.read(0);
        meta.ack_counts = meta.ack_counts +1;
        ack_counts_reg.write(0, meta.ack_counts);
    
        if(meta.ack_counts > THRESH_ACK){
            meta.ack_percent_iterator = ack_percent_iterator_reg.read(0);
            
            if(meta.ack_percent_iterator < meta.ack_drop_percent){
                meta.ack_percent_iterator = meta.ack_percent_iterator + 1;
                ack_percent_iterator_reg.write(0, meta.ack_percent_iterator);
                drop_packet();
            }
            else if (meta.ack_percent_iterator < 100) {
                meta.ack_percent_iterator = meta.ack_percent_iterator + 1;
                ack_percent_iterator_reg.write(0, meta.ack_percent_iterator);
            }
            else if (meta.ack_percent_iterator == 100) {
                meta.ack_percent_iterator = 0;
                ack_percent_iterator_reg.write(0, meta.ack_percent_iterator);
            }
        }
    }
}
