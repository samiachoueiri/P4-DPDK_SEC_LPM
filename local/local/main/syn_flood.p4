#include "registers.p4"

control SYNFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd)
{   
    Register<bit<1>, bit<1>>(1) syn_flood_reg;
    Register<bit<7>, bit<1>>(1) syn_drop_percent_reg;
    Register<bit<32>, bit<1>>(1) syn_counts_reg;
    Register<bit<32>, bit<1>>(1) syn_percent_iterator_reg;
    Register<bit<32>, bit<1>>(1) allow_count_reg;
    
    // Register<bit<32>, bit<1>>(1) reg_time;
    // Register<bit<32>, bit<1>>(1) reg_time_diff;
    // Register<bit<2>, bit<1>>(1) reg_time_key;


    apply {
        attack.write(0,0x1);
        // meta.syn_drop_percent = SYN_DROP_RATE;
        meta.syn_drop_percent = syn_drop_percent_reg.read(0);

        // meta.time = ((bit<64>)istd.timestamp)[31:0];
        // meta.time_key = reg_time_key.read(0);

        // if(meta.time_key == 0){ 
        //     reg_time.write(0, meta.time);
        //     reg_time_key.write(0,meta.time_key+1);
        // }
        // if(meta.time_key == 1){
        //     meta.time_prev = reg_time.read(0);
        //     meta.time_diff = meta.time - meta.time_prev;
        //     reg_time_diff.write(0, meta.time_diff);

        //     if (meta.time_diff >= 1000000){
        //         reg_time_key.write(0,meta.time_key-1); 
        //     }
        // }

        
        meta.syn_counts = 0;
        meta.syn_counts = syn_counts_reg.read(0);
        meta.syn_counts = meta.syn_counts +1;
        syn_counts_reg.write(0, meta.syn_counts);

        meta.allow_count = allow_count_reg.read(0);

        meta.syn_flood = syn_flood_reg.read(0);
        // if(meta.syn_counts > THRESH_SYN){
        // if(meta.syn_flood == 1){
            
            meta.syn_percent_iterator = syn_percent_iterator_reg.read(0);
            
            // if(meta.syn_percent_iterator < meta.syn_drop_percent){
            //     meta.syn_percent_iterator = meta.syn_percent_iterator + 1;
            //     syn_percent_iterator_reg.write(0, meta.syn_percent_iterator);
            //     drop_packet();
            // }
            // else if (meta.syn_percent_iterator < 100) {
            //     meta.syn_percent_iterator = meta.syn_percent_iterator + 1;
            //     syn_percent_iterator_reg.write(0, meta.syn_percent_iterator);
            // }
            // else if (meta.syn_percent_iterator == 100) {
            //     meta.syn_percent_iterator = 0;
            //     syn_percent_iterator_reg.write(0, meta.syn_percent_iterator);
            // }

            if(meta.syn_percent_iterator < meta.allow_count){
                meta.syn_percent_iterator = meta.syn_percent_iterator + 1;
                syn_percent_iterator_reg.write(0, meta.syn_percent_iterator);
                // drop_packet();
            }
            else {
                drop_packet();
            }
        // }
         
    }
}
