#!/usr/bin/python3
"""
Ian Rambo
Functions to get the best hits from tabular output of HMMER and BLAST+
"""
#import argparse
import pandas as pd
import os
from warnings import warn
#------------------------------------------------------------------------------
def domtbl_besthits(target, source, env):
    """
    Get the best hit for each target AA sequence from HMMER domain
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
    dom_agg = domtbl.groupby(['target_name'], as_index = False).agg(aggregations)

    dom_agg.to_csv(target, sep = '\t', encoding='utf-8', header = True, index = False)

    return None
#------------------------------------------------------------------------------
def domtbl_fetch_sequences(targets, sources, env):
    """
    Extract sequences for hits in HMMER domain table output.
    Writes FASTA files to the tmp directory - these will be passed
    to jackhmmer for iterative searches.
    $SOURCES are:
    0. HMMER domain besthit table.
    1. the amino acid FASTA passed to HMMER.
    $TARGETS are the output FASTA files.
    """
    from Bio import SeqIO
    try:
        domtbl = pd.read_csv(sources[0], comment='#', header=None,
        names = ['query_alignment_name','target_name','target_accession',
        'target_len','query_name','accession','query_length','evalue_sequence',
        'bitscore_sequence','bias','domain_number','n_domains','evalue_conditional',
        'evalue_independ','bitscore_domain','bias_domain','hmm_from','hmm_to',
        'ali_from','ali_to','env_from','env_to','acc','target_desc'], sep = '\s+')

        query_names = domtbl['query_alignment_name'].tolist()

        seqfile_targets = [os.path.join(os.path.abspath('../tmp'), '%s_%s.faa' % (pipeline_env['FASTAID'], qname)) for qname in query_names]

        seq_dict = SeqIO.to_dict(SeqIO.parse(sources[1]), 'fasta')

        for seqfile in seqfile_targets:
            env.DEFAULT_TARGETS.append(seqfile)
            with open(seqfile, 'w') as sf:
                seq_objs = [seq_dict[v] for v in target_names]
                SeqIO.write(seq_objs, sf, 'fasta')
    except:
        warn('Input domain table is empty')

    return None
#------------------------------------------------------------------------------
def blast_besthits(target, source, env):
    """
    Get the best hit(s) from BLAST+ output and write to tab delimited output.
    The best hit is based on:
    1. evalue
    2. bitscore
    3. alignment length
    4. percent identity
    """
    from PROGRAM_OPTIONS import blast_outfmt
    blast = pd.read_csv(source, names = blast_outfmt.split()[1:], comment = '#',
    header = None, sep = '\s+')

    aggregations = {'qseqid':'first', 'evalue':min, 'bitscore':max, 'length':max, 'pident':max}

    blast_agg = blast.groupby(['qseqid'], as_index = False).agg(aggregations)
    blast_agg.to_csv(target, sep = '\t', encoding='utf-8', header = True, index = False)

    return None
#------------------------------------------------------------------------------
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', type=str, dest='input_file', action='store',
# help='input hmmer domain table results.')
# parser.add_argument('--output', type=str, dest='output_file', action='store',
# help='best hits for domain table results.')
# opts = parser.parse_args()
# #------------------------------------------------------------------------------
# domtbl_besthits(target = opts.output_file, source = opts.input_file)
