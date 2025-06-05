#!/usr/bin/bash
dpdk_version=21.05
pktgen_version=21.05.0
DPDK_VER=$dpdk_version
PKTGEN_VER=$pktgen_version
export RTE_TARGET=x86_64-native-linuxapp-gcc
export RTE_SDK=$PWD/dpdk-$DPDK_VER

echo DPDK_VER=${DPDK_VER}
echo PKTGEN_VER=${PKTGEN_VER}
echo RTE_SDK=${RTE_SDK}

# downloading and unpacking DPDK
if [ ! -d $RTE_SDK ]; then
  if [ ! -e dpdk-$DPDK_VER.tar.xz ]; then
    wget -q https://fast.dpdk.org/rel/dpdk-$DPDK_VER.tar.xz 
  fi
  tar xf dpdk-$DPDK_VER.tar.xz
fi

echo =========================================================================
echo build and install DPDK ...
echo =========================================================================
cd $RTE_SDK
meson build
ninja -C build
sudo ninja -C build install
cd ..

if [ ! -d pktgen-$PKTGEN_VER ]; then
  echo =========================================================================
  echo download and unpack pktgen
  echo =========================================================================
  if [ ! -e pktgen-$PKTGEN_VER.tar.gz ]; then
    wget -q https://dpdk.org/browse/apps/pktgen-dpdk/snapshot/pktgen-$PKTGEN_VER.tar.gz
  fi
  tar xf pktgen-$PKTGEN_VER.tar.gz
fi

echo =========================================================================
echo building pktgen ...
echo =========================================================================

cd pktgen-$PKTGEN_VER 
tools/pktgen-build.sh clean
tools/pktgen-build.sh buildlua