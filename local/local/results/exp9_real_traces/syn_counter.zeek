module project;

export {
    redef enum Log::ID += { syn_LOG };
    # type icmp_record_: record {
    #     counter: count &log;
    # };

    type syn_record_: record {
        counter: count &log;
    };
}

# global icmp_request_counter = 0;
# global icmp_threshold = 1000;
# global icmp_record: icmp_record_;

global syn_request_counter = 0;
global syn_record: syn_record_;

# event flood_checker() {
#     if (icmp_request_counter > icmp_threshold) {
#         icmp_record$counter = icmp_request_counter;
#         icmp_record$msg = fmt("ICMP flood detected");
#         Log::write(project::syn_LOG, icmp_record);
#         # print fmt("Flood detected with %s icmp packets", icmp_request_counter);
#     }

#     icmp_request_counter = 0;
#     schedule 1 secs { flood_checker() };
# }

event syn_count_logger() {
    syn_record$counter = syn_request_counter;
    Log::write(project::syn_LOG, syn_record);

    syn_request_counter = 0;
    schedule 1 secs { syn_count_logger() };
}

event zeek_init() {
    print("Zeek starts here");

    Log::create_stream(project::syn_LOG, [$columns=syn_record_]);
    local f = Log::get_filter(project::syn_LOG, "default");
    f$path = "night";
    Log::add_filter(project::syn_LOG, f);

    event syn_count_logger();
}

# event icmp_echo_request(c: connection, info: icmp_info, id: count, seq: count, payload: string) {
#     icmp_request_counter += 1;
# }

event connection_SYN_packet(c: connection, pkt:SYN_packet) {
    syn_request_counter += 1;
}

event zeek_done() {
    print("Zeek ends here");
}
