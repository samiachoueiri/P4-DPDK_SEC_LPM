#include <core.p4>
#include <dpdk/pna.p4>

#include "headers.p4"
//--------------------------------------------------------------------------- attacks
#include "syn_flood.p4"
#include "syn_ack_flood.p4"
#include "ack_flood.p4"
#include "fin_flood.p4"
#include "heavy_hitter.p4"
#include "icmp_flood.p4"
#include "udp_flood.p4"
#include "get_tcp_flow.p4"
#include "get_icmp_flow.p4"
#include "registers.p4"
//---------------------------------------------------------------------------
#include "parser.p4"
#include "control.p4"
#include "deparser.p4"

PNA_NIC(
    MainParserImpl(),
    PreControlImpl(),
    MainControlImpl(),
    MainDeparserImpl()
    ) main;