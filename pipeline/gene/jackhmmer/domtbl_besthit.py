#!/usr/bin/python3
import pandas as pd
import argparse
#------------------------------------------------------------------------------
def domtbl_besthits(target, source):
    """
    Get the best hit for each target AA sequence from jackhmmer domain
    table output. The best hit is based on:
    1. min independent e-value
    2. max bitscore
    3. max alignment length
    4. max mean posterior probability of aligned residues
    in the maximum expected accuracy alignment, i.e. reliability of overall
    alignment
    """
    domtbl = pd.read_csv(source, comment='#', header=None,
    names = ['query_alignment_name','target_name','target_accession',
    'target_len','query_name','accession','query_length','evalue_sequence',
    'bitscore_sequence','bias','domain_number','n_domains','evalue_conditional',
    'evalue_independ','bitscore_domain','bias_domain','hmm_from','hmm_to',
    'ali_from','ali_to','env_from','env_to','acc','target_desc'], sep = '\s+')

    domtbl['alignment_length'] = (domtbl['ali_to'] - domtbl['ali_from']).astype(int)

    aggregations = {'query_alignment_name':'first', 'evalue_independ':min, 'acc':max, 'bitscore_domain':max, 'alignment_length':max}
    dom_agg = domtbl.groupby(['target_name'], as_index=False).agg(aggregations)
    dom_agg.to_csv(target, sep='\t', encoding='utf-8', header = True, index = False)

    return None
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, dest='input_file', action='store',
help='input hmmer domain table results.')
parser.add_argument('--output', type=str, dest='output_file', action='store',
help='best hits for domain table results.')
opts = parser.parse_args()
#------------------------------------------------------------------------------
domtbl_besthits(target = opts.output_file, source = opts.input_file)
