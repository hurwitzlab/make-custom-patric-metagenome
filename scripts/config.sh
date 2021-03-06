export CWD=$PWD
export SCRIPT_DIR=$CWD
##where programs are
export BIN_DIR="/rsgrps/bhurwitz/hurwitzlab/bin"
#root project dir
export PRJ_DIR="/rsgrps/bhurwitz/scottdaniel/make-custom-patric-metagenome"
#
##input fasta
#export FASTA_DIR="/rsgrps/bhurwitz/kyclark/mouse/data/screened"
##where original clipped fastq's are, we will use the screened fasta's to search
##for the fastq's
#export CLIPPED_FASTQ="$PRJ_DIR/clipped"
##place for the resultant fastq's
#export FILTERED_FQ="$PRJ_DIR/filtered_fastq"
##place for sorted and merged PE'd reads and orphaned single reads
#export SORTNMG_DIR="$PRJ_DIR/sort-and-merged"
#
##place that original fastq's are
#export FASTQ_DIR="/rsgrps/bhurwitz/hurwitzlab/data/raw/Doetschman_20111007/all"
##place to store split up fastq's for searching later
#export SPLIT_FQ_DIR="$PRJ_DIR/split-fastq"
##place to store taxoner results (step 01)
#export TAXONER_OUT_DIR="$PRJ_DIR/taxoner-out"

#place where Taxonomy.txts are (which have our reads mapped to uniue_ids
export KRONA_OUT_DIR="/rsgrps/bhurwitz/scottdaniel/fastq-taxoner-patric/krona-out"
##place to store taxon counts (step 03)
##export COUNT_OUT_DIR="$PRJ_DIR/count-out"
#export COUNT_OUT_DIR="$PRJ_DIR/count-out"
##place to store goodly mapped reads
#export HIGH_QUAL_DIR="$PRJ_DIR/hq-out"
##place to store list of not-mapped that will be shunted to an assembler (opt-step)
#export READ_OUT_DIR="$PRJ_DIR/unk-out"
##place to store sequences of poorly mapped that will be assembled (opt-step)
#export LOW_QUAL_DIR="$PRJ_DIR/lq-out"
##place to store concatenated sequences from READ_OUT and LOW_QUAL
#export CAT_OUT_DIR="$PRJ_DIR/for-upload"
#where the worker scripts are (PBS batch scripts and their python/perl workdogs)
export WORKER_DIR="$PRJ_DIR/scripts/workers"
##how much to split up fasta files
#export FA_SPLIT_FILE_SIZE=500000 # in KB
##where bowtie2 database is for taxoner
#export BOWTIEDB="/rsgrps/bhurwitz/hurwitzlab/data/reference/taxoner_db"
#where patric genomes are
export PATRIC_GENOMES="/rsgrps/bhurwitz/hurwitzlab/data/reference/patric_bacteria"
#where taxid annotation is
export TAXA="/rsgrps/bhurwitz/scottdaniel/PATRIC_dbCreator/data/Patric_nodes.dmp"
#patric genome index in case you want to go back to original scaffold from the read id
export PATRIC_INDEX="/rsgrps/bhurwitz/hurwitzlab/data/reference/patric_metadata/PATRIC_final_genome_index.txt"
#where patric annotation is
export PATRIC_ANNOT="/rsgrps/bhurwitz/hurwitzlab/data/reference/patric_annot/patric_cds"
#data directory for output
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
