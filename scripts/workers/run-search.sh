#!/usr/bin/env bash

#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l jobtype=cluster_only
#PBS -l select=1:ncpus=2:mem=3gb:pcmem=2gb
#PBS -l pvmem=6gb
#PBS -l walltime=24:10:00
#PBS -l cput=24:10:00
#PBS -M scottdaniel@email.arizona.edu
#PBS -m bea

cd $PBS_O_WORKDIR

COMMON="$WORKER_DIR/common.sh"

if [ -e $COMMON ]; then
  . "$COMMON"
else
  echo Missing common \"$COMMON\"
  exit 1
fi

TMP_FILE=$(mktemp)

get_lines $SOURCE_MAP $TMP_FILE $PBS_ARRAY_INDEX $STEP_SIZE

NUM_FILES=$(lc $TMP_FILE)

echo Found \"$NUM_FILES\" files to process

echo Running python script

export PBS_ARRAY_INDEX

export OUT_DIR="$DATA_DIR/contig-out/$PBS_ARRAY_INDEX"

NUM_GENOMES=$(cut -f2 -d' ' $TMP_FILE | sort -u | lc)

if [ -d $OUT_DIR ]; then
    rm -rf $OUT_DIR/*
else
    init_dir "$OUT_DIR"
fi

export OUT_NAME1="$NUM_GENOMES-strains.fa"
export OUT_NAME2="$NUM_GENOMES-annotation.tab"

python $WORKER_DIR/get-contigs.py -m $TMP_FILE \
    -o1 $OUT_DIR/$OUT_NAME1 \
    -o2 $OUT_DIR/$OUT_NAME2
