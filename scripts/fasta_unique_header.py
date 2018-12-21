#!/usr/bin/python3.5

import argparse
import re
"""
Remove illegal characters from FASTA headers and add a label
to make headers unique.
"""
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, dest='input_file', action='store',
help='input FASTA. Required. Can be piped from stdin using -')
parser.add_argument('--output', type=str, dest='output_file', action='store',
help='output FASTA. Required.')
opts = parser.parse_args()

illegals = re.compile(r'\:|\,|\)|\(|\;|\,|\]|\[|\,|\'')
header_counts = {}

with open(opts.input_file, 'r') as inseqs, open(opts.output_file, 'w') as outseqs:
    for f in inseqs:
        f = f.rstrip()
        if f.startswith('>'):
            f_legal = illegals.sub('_', f)
            if f in header_counts:
                header_counts[f] += 1
                outseqs.write('%s_%d\n' % (f_legal, header_counts[f]))
            else:
                header_counts[f] = 0
                outseqs.write('%s\n' % f_legal)
        else:
            outseqs.write('%s\n' % f)
