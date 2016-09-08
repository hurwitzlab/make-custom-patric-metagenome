#!/usr/bin/env bash

#
#This script is intended to grab those muy importante contigs
#
unset module
set -u
source ./config.sh
export CWD="$PWD"
export STEP_SIZE=2000
#lines of just-genome-and-accn.txt = 156975
#divide by 2000 and you get ~78 subjobs

echo Setting up log files...
PROG=`basename $0 ".sh"`
#Just going to put stdout and stderr together into stdout
export STDOUT_DIR="$CWD/out/$PROG"

init_dir "$STDOUT_DIR"

if [ -e $SOURCE_MAP ]; then
    echo "mapping file $SOURCE_MAP exists, assuming it's fine"
else
    echo "no $SOURCE_MAP or bad file, exiting..."
    exit 12345
fi

export NUM_SEARCHES=$(lc $SOURCE_MAP)

echo \"Processing $NUM_SEARCHES contigs\"

JOB=$(qsub -J 1-$NUM_SEARCHES:$STEP_SIZE -V -N fetch_dog -j oe -o "$STDOUT_DIR" $WORKER_DIR/run-search.sh)

if [ $? -eq 0 ]; then
  echo Submitted job \"$JOB\" for you. La la la. La. la.
else
  echo -e "\nError submitting job\n$JOB\n"
fi




