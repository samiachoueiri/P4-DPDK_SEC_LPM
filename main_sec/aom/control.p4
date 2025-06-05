// #include "registers.p4"

control MainControlImpl(
    inout headers_t       hdr,
    inout main_metadata_t meta,
    in    pna_main_input_metadata_t  istd,
    inout pna_main_output_metadata_t ostd)
{   

    action drop () {
        drop_packet();
    }

    action forward (EthernetAddress dstAddr, PortId_t port_id) {
        send_to_port(port_id);
        hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = dstAddr;
        hdr.ipv4.ttl = hdr.ipv4.ttl -1;
    }

    table forwarding {
        key = { 
            hdr.ipv4.dstAddr: exact; 
        }
        actions = { 
            forward;
            drop;
        }
        size = 1024;
        default_action = drop;
    }

    action noAction () {
    }

    action add_miss () {
        if (meta.add == 1) {
            add_entry(action_name = "noAction", action_params = {}, expire_time_profile_id = EXPIRE_TIME_PROFILE_ID);
        }
        else {
            noAction();
        }
    }

    table open_tcp {
        key = {
            hdr.ipv4.srcAddr: exact;
        }
        actions = {
            noAction;
            add_miss;
        }
        add_on_miss = true;
        default_action = add_miss;
        size = 1000000;
    }
        
    // SYNFlood() syn_flood;
    // FINFlood() fin_flood;
    
    apply {

        if(hdr.ipv4.isValid()) {
            forwarding.apply();

            if(hdr.tcp.isValid()) {
                if(hdr.tcp.flags == 0x2) { // SYN 00010 , attack 1
                    // syn_flood.apply(hdr, meta);
                    meta.add = 1;
                    open_tcp.apply();
                }
                else if(hdr.tcp.flags == 0x01 || hdr.tcp.flags == 0x04 || hdr.tcp.flags == 0x05) { //FIN-RST 00101  , attack 4
                    // fin_flood.apply(hdr, meta);
                    meta.add = 0;  
                    if(open_tcp.apply().miss){drop();} 
                }
            }
            else {
                // attack.write(0,0xF);
                drop_packet();
            }    
        }
        else {
            // attack.write(0,0xF);
            drop_packet();
        }
        
    }
}