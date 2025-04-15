#include "registers.p4"

control FINFlood(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd)
{   

    apply {
        attack.write(0,0x4);

        // timestamp1 state 0
        meta.state_ts = reg_state_ts.read(0);
        if(meta.state_ts == 0){ 
            meta.timestamp1 = ((bit<64>)istd.timestamp)[31:0];
            reg_timestamp1.write(0, meta.timestamp1);
            reg_state_ts.write(0,meta.state_ts+1);
        }
        // timestamp2 state 1
        meta.state_ts = reg_state_ts.read(0);
        if(meta.state_ts == 1){ 
            meta.timestamp2 = ((bit<64>)istd.timestamp)[31:0];
            reg_timestamp2.write(0, meta.timestamp2);
            // reg_state_ts.write(0,meta.state_ts+1);
        }

        meta.add = 0; 
    }
}

// else if(hdr.tcp.flags == 0x01 || hdr.tcp.flags == 0x04 || hdr.tcp.flags == 0x05) { //FIN-RST 00101  , attack 4
//                     fin_flood.apply(hdr, meta, istd);  
//                     if(open_tcp.apply().miss){
//                         // timestamp3 state 2
//                         meta.state_ts = reg_state_ts.read(0)+1;
//                         if(meta.state_ts == 2){ 
//                             meta.timestamp3 = ((bit<64>)istd.timestamp)[31:0];
//                             reg_timestamp3.write(0, meta.timestamp3);
//                             reg_state_ts.write(0,meta.state_ts+1);
//                         }
//                         drop();} 
//                 }
