#!/usr/bin/env python

import os
import pprint
import subprocess
from plumbum import local
from collections import defaultdict

#function to import variable from config.sh
def import_config()
#TODO

#dictionary to store patric ids mapped to ncbi taxa ids (needed)
patric_to_taxa={}

#dictionary to store ids to name (may not use)
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


