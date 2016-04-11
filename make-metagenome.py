#!/usr/bin/env python

import os
import pprint
import subprocess
from plumbum import local
from collections import defaultdict

patric_to_taxa={}
patric_to_name={}
infile = open('tax_ids_to_lineage_ids.txt','r')
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

