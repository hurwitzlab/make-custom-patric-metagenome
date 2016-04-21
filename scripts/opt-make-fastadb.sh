#!/usr/bin/env bash

#
# This script is intended to make a BioSeqIO index from fasta files
#
unset module
set -u
source ./config.sh
export CWD="$PWD"
export STEP_SIZE=1000

PROG=`basename $0 ".sh"`
#Just going to put stdout and stderr together into stdout
STDOUT_DIR="$CWD/out/$PROG"

init_dir "$STDOUT_DIR"

cd "$PATRIC_GENOMES"

export FILES_LIST="$PRJ_DIR/makedb-files"

echo "Finding fasta's"

find . -type f -iname \*.fna | sed "s/^\.\///" > $FILES_LIST

echo "Checking if already processed"

if [ -e $PRJ_DIR/makedb-files-to-process ]; then
    rm $PRJ_DIR/makedb-files-to-process
fi

export FILES_TO_PROCESS="$PRJ_DIR/makedb-files-to-process"

#remove following line after first run
cp $FILES_LIST $FILES_TO_PROCESS

#uncomment following loop if after first run
#while read FASTA; do
#
#    find $PATRIC_GENOMES -iname \*.index | sed "s/^\.\///" > found-indexes
#
#    FINDTEST=$(egrep "$FASTA"\.index ./found-indexes)
#
#    if [[ -z $FINDTEST ]]; then
#        echo $FASTA >> $FILES_TO_PROCESS
#    else
#        continue
#    fi
#
#done < $FILES_LIST

NUM_FILES=$(lc $FILES_TO_PROCESS)

echo \"Found $NUM_FILES to process\"

JOB=$(qsub -J 1-$NUM_FILES:$STEP_SIZE -V -N makedbfasta -j oe -o "$STDOUT_DIR" $WORKER_DIR/make-fastaDB.sh)

if [ $? -eq 0 ]; then
  echo Submitted job \"$JOB\" for you in steps of \"$STEP_SIZE.\" Remember: Try to relax.
else
  echo -e "\nError submitting job\n$JOB\n"
fi
