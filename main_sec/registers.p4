#ifndef _REGISTERS_
#define _REGISTERS_

    Register<bit<5>, bit<1>>(1) attack;

    Register<bit<2>, bit<1>>(1) reg_state_ts;
    Register<bit<32>, bit<1>>(1) reg_timestamp1;
    Register<bit<32>, bit<1>>(1) reg_timestamp2;
    Register<bit<32>, bit<1>>(1) reg_timestamp3;

#endif