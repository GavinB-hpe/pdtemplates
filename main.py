#!/usr/bin/env python3
import argparse
from logparser.Drain import LogParser

INPUTFILE  = "fortemplating.txt"
INDIR      = "."
OUTDIR     = "."
SIMILARITY = 0.5
DEPTH      = 4
log_format = '<Content>'
# regex = [ r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)' ]
regex = [r'\[#[0-9]+\]', 
         r'Critical Alert:',
         r'Domain Name :',
         r'HPE INC Number',
         r'Issue Description']

def main():
    argp = argparse.ArgumentParser(prog='pdtemplates',
                                   description="Analyses event summaries and produces stats on log types")
    argp.add_argument("-f", "--filename", default=INPUTFILE, help="Name of input text file with a summary per line")    
    argp.add_argument("-d", "--depth", default=DEPTH, help=f"Depth param for tree algorithm. Default {DEPTH}")    
    argp.add_argument("-s", "--similarity", default=SIMILARITY, help=f"Similarity param for tree algorithm. Default {SIMILARITY}")    
    args = argp.parse_args()
    depth = int(args.depth)
    st = float(args.similarity)
    parser = LogParser(log_format, indir=INDIR, outdir=OUTDIR, depth=depth, st=st, rex=regex)
    parser.parse(args.filename)

main()

