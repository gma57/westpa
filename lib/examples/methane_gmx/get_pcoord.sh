#!/bin/bash

if [ -n "$SEG_DEBUG" ] ; then
    set -x
    env | sort
fi

cd $WEMD_SIM_ROOT

TPR=methane.tpr
TOP=methane.top
NDX=methane.ndx
OUT=_dist_$$.xvg

function cleanup() {
    rm -f $OUT
}

trap cleanup EXIT

# Get progress coordinate
echo "7 8" | g_dist -f $WEMD_STRUCT_DATA_REF -s $TPR -n $NDX -o $OUT -xvg none || exit 1
awk '{print $2*10;}' < $OUT > $WEMD_PCOORD_RETURN || exit 1

if [ -n "$SEG_DEBUG" ] ; then
    head -v $WEMD_PCOORD_RETURN
fi


