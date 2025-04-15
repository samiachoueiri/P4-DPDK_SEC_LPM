typedef bit<48> EthernetAddress;
typedef bit<32> IP4Address;  
const bit<16> TYPE_IPV4 = 0x0800;
const bit<8> TYPE_TCP = 0x6;
const bit<8> TYPE_ICMP = 0x1;
const bit<8> TYPE_UDP = 0x11;

//-----------------------------HH
#define THRESH_HH 100000
//-----------------------------SYN 
#define THRESH_SYN 1000000
#define SYN_DROP_RATE 25
//-----------------------------SYN-ACK 
#define THRESH_SYNACK 1000000
#define SYNACK_DROP_RATE 50
//-----------------------------ACK
#define THRESH_ACK 1000000
#define ACK_DROP_RATE 75
//-----------------------------FIN-RST
const ExpireTimeProfileId_t EXPIRE_TIME_PROFILE_ID = (ExpireTimeProfileId_t) 4;
//-----------------------------ICMP-REQ
#define THRESH_ICMP 200000
//-----------------------------UDP 1000000 / 500000 / 333333 / 250000 / 200000 / 166666 / 142857 / 125000
#define THRESH_UDP 1000000
#define UDP_DROP_RATE 50

#define SKETCH_LENGTH 32768
#define SKETCH_WIDTH 1 //32

header ethernet_t {
    EthernetAddress dstAddr;
    EthernetAddress srcAddr;
    bit<16>         etherType;
}

header ipv4_t {
    bit<4>  version;
    bit<4>  ihl;
    bit<8>  diffserv;
    bit<16> totalLen;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragOffset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> hdrChecksum;
    IP4Address srcAddr;
    IP4Address dstAddr;
}

header tcp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4>  dataOffset;
    bit<4>  res;
    bit<3>  ecn;
    bit<5>  flags; //ACK,PSH,RST,SYN,FIN
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr; 
}

header icmp_t {
    bit<8> type; // 8 for request
    bit<8> code;         
    bit<16> checksum;    
    bit<16> id;          
    bit<16> seq;         
}

header udp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<16> length_;
    bit<16> checksum;
}

// header http_t {
//     bit<8> method; // GET, POST, etc.
//     bit<32> url;
// }

struct main_metadata_t {
    bit<16> proto;
//----------------------------- tcp flow id    
    bit<16> flow_id0;
    bit<16> flow_id1;
    bit<16> flow_id2;
    bit<16> flow_id3;
//----------------------------- icmp flow id    
    bit<16> flow_icmp_id0;
    bit<16> flow_icmp_id1;
    bit<16> flow_icmp_id2;
    bit<16> flow_icmp_id3;
//-----------------------------HH
    bit<20> count_0;
    bit<20> count_1;
    bit<20> count_2;
    bit<20> count_3;
    bit<20> minimum;    
    bit<20> dif;
//-----------------------------SYN
    bit<7> syn_drop_percent;
    bit<32> syn_counts;
    bit<7> syn_percent_iterator;
//-----------------------------SYN-ACK
    bit<7> synack_drop_percent;
    bit<32> synack_counts;
    bit<7> synack_percent_iterator;
//-----------------------------ACK
    bit<7> ack_drop_percent;
    bit<32> ack_counts;
    bit<7> ack_percent_iterator;
//-----------------------------FIN-RST
    bit<1> add;
//-----------------------------ICMP-REQ
    bit<20> count_icmp_0;
    bit<20> count_icmp_1;
    bit<20> count_icmp_2;
    bit<20> count_icmp_3;
    bit<20> minimum_icmp;    
    bit<20> dif_icmp;
//-----------------------------UDP
    bit<7> udp_drop_percent;
    bit<32> udp_counts;
    bit<7> udp_percent_iterator;

    bit<16> index_sketch0;
    bit<16> index_sketch1;
    bit<16> index_sketch2;

    bit<1> value_sketch0;
    bit<1> value_sketch1;
    bit<1> value_sketch2;

    // bit<1> new_flow;
    bit<2> state_ts;
    bit<32> timestamp1;
    bit<32> timestamp2;
    bit<32> timestamp3;
}

struct headers_t {
    ethernet_t ethernet;
    ipv4_t ipv4;
    tcp_t tcp;
    icmp_t icmp;
    udp_t udp;
}