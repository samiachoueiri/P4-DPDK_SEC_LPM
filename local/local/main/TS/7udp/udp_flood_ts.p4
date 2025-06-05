#include "registers.p4"

control UDPFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd)
{   
    action noAction () {
    }

    action add_miss_udp () {
        add_entry(action_name = "noAction", action_params = {}, expire_time_profile_id = EXPIRE_TIME_PROFILE_ID);
    }

    table open_udp {
        key = {
            hdr.ipv4.srcAddr: exact;
            hdr.ipv4.dstAddr: exact;
        }
        actions = {
            noAction;
            add_miss_udp;
        }
        add_on_miss = true;
        default_action = add_miss_udp;
        size = 1024;
    }

    // // Register<bit<7>, bit<1>>(1) drop_percent_reg;
    Register<bit<32>, bit<1>>(1) udp_counts_reg;
    Register<bit<7>, bit<1>>(1) udp_percent_iterator_reg;


    apply {
        attack.write(0,0x7);
        // timestamp1 state 0
        meta.state_ts = reg_state_ts.read(0);
        if(meta.state_ts == 0){ 
            meta.timestamp1 = ((bit<64>)istd.timestamp)[31:0];
            reg_timestamp1.write(0, meta.timestamp1);
            reg_state_ts.write(0,meta.state_ts+1);
        }

        // drop_packet();
        if(open_udp.apply().hit){
            // meta.udp_drop_percent = drop_percent_reg.read(0);
            meta.udp_drop_percent = UDP_DROP_RATE;
            meta.udp_counts = 0;

            meta.udp_counts = udp_counts_reg.read(0);
            meta.udp_counts = meta.udp_counts +1;
            udp_counts_reg.write(0, meta.udp_counts);
        
            if(meta.udp_counts > THRESH_UDP){
                meta.udp_percent_iterator = udp_percent_iterator_reg.read(0);
                
                if(meta.udp_percent_iterator < meta.udp_drop_percent){
                    meta.udp_percent_iterator = meta.udp_percent_iterator + 1;
                    udp_percent_iterator_reg.write(0, meta.udp_percent_iterator);
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
                else if (meta.udp_percent_iterator < 100) {
                    meta.udp_percent_iterator = meta.udp_percent_iterator + 1;
                    udp_percent_iterator_reg.write(0, meta.udp_percent_iterator);
                }
                else if (meta.udp_percent_iterator == 100) {
                    meta.udp_percent_iterator = 0;
                    udp_percent_iterator_reg.write(0, meta.udp_percent_iterator);
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
}
