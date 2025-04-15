







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

struct main_metadata_t {
	bit<64> pna_main_input_metadata_timestamp
	bit<32> pna_main_input_metadata_input_port
	bit<16> local_metadata_flow_id0
	bit<32> local_metadata_count_0
	bit<64> local_metadata_last_timestamp
	bit<64> local_metadata_current_timestamp
	bit<64> local_metadata_interarrival_value
	bit<32> pna_main_output_metadata_output_port
	bit<32> MainControlT_tmp_0
	bit<32> MainControlT_tmp_1
	bit<32> MainControlT_tmp_7
	bit<32> MainControlT_tmp_8
	bit<32> MainControlT_tmp_ip
	bit<48> MainControlT_tmp_mac
}
metadata instanceof main_metadata_t

header ethernet instanceof ethernet_t
header ipv4 instanceof ipv4_t
header tcp instanceof tcp_t

regarray reg_index_0 size 0x1 initval 0
regarray ht0_0 size 0x8000 initval 0
regarray reg_last_0 size 0x8000 initval 0
regarray reg_curr_0 size 0x8000 initval 0
regarray reg_last_timestamp_0 size 0x8000 initval 0
regarray reg_iat_0 size 0x8000 initval 0
regarray direction size 0x100 initval 0
apply {
	rx m.pna_main_input_metadata_input_port
	extract h.ethernet
	jmpeq MAINPARSERIMPL_PARSE_IPV4 h.ethernet.etherType 0x800
	jmp MAINPARSERIMPL_ACCEPT
	MAINPARSERIMPL_PARSE_IPV4 :	extract h.ipv4
	jmpeq MAINPARSERIMPL_PARSE_TCP h.ipv4.protocol 0x6
	jmp MAINPARSERIMPL_ACCEPT
	MAINPARSERIMPL_PARSE_TCP :	extract h.tcp
	MAINPARSERIMPL_ACCEPT :	jmpnv LABEL_END h.ipv4
	mov m.MainControlT_tmp_0 h.ipv4.srcAddr
	mov m.MainControlT_tmp_1 h.ipv4.dstAddr
	hash crc32 m.local_metadata_flow_id0  m.MainControlT_tmp_0 m.MainControlT_tmp_1
	and m.local_metadata_flow_id0 0x7FFF
	add m.local_metadata_flow_id0 0x0
	mov m.MainControlT_tmp_7 m.local_metadata_flow_id0
	regwr reg_index_0 0x0 m.MainControlT_tmp_7
	regrd m.local_metadata_last_timestamp reg_last_timestamp_0 m.local_metadata_flow_id0
	mov m.local_metadata_current_timestamp m.pna_main_input_metadata_timestamp
	jmpeq LABEL_FALSE_0 m.local_metadata_last_timestamp 0x0
	regwr reg_last_0 m.local_metadata_flow_id0 m.local_metadata_last_timestamp
	regwr reg_curr_0 m.local_metadata_flow_id0 m.local_metadata_current_timestamp
	mov m.local_metadata_interarrival_value m.pna_main_input_metadata_timestamp
	sub m.local_metadata_interarrival_value m.local_metadata_last_timestamp
	jmp LABEL_END_0
	LABEL_FALSE_0 :	mov m.local_metadata_interarrival_value 0x0
	LABEL_END_0 :	regwr reg_iat_0 m.local_metadata_flow_id0 m.local_metadata_interarrival_value
	regwr reg_last_timestamp_0 m.local_metadata_flow_id0 m.local_metadata_current_timestamp
	regrd m.local_metadata_count_0 ht0_0 m.local_metadata_flow_id0
	mov m.MainControlT_tmp_8 m.local_metadata_count_0
	add m.MainControlT_tmp_8 0x1
	and m.MainControlT_tmp_8 0xFFFFF
	regwr ht0_0 m.local_metadata_flow_id0 m.MainControlT_tmp_8
	mov m.MainControlT_tmp_ip h.ipv4.srcAddr
	mov h.ipv4.srcAddr h.ipv4.dstAddr
	mov h.ipv4.dstAddr m.MainControlT_tmp_ip
	mov m.MainControlT_tmp_mac h.ethernet.srcAddr
	mov h.ethernet.srcAddr h.ethernet.dstAddr
	mov h.ethernet.dstAddr m.MainControlT_tmp_mac
	jmpneq LABEL_FALSE_1 m.pna_main_input_metadata_input_port 0x0
	mov m.pna_main_output_metadata_output_port 0x0
	jmp LABEL_END
	LABEL_FALSE_1 :	jmpneq LABEL_END m.pna_main_input_metadata_input_port 0x1
	mov m.pna_main_output_metadata_output_port 0x1
	LABEL_END :	emit h.ethernet
	emit h.ipv4
	emit h.tcp
	tx m.pna_main_output_metadata_output_port
}


