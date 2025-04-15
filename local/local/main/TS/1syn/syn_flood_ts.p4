#include "registers.p4"

control SYNFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd)
{   
    // Register<bit<7>, bit<1>>(1) drop_percent_reg;
    Register<bit<32>, bit<1>>(1) syn_counts_reg;
    Register<bit<7>, bit<1>>(1) syn_percent_iterator_reg;


    apply {
        attack.write(0,0x1);
        // timestamp1 state 0
        meta.state_ts = reg_state_ts.read(0);
        if(meta.state_ts == 0){ 
            meta.timestamp1 = ((bit<64>)istd.timestamp)[31:0];
            // meta.timestamp1 = 5;
            reg_timestamp1.write(0, meta.timestamp1);
            reg_state_ts.write(0,meta.state_ts+1);
        }

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
                // timestamp3 state 2
                // reg_state_ts.write(0,meta.state_ts+1);
                meta.state_ts = reg_state_ts.read(0)+1;
                if(meta.state_ts == 2){ 
                    meta.timestamp3 = ((bit<64>)istd.timestamp)[31:0];
                    // meta.timestamp3_64 = ((bit<64>)istd.timestamp);
                    // meta.timestamp3 = meta.timestamp3_64[31:0];
                    reg_timestamp3.write(0, meta.timestamp3);
                    reg_state_ts.write(0,meta.state_ts+1);
                }
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

        // timestamp2 state 1
        meta.state_ts = reg_state_ts.read(0);
        if(meta.state_ts == 1){ 
            meta.timestamp2 = ((bit<64>)istd.timestamp)[31:0];
            // meta.timestamp2 = 55;
            reg_timestamp2.write(0, meta.timestamp2);
            // reg_state_ts.write(0,meta.state_ts+1);
        }
         
    }
}
