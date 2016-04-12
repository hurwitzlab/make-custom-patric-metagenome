#!/usr/bin/env python

#PBS -W group_list=bhurwitz
#PBS -q standard
#PBS -l jobtype=cluster_only
#PBS -l select=1:ncpus=6:mem=11gb
#PBS -l pvmem=22gb
#PBS -l place=pack:shared
#PBS -l walltime=24:00:00
#PBS -l cput=24:00:00
#PBS -M scottdaniel@email.arizona.edu
#PBS -m bea

import os
import pprint
import subprocess
from plumbum import local
from collections import defaultdict

#change directory to where script is launched (stupid PBS!!!)
local.cwd.chdir(os.environ.get('PBS_O_WORKDIR'))

#function to import variable from config.sh or other sourcefile
def import_config(sourcefile='config.sh'):
    command = ['bash', '-c', 'source ' + sourcefile + ' && env']
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)
    for line in proc.stdout:
        (key, _, value) = line.partition("=")
        os.environ[key] = value.rstrip('\n')
    proc.communicate()

#call the function
import_config()

#for testing
#pprint.pprint(dict(os.environ))

#dictionary to store patric ids mapped to ncbi taxa ids (needed)
patric_to_taxa={}

#dictionary to store ids to name (optionally use this)
patric_to_name={}

#file with list of ids
infile = open('tax_ids_to_lineage_ids.txt','r')

#final outfile
outfile = open('./data/patric_contigs.fa','w')

#infile should look like this
#genome_id (which is really patric_id) genome_name taxon_id
#592010.4    Abiotrophia defectiva ATCC 49176    592010
#509191.4    Acetivibrio cellulolyticus CD2  509191

for line in infile:
    if ('.' in line):
        line.rstrip('\n')
        patricid=line.split()[0]
        name=line.split()[1]
        taxid=line.split()[2]
        patric_to_taxa.update({patricid:taxid})
        patric_to_name.update({patricid:name})

#change dir to where genomes are
local.cwd.chdir(os.environ.get('PATRIC_DIR'))

#import find command using plumbum
find=local['find']

for patricid in patric_to_taxa:
    
    #find genome
    #NOTE: this will break if there are multiple matches
    print('Searching for '+patricid+'.fna')
    genome_name=find('./','-iname','*'+patricid+'*')
    genome_name=genome_name.rstrip('\n')

    #read into temporary file
    try:
        temp_genome = open(genome_name,'r')
    except IOError:
        print(patricid+'.fna not found')
        continue

    #write each line of file to the outfile
    for line in temp_genome:
        outfile.write(line)

    #close file
    temp_genome.close

#being a good memory citizen
infile.close()
outfile.close()
