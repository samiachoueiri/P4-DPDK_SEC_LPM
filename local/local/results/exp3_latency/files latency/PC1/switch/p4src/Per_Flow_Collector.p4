/* -*- P4_16 -*- */

#include <core.p4>
#include <tna.p4>
#include "Headers_and_Definitions.p4"



struct flow_digest_t {
    bit<11> flow_id;
	bit<11> rev_flow_id;
    bit<32> flow_source_IP;
    bit<32> flow_destination_IP;
    bit<16> flow_source_port;
    bit<16> flow_destination_port;	
}

struct flow_timing_t {
    bit<32> flow_start_time;
    bit<32> flow_end_time;
}

struct flow_sampling_t {
    bit<32> prev_sampling_time;
    bit<32> flow_sampling_rate;
} 
  

/*************************************************************************
 **************  I N G R E S S   P R O C E S S I N G   *******************
 *************************************************************************/

    /***********************  H E A D E R S  ************************/
    struct my_ingress_headers_t {
        ethernet_h   ethernet;
        ipv4_h       ipv4;
        tcp_h        tcp;
        tmp_h        tmp;
        udp_h        udp;
        rtp_h        rtp;

    }
    /******  G L O B A L   I N G R E S S   M E T A D A T A  *********/
    struct my_ingress_metadata_t {
        bit<11> flow_id;
		bit<11> rev_flow_id;
        
        bit<32> flow_sample_length;

        bit<32> flow_end_time;

        bit<32> check_to_sample;

		bit<9> in_port;
		

        bit<13> index_sketch0;
		bit<13> index_sketch1;
		bit<13> index_sketch2;
		bit<13> index_sketch3;

		bit<1> value_sketch0;
		bit<1> value_sketch1;
		bit<1> value_sketch2;
		bit<1> value_sketch3;

        bit<32> expected_ack;
        bit<32> pkt_signature;

        bit<16> hashed_location_1;
        bit<16> hashed_location_2;

        bit<32> table_1_read;
        bit<32> rtt;
        bit<32> lost;
		
		bit<8> lock;
		bit<32> seq_hash;

        bool pkt_type;
    
        bit<32> tmp_1;
        bit<32> tmp_2;
        bit<32> tmp_3;
        bit<32> total_hdr_len_bytes; 
        bit<32> total_body_len_bytes;

        bit<32> total_before;
		bit<32> total_after;

        bit<32> flow_current_time;

        bit<1> last_was_ack;
        bit<32> last_ack_arrival;

    }
    /***********************  P A R S E R  **************************/
    parser IngressParser(packet_in        pkt,
        /* User */
        out my_ingress_headers_t          hdr,
        out my_ingress_metadata_t         meta,
        /* Intrinsic */
        out ingress_intrinsic_metadata_t  ig_intr_md)
        {
            /* This is a mandatory state, required by Tofino Architecture */
            state start {
                pkt.extract(ig_intr_md);
                pkt.advance(PORT_METADATA_SIZE);
                transition parse_ethernet;
            }

            state parse_ethernet {
                pkt.extract(hdr.ethernet);
                transition parse_ipv4;
            }

            state parse_ipv4 {
                pkt.extract(hdr.ipv4);
                transition parse_tcp;
            }

            state parse_tcp {
                pkt.extract(hdr.tcp);
                transition accept;
            }

            state parse_udp {
                pkt.extract(hdr.udp);
                transition parse_rtp;
            }
            
            state parse_rtp {
                pkt.extract(hdr.rtp);
                transition accept;
            }


        }


    /***************** M A T C H - A C T I O N  *********************/
    control Ingress(
        /* User */
        inout my_ingress_headers_t                       hdr,
        inout my_ingress_metadata_t                      meta,
        /* Intrinsic */
        in    ingress_intrinsic_metadata_t               ig_intr_md,
        in    ingress_intrinsic_metadata_from_parser_t   ig_prsr_md,
        inout ingress_intrinsic_metadata_for_deparser_t  ig_dprsr_md,
        inout ingress_intrinsic_metadata_for_tm_t        ig_tm_md)
        {

            apply {
                if(hdr.tcp.isValid()){
                hdr.tmp.setValid();
                hdr.tmp.in_port = ig_intr_md.ingress_port;
                }
                //Port 140 is the one receiving the duplicated packets for calculating the queuing delay

                if(ig_intr_md.ingress_port == 132){
                    ig_tm_md.ucast_egress_port=156;
                }
                else if( ig_intr_md.ingress_port == 140){
                    ig_tm_md.ucast_egress_port=148;
                }
                else if( ig_intr_md.ingress_port == 156){
                    ig_tm_md.ucast_egress_port=132;
                }else if( ig_intr_md.ingress_port == 148){
                    ig_tm_md.ucast_egress_port=140;
                }

            }
        }

    /*********************  D E P A R S E R  ************************/
    control IngressDeparser(packet_out pkt,
        /* User */
        inout my_ingress_headers_t                       hdr,
        in    my_ingress_metadata_t                      meta,
        /* Intrinsic */
        in    ingress_intrinsic_metadata_for_deparser_t  ig_dprsr_md)
        {

            apply {
                pkt.emit(hdr);
            }
        }


/*************************************************************************
 ****************  E G R E S S   P R O C E S S I N G   *******************
 *************************************************************************/

    /***********************  H E A D E R S  ************************/
    struct my_egress_headers_t {
        ethernet_h   ethernet;
        ipv4_h       ipv4;
        tcp_h        tcp;
        tmp_h        tmp;
    }
    /********  G L O B A L   E G R E S S   M E T A D A T A  *********/
    struct my_egress_metadata_t {
        bit<32> packet_hash;
        bit<32> packet_queue_delay;		
        bit<11> flow_id;
    }
    /***********************  P A R S E R  **************************/
    parser EgressParser(packet_in        pkt,
        /* User */
        out my_egress_headers_t          hdr,
        out my_egress_metadata_t         meta,
        /* Intrinsic */
        out egress_intrinsic_metadata_t  eg_intr_md)
        {
            /* This is a mandatory state, required by Tofino Architecture */
            state start {
                pkt.extract(eg_intr_md);
                transition parse_ethernet;
            }

            state parse_ethernet {
                pkt.extract(hdr.ethernet);
                transition parse_ipv4;
            }

            state parse_ipv4 {
                pkt.extract(hdr.ipv4);
                transition parse_tcp;
            }

            state parse_tcp {
                pkt.extract(hdr.tcp);
                transition parse_tmp;
            }

            state parse_tmp {
                pkt.extract(hdr.tmp);
                transition accept;
            }
        }

    /***************** M A T C H - A C T I O N  *********************/
    control Egress(
        /* User */
        inout my_egress_headers_t                          hdr,
        inout my_egress_metadata_t                         meta,
        /* Intrinsic */
        in    egress_intrinsic_metadata_t                  eg_intr_md,
        in    egress_intrinsic_metadata_from_parser_t      eg_prsr_md,
        inout egress_intrinsic_metadata_for_deparser_t     eg_dprsr_md,
        inout egress_intrinsic_metadata_for_output_port_t  eg_oport_md)
        {

            Hash<bit<11>>(HashAlgorithm_t.CRC16) hash;
                action apply_hash() {
                    meta.flow_id = hash.get({
                        hdr.ipv4.src_addr,
                        hdr.ipv4.dst_addr,
                        hdr.ipv4.protocol,
                        hdr.tcp.src_port,
                        hdr.tcp.dst_port
                    });
                }
                table calc_flow_id {
                    actions = {
                        apply_hash;
                    }
                    const default_action = apply_hash();
                }
                
                
                // ------------------------- QUEUE DELAY--------------------------------------
                // ---------------------------------------------------------------------------
                
                Hash<bit<32>>(HashAlgorithm_t.CRC32) packet_hash;
                action apply_packet_hash() {
                    meta.packet_hash = packet_hash.get({
                        meta.flow_id,
                        hdr.tcp.seq_no
                    });
                }
                table calc_packet_hash {
                    actions = {
                        apply_packet_hash;
                    }
                    const default_action = apply_packet_hash();
                }
                Register<bit<32>, bit<17>>(100000) packets_timestamp;
                RegisterAction<bit<32>, bit<17>, bit<32>>(packets_timestamp) update_packets_timestamp = {
                    void apply(inout bit<32> register_data) {
                            // register_data = eg_prsr_md.global_tstamp[31:0];//[41:10]
                            register_data = eg_prsr_md.global_tstamp[33:2];//[41:10]
                    }
                };
                action exec_update_packets_timestamp(){
                    update_packets_timestamp.execute(meta.packet_hash[16:0]);
                }
                RegisterAction<bit<32>, bit<17>, bit<32>>(packets_timestamp) calc_queue_delay_packet = {
                    void apply(inout bit<32> register_data, out bit<32> result) {
                        if(eg_prsr_md.global_tstamp[33:2] > register_data && eg_prsr_md.global_tstamp[33:2] - register_data < 12500000) {
                            result = eg_prsr_md.global_tstamp[33:2] - register_data;
                        } else {
                            result = 0;
                        }
                    }
                };
                action exec_calc_queue_delay_packet(){
                    meta.packet_queue_delay = calc_queue_delay_packet.execute(meta.packet_hash[16:0]);
                }
                
                // Averaging
                Lpf<value_t, bit<1>>(size=1) lpf_queue_delay_1;
                Lpf<value_t, bit<1>>(size=1) lpf_queue_delay_2;
                value_t lpf_queue_delay_input;
                value_t lpf_queue_delay_output_1;
                value_t lpf_queue_delay_output_2;

                
                
                Register<bit<32>, _>(2048) queue_delays;
                RegisterAction<bit<32>, _, bit<32>>(queue_delays) update_queue_delays = {
                    void apply(inout bit<32> register_data) {
                        register_data = meta.packet_queue_delay;
                    }
                };
                action exec_update_queue_delays(){
                    update_queue_delays.execute(0);
                }


                apply {
                    calc_flow_id.apply();
                    calc_packet_hash.apply();
                    if (hdr.tmp.in_port  == 132) {
                        exec_update_packets_timestamp();
                    }
                    else if(hdr.tmp.in_port  == 156) {
                        exec_calc_queue_delay_packet();
                        if(meta.packet_queue_delay != 0) {
                            // lpf_queue_delay_input = (value_t)meta.packet_queue_delay;
                            // lpf_queue_delay_output_1 = lpf_queue_delay_1.execute(lpf_queue_delay_input, 0);
                            // lpf_queue_delay_output_2 = lpf_queue_delay_2.execute(lpf_queue_delay_output_1, 0);
                            // meta.packet_queue_delay = lpf_queue_delay_output_2;
                            exec_update_queue_delays();

                        }
                    }
                    // else if(ig_intr_md.ingress_port== 132){
                    //     exec_update_total_packets();
                    // }
                    // eg_dprsr_md.drop_ctl = 0;
                
                }
            }
        

    /*********************  D E P A R S E R  ************************/
    control EgressDeparser(packet_out pkt,
        /* User */
        inout my_egress_headers_t                       hdr,
        in my_egress_metadata_t                      meta,
        /* Intrinsic */
        in    egress_intrinsic_metadata_for_deparser_t  eg_dprsr_md)
        {
            apply {
                pkt.emit(hdr.ethernet);
                pkt.emit(hdr.ipv4);
                pkt.emit(hdr.tcp);
            }
        }


/************ F I N A L   P A C K A G E ******************************/
Pipeline(
    IngressParser(),
    Ingress(),
    IngressDeparser(),
    EgressParser(),
    Egress(),
    EgressDeparser()
) pipe;

Switch(pipe) main;



