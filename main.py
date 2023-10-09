#!/usr/bin/env python3
import argparse
import csv
import numpy as np
import pandas as pd

import plotly.express as px
from logparser.Drain import LogParser


INPUTFILE  = "fortemplating.txt"
INDIR      = "."
OUTDIR     = "."
SIMILARITY = 0.5
DEPTH      = 4
COLWIDTH   = 100
LENGTH     = 16
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
    argp.add_argument("-f", "--filename", default=INPUTFILE, help=f"Name of input text file with a summary per line. Default {INPUTFILE}")
    argp.add_argument("-d", "--depth", default=DEPTH, type=int, help=f"Depth param for tree algorithm. Default {DEPTH}")
    argp.add_argument("-s", "--similarity", default=SIMILARITY, type=float, help=f"Similarity param for tree algorithm. Default {SIMILARITY}")
    argp.add_argument("-w", "--width", default=COLWIDTH, type=int, help=f"Max column width. Default {COLWIDTH}")
    argp.add_argument("-l", "--length", default=LENGTH, type=int, help=f"Number of rows to show. 0 implies all rows. Default {LENGTH}")
    argp.add_argument("-p", "--plot", action='store_true', help="Show graph of results.")

    args = argp.parse_args()
    depth = int(args.depth)
    st = float(args.similarity)
    parser = LogParser(log_format, indir=INDIR, outdir=OUTDIR, depth=depth, st=st, rex=regex)
    parser.parse(args.filename)
    # parser dumps data as a CSV file, which is irritatnig as it needs to be read back in
    csvname = args.filename + "_templates.csv"
    results = []
    count = 0
    print(f"Resulting CSV file is {csvname}")
    pd.set_option('display.max_colwidth', args.width)
    df = pd.read_csv(csvname)
    df = df.sort_values(by=['Occurrences'], ascending=False)
    if args.length == 0 :
        with pd.option_context('display.max_rows', None):  
            print(df)
    else:
        print(df.head(args.length))
    if args.plot:
        fig = px.bar(df, x="EventId", y="Occurrences", title="Event Types") 
        fig.show()


main()

