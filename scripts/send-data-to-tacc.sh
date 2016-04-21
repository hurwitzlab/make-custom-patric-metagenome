#!/usr/bin/env bash

#PBS -N sender
#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l jobtype=serial
#PBS -l select=1:ncpus=2:mem=3gb:pcmem=2gb
#PBS -l pvmem=6gb
#PBS -l walltime=6:00:00
#PBS -l cput=6:00:00
#PBS -M scottdaniel@email.arizona.edu

#cd $PBS_O_WORKDIR

while [ 1 ]; do
    rsync --timeout=60 -aivvzhP --rsh=ssh --exclude='data/patric_contigs.fa' ./* sdaniel@stampede.tacc.utexas.edu:/work/03859/sdaniel/custom_patric_genome/
    if [ "$?" = "0" ]; then
            echo "Rsync success!"
            exit 0
        else
            echo "Rsync failure. Retrying in a minute"
            sleep 60
    fi
done
