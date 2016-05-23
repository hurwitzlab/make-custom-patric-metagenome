export CWD=$PWD
export SCRIPT_DIR=$CWD

export PRJ_DIR="/Users/Scott/make-custom-patric-metagenome"
#where the worker scripts are (PBS batch scripts and their python/perl workdogs)
export WORKER_DIR="$PRJ_DIR/scripts/workers"
#where patric genomes are
export PATRIC_GENOMES="$PRJ_DIR/genomes"
#patric genome index in case you want to go back to original scaffold from the read id
export PATRIC_INDEX="$PRJ_DIR/PATRIC_final_genome_index.txt"
#where patric annotation is
export PATRIC_ANNOT="$PRJ_DIR/annotation"
#place to put output
export DATA_DIR="$PRJ_DIR/data"
#source file with patric accn's (first field) [space] and patric strain/genome number (second field)
export SOURCE_MAP="$DATA_DIR/just-strain-and-accn-right-list.txt"


# --------------------------------------------------
function init_dir {
    for dir in $*; do
        if [ -d "$dir" ]; then
            rm -rf $dir/*
        else
            mkdir -p "$dir"
        fi
    done
}

# --------------------------------------------------
function lc() {
    wc -l $1 | cut -d ' ' -f 1
}
