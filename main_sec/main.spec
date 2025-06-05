



























struct ethernet_t {
	bit<48> dstAddr
	bit<48> srcAddr
	bit<16> etherType
}

struct ipv4_t {
	bit<8> version_ihl
	bit<8> diffserv
	bit<16> totalLen
	bit<16> identification
	bit<16> flags_fragOffset
	bit<8> ttl
	bit<8> protocol
	bit<16> hdrChecksum
	bit<32> srcAddr
	bit<32> dstAddr
}

struct tcp_t {
	bit<16> srcPort
	bit<16> dstPort
	bit<32> seqNo
	bit<32> ackNo
	bit<8> dataOffset_res
	bit<8> ecn_flags
	bit<16> window
	bit<16> checksum
	bit<16> urgentPtr
}

struct icmp_t {
	bit<8> type
	bit<8> code
	bit<16> checksum
	bit<16> id
	bit<16> seq
}

struct udp_t {
	bit<16> srcPort
	bit<16> dstPort
	bit<16> length_
	bit<16> checksum
}

struct forward_arg_t {
	bit<48> dstAddr
	bit<32> port_id
}

struct main_metadata_t {
	bit<32> pna_main_input_metadata_input_port
	bit<16> local_metadata_proto
	bit<16> local_metadata_flow_id0
	bit<16> local_metadata_flow_id1
	bit<16> local_metadata_flow_id2
	bit<16> local_metadata_flow_id3
	bit<16> local_metadata_flow_icmp_id0
	bit<16> local_metadata_flow_icmp_id1
	bit<16> local_metadata_flow_icmp_id2
	bit<16> local_metadata_flow_icmp_id3
	bit<32> local_metadata_count_0
	bit<32> local_metadata_count_1
	bit<32> local_metadata_count_2
	bit<32> local_metadata_count_3
	bit<32> local_metadata_minimum
	bit<32> local_metadata_dif
	bit<32> local_metadata_syn_drop_percent
	bit<32> local_metadata_syn_counts
	bit<32> local_metadata_syn_percent_iterator
	bit<32> local_metadata_synack_drop_percent
	bit<32> local_metadata_synack_counts
	bit<32> local_metadata_synack_percent_iterator
	bit<32> local_metadata_ack_drop_percent
	bit<32> local_metadata_ack_counts
	bit<32> local_metadata_ack_percent_iterator
	bit<32> local_metadata_add
	bit<32> local_metadata_count_icmp_0
	bit<32> local_metadata_count_icmp_1
	bit<32> local_metadata_count_icmp_2
	bit<32> local_metadata_count_icmp_3
	bit<32> local_metadata_minimum_icmp
	bit<32> local_metadata_dif_icmp
	bit<32> local_metadata_udp_drop_percent
	bit<32> local_metadata_udp_counts
	bit<32> local_metadata_udp_percent_iterator
	bit<32> pna_main_output_metadata_output_port
	bit<32> MainControlT_tmp
	bit<32> MainControlT_tmp_0
	bit<32> MainControlT_tmp_1
	bit<8> MainControlT_tmp_2
	bit<8> MainControlT_tmp_3
	bit<8> MainControlT_tmp_5
	bit<8> MainControlT_tmp_6
	bit<8> MainControlT_tmp_8
	bit<8> MainControlT_tmp_9
	bit<8> MainControlT_tmp_11
	bit<8> MainControlT_tmp_12
	bit<8> MainControlT_tmp_14
	bit<8> MainControlT_tmp_15
	bit<8> MainControlT_tmp_17
	bit<8> MainControlT_tmp_18
	bit<32> MainControlT_tmp_20
	bit<32> MainControlT_tmp_21
	bit<32> MainControlT_tmp_22
	bit<16> MainControlT_tmp_23
	bit<16> MainControlT_tmp_24
	bit<32> MainControlT_tmp_25
	bit<32> MainControlT_tmp_26
	bit<8> MainControlT_tmp_27
	bit<16> MainControlT_tmp_28
	bit<16> MainControlT_tmp_29
	bit<32> MainControlT_tmp_30
	bit<32> MainControlT_tmp_31
	bit<8> MainControlT_tmp_32
	bit<16> MainControlT_tmp_33
	bit<16> MainControlT_tmp_34
	bit<32> MainControlT_tmp_35
	bit<32> MainControlT_tmp_36
	bit<8> MainControlT_tmp_37
	bit<16> MainControlT_tmp_38
	bit<16> MainControlT_tmp_39
	bit<32> MainControlT_tmp_40
	bit<32> MainControlT_tmp_41
	bit<8> MainControlT_tmp_42
	bit<32> MainControlT_tmp_43
	bit<32> MainControlT_tmp_44
	bit<32> MainControlT_tmp_45
	bit<32> MainControlT_tmp_46
	bit<32> MainControlT_tmp_47
	bit<32> MainControlT_tmp_48
	bit<32> MainControlT_tmp_49
	bit<32> MainControlT_tmp_50
	bit<32> MainControlT_tmp_51
	bit<32> MainControlT_tmp_52
	bit<32> MainControlT_tmp_53
	bit<32> MainControlT_tmp_54
	bit<32> MainControlT_tmp_55
	bit<32> MainControlT_tmp_56
	bit<32> MainControlT_tmp_57
	bit<32> MainControlT_tmp_58
	bit<8> timeout_id
	bit<8> timeout_id_0
}
metadata instanceof main_metadata_t

header ethernet instanceof ethernet_t
header ipv4 instanceof ipv4_t
header tcp instanceof tcp_t
header icmp instanceof icmp_t
header udp instanceof udp_t

regarray attack size 0x1 initval 0
regarray reg_state_ts size 0x1 initval 0
regarray reg_timestamp1 size 0x1 initval 0
regarray reg_timestamp2 size 0x1 initval 0
regarray reg_timestamp3 size 0x1 initval 0
regarray get_tcp_flow_flow_id0 size 0x1 initval 0
regarray get_tcp_flow_flow_id1 size 0x1 initval 0
regarray get_tcp_flow_flow_id2 size 0x1 initval 0
regarray get_tcp_flow_flow_id3 size 0x1 initval 0
regarray get_icmp_flow_flow_icmp_id0 size 0x1 initval 0
regarray get_icmp_flow_flow_icmp_id1 size 0x1 initval 0
regarray get_icmp_flow_flow_icmp_id2 size 0x1 initval 0
regarray get_icmp_flow_flow_icmp_id3 size 0x1 initval 0
regarray heavy_hitter_ht0 size 0x8000 initval 0
regarray heavy_hitter_ht1 size 0x8000 initval 0
regarray heavy_hitter_ht2 size 0x8000 initval 0
regarray heavy_hitter_ht3 size 0x8000 initval 0
regarray syn_flood_syn_counts_reg size 0x1 initval 0
regarray syn_flood_syn_percent_iterator_reg size 0x1 initval 0
regarray syn_ack_flood_synack_counts_reg size 0x1 initval 0
regarray syn_ack_flood_synack_percent_iterator_reg size 0x1 initval 0
regarray ack_flood_ack_counts_reg size 0x1 initval 0
regarray ack_flood_ack_percent_iterator_reg size 0x1 initval 0
regarray icmp_flood_ht_icmp size 0x8000 initval 0
regarray icmp_flood_ht_icmp_0 size 0x8000 initval 0
regarray icmp_flood_ht_icmp_1 size 0x8000 initval 0
regarray icmp_flood_ht_icmp_2 size 0x8000 initval 0
regarray udp_flood_udp_counts_reg size 0x1 initval 0
regarray udp_flood_udp_percent_iterator_reg size 0x1 initval 0
regarray proto_0 size 0x1 initval 0
regarray direction size 0x100 initval 0
action drop args none {
	drop
	return
}

action forward args instanceof forward_arg_t {
	mov m.pna_main_output_metadata_output_port t.port_id
	mov h.ethernet.srcAddr h.ethernet.dstAddr
	mov h.ethernet.dstAddr t.dstAddr
	add h.ipv4.ttl 0xFF
	return
}

action noAction args none {
	return
}

action add_miss args none {
	jmpneq LABEL_END_34 m.local_metadata_add 0x1
	mov m.timeout_id 0x4
	learn noAction m.timeout_id
	LABEL_END_34 :	return
}

action udp_flood_noAction_0 args none {
	return
}

action udp_flood_add_miss_udp_0 args none {
	mov m.timeout_id_0 0x4
	learn udp_flood_noAction_0 m.timeout_id_0
	return
}

table forwarding {
	key {
		h.ipv4.dstAddr exact
	}
	actions {
		forward
		drop
	}
	default_action drop args none 
	size 0x400
}


learner open_tcp {
	key {
		h.ipv4.srcAddr
	}
	actions {
		noAction
		add_miss
	}
	default_action add_miss args none 
	size 0x400
	timeout {
		10
		30
		60
		120
		300
		43200
		120
		120

		}
}

learner udp_flood_open_udp {
	key {
		h.ipv4.srcAddr
		h.ipv4.dstAddr
	}
	actions {
		udp_flood_noAction_0
		udp_flood_add_miss_udp_0
	}
	default_action udp_flood_add_miss_udp_0 args none 
	size 0x400
	timeout {
		10
		30
		60
		120
		300
		43200
		120
		120

		}
}

apply {
	rx m.pna_main_input_metadata_input_port
	extract h.ethernet
	jmpeq MAINPARSERIMPL_PARSE_IPV4 h.ethernet.etherType 0x800
	jmp MAINPARSERIMPL_ACCEPT
	MAINPARSERIMPL_PARSE_IPV4 :	extract h.ipv4
	jmpeq MAINPARSERIMPL_PARSE_TCP h.ipv4.protocol 0x6
	jmpeq MAINPARSERIMPL_PARSE_ICMP h.ipv4.protocol 0x1
	jmpeq MAINPARSERIMPL_PARSE_UDP h.ipv4.protocol 0x11
	jmp MAINPARSERIMPL_ACCEPT
	MAINPARSERIMPL_PARSE_UDP :	extract h.udp
	jmp MAINPARSERIMPL_ACCEPT
	MAINPARSERIMPL_PARSE_TCP :	extract h.tcp
	jmp MAINPARSERIMPL_ACCEPT
	MAINPARSERIMPL_PARSE_ICMP :	extract h.icmp
	MAINPARSERIMPL_ACCEPT :	jmpnv LABEL_FALSE h.ipv4
	table forwarding
	mov m.local_metadata_proto h.ipv4.protocol
	regwr proto_0 0x0 m.local_metadata_proto
	jmpnv LABEL_FALSE_0 h.tcp
	mov m.MainControlT_tmp_17 h.tcp.ecn_flags
	and m.MainControlT_tmp_17 0x1F
	mov m.MainControlT_tmp_18 m.MainControlT_tmp_17
	and m.MainControlT_tmp_18 0x1F
	jmpneq LABEL_FALSE_1 m.MainControlT_tmp_18 0x2
	regwr attack 0x0 0x1
	mov m.local_metadata_syn_drop_percent 0x19
	regrd m.local_metadata_syn_counts syn_flood_syn_counts_reg 0x0
	add m.local_metadata_syn_counts 0x1
	regwr syn_flood_syn_counts_reg 0x0 m.local_metadata_syn_counts
	jmpgt LABEL_TRUE_2 m.local_metadata_syn_counts 0xF4240
	jmp LABEL_END
	LABEL_TRUE_2 :	regrd m.local_metadata_syn_percent_iterator syn_flood_syn_percent_iterator_reg 0x0
	jmplt LABEL_TRUE_3 m.local_metadata_syn_percent_iterator 0x19
	jmplt LABEL_TRUE_4 m.local_metadata_syn_percent_iterator 0x64
	jmpneq LABEL_END m.local_metadata_syn_percent_iterator 0x64
	mov m.local_metadata_syn_percent_iterator 0x0
	regwr syn_flood_syn_percent_iterator_reg 0x0 m.local_metadata_syn_percent_iterator
	jmp LABEL_END
	jmp LABEL_END
	LABEL_TRUE_4 :	add m.local_metadata_syn_percent_iterator 0x1
	and m.local_metadata_syn_percent_iterator 0x7F
	regwr syn_flood_syn_percent_iterator_reg 0x0 m.local_metadata_syn_percent_iterator
	jmp LABEL_END
	LABEL_TRUE_3 :	add m.local_metadata_syn_percent_iterator 0x1
	and m.local_metadata_syn_percent_iterator 0x7F
	regwr syn_flood_syn_percent_iterator_reg 0x0 m.local_metadata_syn_percent_iterator
	drop
	jmp LABEL_END
	LABEL_FALSE_1 :	mov m.MainControlT_tmp_14 h.tcp.ecn_flags
	and m.MainControlT_tmp_14 0x1F
	mov m.MainControlT_tmp_15 m.MainControlT_tmp_14
	and m.MainControlT_tmp_15 0x1F
	jmpneq LABEL_FALSE_6 m.MainControlT_tmp_15 0x12
	regwr attack 0x0 0x2
	mov m.local_metadata_synack_drop_percent 0x32
	regrd m.local_metadata_synack_counts syn_ack_flood_synack_counts_reg 0x0
	add m.local_metadata_synack_counts 0x1
	regwr syn_ack_flood_synack_counts_reg 0x0 m.local_metadata_synack_counts
	jmpgt LABEL_TRUE_7 m.local_metadata_synack_counts 0xF4240
	jmp LABEL_END
	LABEL_TRUE_7 :	regrd m.local_metadata_synack_percent_iterator syn_ack_flood_synack_percent_iterator_reg 0x0
	jmplt LABEL_TRUE_8 m.local_metadata_synack_percent_iterator 0x32
	jmplt LABEL_TRUE_9 m.local_metadata_synack_percent_iterator 0x64
	jmpneq LABEL_END m.local_metadata_synack_percent_iterator 0x64
	mov m.local_metadata_synack_percent_iterator 0x0
	regwr syn_ack_flood_synack_percent_iterator_reg 0x0 m.local_metadata_synack_percent_iterator
	jmp LABEL_END
	jmp LABEL_END
	LABEL_TRUE_9 :	add m.local_metadata_synack_percent_iterator 0x1
	and m.local_metadata_synack_percent_iterator 0x7F
	regwr syn_ack_flood_synack_percent_iterator_reg 0x0 m.local_metadata_synack_percent_iterator
	jmp LABEL_END
	LABEL_TRUE_8 :	add m.local_metadata_synack_percent_iterator 0x1
	and m.local_metadata_synack_percent_iterator 0x7F
	regwr syn_ack_flood_synack_percent_iterator_reg 0x0 m.local_metadata_synack_percent_iterator
	drop
	jmp LABEL_END
	LABEL_FALSE_6 :	mov m.MainControlT_tmp_11 h.tcp.ecn_flags
	and m.MainControlT_tmp_11 0x1F
	mov m.MainControlT_tmp_12 m.MainControlT_tmp_11
	and m.MainControlT_tmp_12 0x1F
	jmpneq LABEL_FALSE_11 m.MainControlT_tmp_12 0x10
	regwr attack 0x0 0x3
	mov m.local_metadata_add 0x1
	mov m.local_metadata_ack_drop_percent 0x4B
	regrd m.local_metadata_ack_counts ack_flood_ack_counts_reg 0x0
	add m.local_metadata_ack_counts 0x1
	regwr ack_flood_ack_counts_reg 0x0 m.local_metadata_ack_counts
	jmpgt LABEL_TRUE_12 m.local_metadata_ack_counts 0xF4240
	jmp LABEL_END_12
	LABEL_TRUE_12 :	regrd m.local_metadata_ack_percent_iterator ack_flood_ack_percent_iterator_reg 0x0
	jmplt LABEL_TRUE_13 m.local_metadata_ack_percent_iterator 0x4B
	jmplt LABEL_TRUE_14 m.local_metadata_ack_percent_iterator 0x64
	jmpneq LABEL_END_12 m.local_metadata_ack_percent_iterator 0x64
	mov m.local_metadata_ack_percent_iterator 0x0
	regwr ack_flood_ack_percent_iterator_reg 0x0 m.local_metadata_ack_percent_iterator
	jmp LABEL_END_12
	jmp LABEL_END_12
	LABEL_TRUE_14 :	add m.local_metadata_ack_percent_iterator 0x1
	and m.local_metadata_ack_percent_iterator 0x7F
	regwr ack_flood_ack_percent_iterator_reg 0x0 m.local_metadata_ack_percent_iterator
	jmp LABEL_END_12
	LABEL_TRUE_13 :	add m.local_metadata_ack_percent_iterator 0x1
	and m.local_metadata_ack_percent_iterator 0x7F
	regwr ack_flood_ack_percent_iterator_reg 0x0 m.local_metadata_ack_percent_iterator
	drop
	LABEL_END_12 :	table open_tcp
	jmp LABEL_END
	LABEL_FALSE_11 :	mov m.MainControlT_tmp_2 h.tcp.ecn_flags
	and m.MainControlT_tmp_2 0x1F
	mov m.MainControlT_tmp_3 m.MainControlT_tmp_2
	and m.MainControlT_tmp_3 0x1F
	mov m.MainControlT_tmp_5 h.tcp.ecn_flags
	and m.MainControlT_tmp_5 0x1F
	mov m.MainControlT_tmp_6 m.MainControlT_tmp_5
	and m.MainControlT_tmp_6 0x1F
	mov m.MainControlT_tmp_8 h.tcp.ecn_flags
	and m.MainControlT_tmp_8 0x1F
	mov m.MainControlT_tmp_9 m.MainControlT_tmp_8
	and m.MainControlT_tmp_9 0x1F
	jmpeq LABEL_TRUE_16 m.MainControlT_tmp_3 0x1
	jmpeq LABEL_TRUE_16 m.MainControlT_tmp_6 0x4
	jmpeq LABEL_TRUE_16 m.MainControlT_tmp_9 0x5
	mov m.MainControlT_tmp_23 h.tcp.srcPort
	mov m.MainControlT_tmp_24 h.tcp.dstPort
	mov m.MainControlT_tmp_25 h.ipv4.srcAddr
	mov m.MainControlT_tmp_26 h.ipv4.dstAddr
	mov m.MainControlT_tmp_27 h.ipv4.protocol
	hash crc32 m.local_metadata_flow_id0  m.MainControlT_tmp_23 m.MainControlT_tmp_27
	and m.local_metadata_flow_id0 0x7FFF
	add m.local_metadata_flow_id0 0x0
	mov m.MainControlT_tmp_28 h.tcp.srcPort
	mov m.MainControlT_tmp_29 h.tcp.dstPort
	mov m.MainControlT_tmp_30 h.ipv4.srcAddr
	mov m.MainControlT_tmp_31 h.ipv4.dstAddr
	mov m.MainControlT_tmp_32 h.ipv4.protocol
	hash crc32 m.local_metadata_flow_id1  m.MainControlT_tmp_28 m.MainControlT_tmp_32
	and m.local_metadata_flow_id1 0x7FFF
	add m.local_metadata_flow_id1 0x64
	mov m.MainControlT_tmp_33 h.tcp.srcPort
	mov m.MainControlT_tmp_34 h.tcp.dstPort
	mov m.MainControlT_tmp_35 h.ipv4.srcAddr
	mov m.MainControlT_tmp_36 h.ipv4.dstAddr
	mov m.MainControlT_tmp_37 h.ipv4.protocol
	hash crc32 m.local_metadata_flow_id2  m.MainControlT_tmp_33 m.MainControlT_tmp_37
	and m.local_metadata_flow_id2 0x7FFF
	add m.local_metadata_flow_id2 0xC8
	mov m.MainControlT_tmp_38 h.tcp.srcPort
	mov m.MainControlT_tmp_39 h.tcp.dstPort
	mov m.MainControlT_tmp_40 h.ipv4.srcAddr
	mov m.MainControlT_tmp_41 h.ipv4.dstAddr
	mov m.MainControlT_tmp_42 h.ipv4.protocol
	hash crc32 m.local_metadata_flow_id3  m.MainControlT_tmp_38 m.MainControlT_tmp_42
	and m.local_metadata_flow_id3 0x7FFF
	add m.local_metadata_flow_id3 0x12C
	regwr get_tcp_flow_flow_id0 0x0 m.local_metadata_flow_id0
	regwr get_tcp_flow_flow_id1 0x0 m.local_metadata_flow_id1
	regwr get_tcp_flow_flow_id2 0x0 m.local_metadata_flow_id2
	regwr get_tcp_flow_flow_id3 0x0 m.local_metadata_flow_id3
	regwr attack 0x0 0x5
	mov m.local_metadata_minimum 0xFFFFF
	regrd m.local_metadata_count_0 heavy_hitter_ht0 m.local_metadata_flow_id0
	regrd m.local_metadata_count_1 heavy_hitter_ht1 m.local_metadata_flow_id1
	regrd m.local_metadata_count_2 heavy_hitter_ht2 m.local_metadata_flow_id2
	regrd m.local_metadata_count_3 heavy_hitter_ht3 m.local_metadata_flow_id3
	mov m.local_metadata_dif 0xFFFFF
	sub m.local_metadata_dif m.local_metadata_count_0
	and m.local_metadata_dif 0xFFFFF
	mov m.MainControlT_tmp 0xFFFFF
	sub m.MainControlT_tmp m.local_metadata_count_0
	and m.MainControlT_tmp 0xFFFFF
	jmpgt LABEL_TRUE_17 m.MainControlT_tmp 0x0
	jmp LABEL_END_17
	LABEL_TRUE_17 :	mov m.local_metadata_minimum m.local_metadata_count_0
	LABEL_END_17 :	mov m.local_metadata_dif m.local_metadata_minimum
	sub m.local_metadata_dif m.local_metadata_count_1
	and m.local_metadata_dif 0xFFFFF
	mov m.MainControlT_tmp_0 m.local_metadata_minimum
	sub m.MainControlT_tmp_0 m.local_metadata_count_1
	and m.MainControlT_tmp_0 0xFFFFF
	jmpgt LABEL_TRUE_18 m.MainControlT_tmp_0 0x0
	jmp LABEL_END_18
	LABEL_TRUE_18 :	mov m.local_metadata_minimum m.local_metadata_count_1
	LABEL_END_18 :	mov m.local_metadata_dif m.local_metadata_minimum
	sub m.local_metadata_dif m.local_metadata_count_2
	and m.local_metadata_dif 0xFFFFF
	mov m.MainControlT_tmp_1 m.local_metadata_minimum
	sub m.MainControlT_tmp_1 m.local_metadata_count_2
	and m.MainControlT_tmp_1 0xFFFFF
	jmpgt LABEL_TRUE_19 m.MainControlT_tmp_1 0x0
	jmp LABEL_END_19
	LABEL_TRUE_19 :	mov m.local_metadata_minimum m.local_metadata_count_2
	LABEL_END_19 :	jmpgt LABEL_TRUE_20 m.local_metadata_minimum 0x186A0
	mov m.MainControlT_tmp_51 m.local_metadata_count_0
	add m.MainControlT_tmp_51 0x1
	and m.MainControlT_tmp_51 0xFFFFF
	regwr heavy_hitter_ht0 m.local_metadata_flow_id0 m.MainControlT_tmp_51
	mov m.MainControlT_tmp_52 m.local_metadata_count_1
	add m.MainControlT_tmp_52 0x1
	and m.MainControlT_tmp_52 0xFFFFF
	regwr heavy_hitter_ht1 m.local_metadata_flow_id1 m.MainControlT_tmp_52
	mov m.MainControlT_tmp_53 m.local_metadata_count_2
	add m.MainControlT_tmp_53 0x1
	and m.MainControlT_tmp_53 0xFFFFF
	regwr heavy_hitter_ht2 m.local_metadata_flow_id2 m.MainControlT_tmp_53
	mov m.MainControlT_tmp_54 m.local_metadata_count_3
	add m.MainControlT_tmp_54 0x1
	and m.MainControlT_tmp_54 0xFFFFF
	regwr heavy_hitter_ht3 m.local_metadata_flow_id3 m.MainControlT_tmp_54
	jmp LABEL_END
	LABEL_TRUE_20 :	drop
	jmp LABEL_END
	LABEL_TRUE_16 :	regwr attack 0x0 0x4
	mov m.local_metadata_add 0x0
	table open_tcp
	jmpnh LABEL_FALSE_21
	jmp LABEL_END
	LABEL_FALSE_21 :	drop
	jmp LABEL_END
	LABEL_FALSE_0 :	jmpnv LABEL_FALSE_22 h.icmp
	jmpeq LABEL_TRUE_23 h.icmp.type 0x8
	jmpeq LABEL_TRUE_23 h.icmp.type 0x63
	jmp LABEL_END_23
	LABEL_TRUE_23 :	mov m.MainControlT_tmp_43 h.ipv4.srcAddr
	mov m.MainControlT_tmp_44 h.ipv4.dstAddr
	hash crc32 m.local_metadata_flow_icmp_id0  m.MainControlT_tmp_43 m.MainControlT_tmp_44
	and m.local_metadata_flow_icmp_id0 0x7FFF
	add m.local_metadata_flow_icmp_id0 0x0
	mov m.MainControlT_tmp_45 h.ipv4.srcAddr
	mov m.MainControlT_tmp_46 h.ipv4.dstAddr
	hash crc32 m.local_metadata_flow_icmp_id1  m.MainControlT_tmp_45 m.MainControlT_tmp_46
	and m.local_metadata_flow_icmp_id1 0x7FFF
	add m.local_metadata_flow_icmp_id1 0x64
	mov m.MainControlT_tmp_47 h.ipv4.srcAddr
	mov m.MainControlT_tmp_48 h.ipv4.dstAddr
	hash crc32 m.local_metadata_flow_icmp_id2  m.MainControlT_tmp_47 m.MainControlT_tmp_48
	and m.local_metadata_flow_icmp_id2 0x7FFF
	add m.local_metadata_flow_icmp_id2 0xC8
	mov m.MainControlT_tmp_49 h.ipv4.srcAddr
	mov m.MainControlT_tmp_50 h.ipv4.dstAddr
	hash crc32 m.local_metadata_flow_icmp_id3  m.MainControlT_tmp_49 m.MainControlT_tmp_50
	and m.local_metadata_flow_icmp_id3 0x7FFF
	add m.local_metadata_flow_icmp_id3 0x12C
	regwr get_icmp_flow_flow_icmp_id0 0x0 m.local_metadata_flow_icmp_id0
	regwr get_icmp_flow_flow_icmp_id1 0x0 m.local_metadata_flow_icmp_id1
	regwr get_icmp_flow_flow_icmp_id2 0x0 m.local_metadata_flow_icmp_id2
	regwr get_icmp_flow_flow_icmp_id3 0x0 m.local_metadata_flow_icmp_id3
	LABEL_END_23 :	regwr attack 0x0 0x6
	mov m.local_metadata_minimum 0xFFFFF
	regrd m.local_metadata_count_icmp_0 icmp_flood_ht_icmp m.local_metadata_flow_icmp_id0
	regrd m.local_metadata_count_icmp_1 icmp_flood_ht_icmp_0 m.local_metadata_flow_icmp_id1
	regrd m.local_metadata_count_icmp_2 icmp_flood_ht_icmp_1 m.local_metadata_flow_icmp_id2
	regrd m.local_metadata_count_icmp_3 icmp_flood_ht_icmp_2 m.local_metadata_flow_icmp_id3
	mov m.local_metadata_dif_icmp m.local_metadata_minimum_icmp
	sub m.local_metadata_dif_icmp m.local_metadata_count_icmp_0
	and m.local_metadata_dif_icmp 0xFFFFF
	mov m.MainControlT_tmp_20 m.local_metadata_minimum_icmp
	sub m.MainControlT_tmp_20 m.local_metadata_count_icmp_0
	and m.MainControlT_tmp_20 0xFFFFF
	jmpgt LABEL_TRUE_24 m.MainControlT_tmp_20 0x0
	jmp LABEL_END_24
	LABEL_TRUE_24 :	mov m.local_metadata_minimum_icmp m.local_metadata_count_icmp_0
	LABEL_END_24 :	mov m.local_metadata_dif_icmp m.local_metadata_minimum_icmp
	sub m.local_metadata_dif_icmp m.local_metadata_count_icmp_1
	and m.local_metadata_dif_icmp 0xFFFFF
	mov m.MainControlT_tmp_21 m.local_metadata_minimum_icmp
	sub m.MainControlT_tmp_21 m.local_metadata_count_icmp_1
	and m.MainControlT_tmp_21 0xFFFFF
	jmpgt LABEL_TRUE_25 m.MainControlT_tmp_21 0x0
	jmp LABEL_END_25
	LABEL_TRUE_25 :	mov m.local_metadata_minimum_icmp m.local_metadata_count_icmp_1
	LABEL_END_25 :	mov m.local_metadata_dif_icmp m.local_metadata_minimum_icmp
	sub m.local_metadata_dif_icmp m.local_metadata_count_icmp_2
	and m.local_metadata_dif_icmp 0xFFFFF
	mov m.MainControlT_tmp_22 m.local_metadata_minimum_icmp
	sub m.MainControlT_tmp_22 m.local_metadata_count_icmp_2
	and m.MainControlT_tmp_22 0xFFFFF
	jmpgt LABEL_TRUE_26 m.MainControlT_tmp_22 0x0
	jmp LABEL_END_26
	LABEL_TRUE_26 :	mov m.local_metadata_minimum_icmp m.local_metadata_count_icmp_2
	LABEL_END_26 :	jmpgt LABEL_TRUE_27 m.local_metadata_minimum_icmp 0x30D40
	mov m.MainControlT_tmp_55 m.local_metadata_count_icmp_0
	add m.MainControlT_tmp_55 0x1
	and m.MainControlT_tmp_55 0xFFFFF
	regwr icmp_flood_ht_icmp m.local_metadata_flow_icmp_id0 m.MainControlT_tmp_55
	mov m.MainControlT_tmp_56 m.local_metadata_count_icmp_1
	add m.MainControlT_tmp_56 0x1
	and m.MainControlT_tmp_56 0xFFFFF
	regwr icmp_flood_ht_icmp_0 m.local_metadata_flow_icmp_id1 m.MainControlT_tmp_56
	mov m.MainControlT_tmp_57 m.local_metadata_count_icmp_2
	add m.MainControlT_tmp_57 0x1
	and m.MainControlT_tmp_57 0xFFFFF
	regwr icmp_flood_ht_icmp_1 m.local_metadata_flow_icmp_id2 m.MainControlT_tmp_57
	mov m.MainControlT_tmp_58 m.local_metadata_count_icmp_3
	add m.MainControlT_tmp_58 0x1
	and m.MainControlT_tmp_58 0xFFFFF
	regwr icmp_flood_ht_icmp_2 m.local_metadata_flow_icmp_id3 m.MainControlT_tmp_58
	jmp LABEL_END
	LABEL_TRUE_27 :	drop
	jmp LABEL_END
	LABEL_FALSE_22 :	jmpnv LABEL_FALSE_28 h.udp
	regwr attack 0x0 0x7
	table udp_flood_open_udp
	jmpnh LABEL_END
	mov m.local_metadata_udp_drop_percent 0x32
	regrd m.local_metadata_udp_counts udp_flood_udp_counts_reg 0x0
	add m.local_metadata_udp_counts 0x1
	regwr udp_flood_udp_counts_reg 0x0 m.local_metadata_udp_counts
	jmpgt LABEL_TRUE_30 m.local_metadata_udp_counts 0xF4240
	jmp LABEL_END
	LABEL_TRUE_30 :	regrd m.local_metadata_udp_percent_iterator udp_flood_udp_percent_iterator_reg 0x0
	jmplt LABEL_TRUE_31 m.local_metadata_udp_percent_iterator 0x32
	jmplt LABEL_TRUE_32 m.local_metadata_udp_percent_iterator 0x64
	jmpneq LABEL_END m.local_metadata_udp_percent_iterator 0x64
	mov m.local_metadata_udp_percent_iterator 0x0
	regwr udp_flood_udp_percent_iterator_reg 0x0 m.local_metadata_udp_percent_iterator
	jmp LABEL_END
	jmp LABEL_END
	LABEL_TRUE_32 :	add m.local_metadata_udp_percent_iterator 0x1
	and m.local_metadata_udp_percent_iterator 0x7F
	regwr udp_flood_udp_percent_iterator_reg 0x0 m.local_metadata_udp_percent_iterator
	jmp LABEL_END
	LABEL_TRUE_31 :	add m.local_metadata_udp_percent_iterator 0x1
	and m.local_metadata_udp_percent_iterator 0x7F
	regwr udp_flood_udp_percent_iterator_reg 0x0 m.local_metadata_udp_percent_iterator
	drop
	jmp LABEL_END
	LABEL_FALSE_28 :	regwr attack 0x0 0xF
	drop
	jmp LABEL_END
	LABEL_FALSE :	regwr attack 0x0 0xF
	drop
	LABEL_END :	emit h.ethernet
	emit h.ipv4
	emit h.tcp
	emit h.icmp
	emit h.udp
	tx m.pna_main_output_metadata_output_port
}


