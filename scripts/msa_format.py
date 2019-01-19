#!/usr/bin/python3
from Bio import AlignIO
import argparse
"""
Convert between multiple sequence alignment formats.
"""
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, dest='input_file', action='store',
help='input MSA. Required.')
parser.add_argument('--output', type=str, dest='output_file', action='store',
help='output MSA. Required.')
parser.add_argument('--infmt', type=str, dest='infmt', action='store',
help="""input MSA format. Required. Valid formats: clustal, emboss, fasta, fasta-m10, ig,
maf, mauve, nexus, phylip, phylip-sequential, phylip-relaxed, stockholm""")
parser.add_argument('--outfmt', type=str, dest='outfmt', action='store',
help="""output MSA format. Required. Valid formats: clustal, emboss, fasta, fasta-m10, ig,
maf, mauve, nexus, phylip, phylip-sequential, phylip-relaxed, stockholm""")
#------------------------------------------------------------------------------
opts = parser.parse_args()

input_handle = open(opts.input_file, 'r')
output_handle = open(str(opts.output_file), 'w')

alignment = AlignIO.parse(input_handle, opts.infmt)
AlignIO.write(alignment, output_handle, opts.outfmt)

input_handle.close()
output_handle.close()
