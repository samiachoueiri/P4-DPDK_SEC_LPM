control ACTIONS(
    inout headers_t       hdr,
    inout main_metadata_t meta)
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

    apply {
        }

}