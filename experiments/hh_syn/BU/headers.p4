

//--------------------------------------------------------------------------------------- headers
typedef bit<48> EthernetAddress;
typedef bit<32> IP4Address;  
const bit<16> TYPE_IPV4 = 0x0800;
const bit<8> TYPE_TCP = 6;

#define SYN_DROP_RATE 50
#define THRESH_HH 100000
#define THRESH_SYN 1000000


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

// header tcp_t {
//     bit<16> srcPort;
//     bit<16> dstPort;
//     bit<32> seqNo;
//     bit<32> ackNo;
//     bit<4>  dataOffset;
//     bit<3>  res;
//     bit<3>  ecn;
//     bit<6>  ctrl;
//     bit<16> window;
//     bit<16> checksum;
//     bit<16> urgentPtr;
// }

header tcp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4>  dataOffset;
    bit<4>  res;
    bit<3>  ecn;
    bit<5>  flags;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr; 
}

struct main_metadata_t {
    bit<16> flow_id0;
    bit<16> flow_id1;
    bit<16> flow_id2;
    bit<16> flow_id3;
    bit<20> count_0;
    bit<20> count_1;
    bit<20> count_2;
    bit<20> count_3;
    bit<20> minimum;    
    bit<20> dif;
    bit<64> last_timestamp;
    bit<64> current_timestamp;
    bit<64> interarrival_value;

    bit<7> drop_percent;
    bit<32> syn_counts;
    bit<7> percent_iterator;   
}


struct headers_t {
    ethernet_t ethernet;
    ipv4_t ipv4;
    tcp_t tcp;
}

