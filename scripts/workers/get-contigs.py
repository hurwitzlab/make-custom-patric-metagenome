#!/usr/bin/env python

"""
What has to be done...

"""
import os
import pprint
import subprocess
from plumbum import local
from collections import defaultdict

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
    parser.add_argument("-o", "--out", action="store", \
        help="File out",default=(os.environ.get('OUT_DIR') + \
        '/' + os.environ.get('OUT_NAME')))

    args = vars(parser.parse_args())

file_in = open(args["file"],"r")
file_out = open(args["out"],"w")

strain_to_accn={}

for line in file_in:
    line=line.rstrip('\n')
    cols=line.split(' ')
    accn=cols[0]
    strain=cols[1]
    #this adds in the accn's as a list if there are more than one
    strain_to_accn.setdefault(strain,[])
    strain_to_accn[strain].append(accn)


