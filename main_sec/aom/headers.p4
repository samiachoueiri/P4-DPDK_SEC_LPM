typedef bit<48> EthernetAddress;
typedef bit<32> IP4Address;  
const bit<16> TYPE_IPV4 = 0x0800;
const bit<8> TYPE_TCP = 0x6;

//-----------------------------SYN
// #define THRESH_SYN 1000000
// #define SYN_DROP_RATE 25
//-----------------------------FIN-RST
const ExpireTimeProfileId_t EXPIRE_TIME_PROFILE_ID = (ExpireTimeProfileId_t) 4;

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

struct main_metadata_t {
//-----------------------------SYN
    // bit<7> syn_drop_percent;
    // bit<32> syn_counts;
    // bit<7> syn_percent_iterator;
//-----------------------------FIN-RST
    bit<1> add;
}

struct headers_t {
    ethernet_t ethernet;
    ipv4_t ipv4;
    tcp_t tcp;
}