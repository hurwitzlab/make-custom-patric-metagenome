#!/usr/bin/env python

"""
What has to be done...

"""
import argparse
import os
import pprint
import subprocess
from plumbum import local
from Bio import SeqIO

#function to import variable from config.sh or other sourcefile
def import_config(sourcefile='./config.sh'):
    command = ['bash', '-c', 'source ' + sourcefile + ' && env']
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)
    for line in proc.stdout:
        (key, _, value) = line.partition("=")
        os.environ[key] = value.rstrip('\n')
    proc.communicate()

#don't need to import environment because it should already be set
#from calling shell script
#import_config()

if __name__ == "__main__":
    parser = \
    argparse.ArgumentParser(description="Script to fix taxonomy text files.")
    parser.add_argument("-m", "--map", action="store", \
        help="File in",default=os.environ.get('SOURCE_MAP'))
    parser.add_argument("-o1", "--out1", action="store", \
        help="File out",default=''.join([os.environ.get('OUT_DIR'),\
        '/',os.environ.get('OUT_NAME1')]))
    parser.add_argument("-o2", "--out2", action="store", \
        help="Annotation out", default=''.join([os.environ.get('OUT_DIR'),\
        '/',os.environ.get('OUT_NAME2')))

    args = vars(parser.parse_args())

file_in = open(args["map"],"r")
file_out1 = open(args["out1"],"w")
file_out2 = open(args["out2"],"w")

strain_to_accn={}

for line in file_in:
    line=line.rstrip('\n')
    cols=line.split(' ')
    accn=cols[0]
    strain=cols[1]
    #this adds in the accn's as a list if there are more than one
    strain_to_accn.setdefault(strain,[])
    strain_to_accn[strain].append(accn)

for strain in strain_to_accn:
    print 'Getting genome accns for {}'.format(strain)
    if not os.path.isfile(''.join([os.environ.get('PATRIC_GENOMES'),'/',\
            strain,'.fna'])):
        print '{}.fna does not exist'.format(strain)
        continue
    record_dict = SeqIO.index(''.join([os.environ.get('PATRIC_GENOMES'),'/',\
            strain,'.fna']),'fasta')
    if type(strain_to_accn[strain])==list:
        number_written = 0
        for accn in strain_to_accn[strain]:
            #SeqIO.write returns the number of records written
            #and in python also executes the code!
            #Note the SeqIO.write adds in /n to make the fasta record
            #more readable, if we want raw records we have to use
            #record_dict.get_raw(accn) and can't use SeqIO.write
            number_written += SeqIO.write(record_dict[accn],file_out,'fasta')
    else:
        SeqIO.write(record_dict[accn],file_out,'fasta')
        print 'Wrote 1 record to {}'.format(strain)
    
    print 'Number of records written to {} = {}'.format(strain,\
            number_written)

    record_dict.close()

    print "Getting annotation for strain {}".format(strain) 

    annot_path = ''.join([os.environ.get('PATRIC_ANNOT'),'/',\
            strain,'.PATRIC.cds.tab'])

    if not os.path.isfile(annot_path):
        print '{}.PATRIC.cds.tab does not exist'.format(strain)
        continue
    
    annot_file = open(annot_path,"r")

    for line in annot_file:
        line=line.rstrip('\n')
        cols=line.split(' ')




file_in.close()
file_out1.close()
file_out2.close()
