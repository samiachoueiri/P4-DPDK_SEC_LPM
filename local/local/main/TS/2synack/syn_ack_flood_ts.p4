#include "registers.p4"

control SYNACKFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd)
{   
    Register<bit<32>, bit<1>>(1) synack_counts_reg;
    Register<bit<7>, bit<1>>(1) synack_percent_iterator_reg;


    apply {
        attack.write(0,0x2);
        // timestamp1 state 0
        meta.state_ts = reg_state_ts.read(0);
        if(meta.state_ts == 0){ 
            meta.timestamp1 = ((bit<64>)istd.timestamp)[31:0];
            reg_timestamp1.write(0, meta.timestamp1);
            reg_state_ts.write(0,meta.state_ts+1);
        }

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
                // timestamp3 state 2
                // reg_state_ts.write(0,meta.state_ts+1);
                meta.state_ts = reg_state_ts.read(0)+1;
                if(meta.state_ts == 2){ 
                    meta.timestamp3 = ((bit<64>)istd.timestamp)[31:0];
                    reg_timestamp3.write(0, meta.timestamp3);
                    reg_state_ts.write(0,meta.state_ts+1);
                }
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
        // timestamp2 state 1
        meta.state_ts = reg_state_ts.read(0);
        if(meta.state_ts == 1){ 
            meta.timestamp2 = ((bit<64>)istd.timestamp)[31:0];
            reg_timestamp2.write(0, meta.timestamp2);
            // reg_state_ts.write(0,meta.state_ts+1);
        }
    }
}
