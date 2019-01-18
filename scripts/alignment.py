#!/usr/bin/python3.5
"""
Ian Rambo
Functions for use with multiple sequence alignments.
"""
#------------------------------------------------------------------------------
def consensus_sequence(alignment, format):
    from Bio import AlignIO
    from Bio.Align import AlignInfo
    """
    Obtain a consensus sequence from a multiple sequence alignment.
    """
    ali = AlignIO.read(open(alignment), format)
    summary_align = AlignInfo.SummaryInfo(ali)
    consensus = summary_align.dumb_consensus()
    return consensus

#------------------------------------------------------------------------------
def msa_merge_table(target, sources, env):
    '''
    Create a merged MSA table for mafft --merge.
    e.g.
    1 2 3 #
    4 5 6 7 #
    8 9 10 #
    Sequences 1, 2, and 3 are aligned.
    $SOURCES is a list of MSA paths.
    '''
    with open(str(target[0]), 'w') as mt:
        nseq = 1
        for msa in source:
            msa = str(msa)
            with open(msa, 'r') as m:
                for i in m:
                    if i.startswith('>'):
                        mt.write('%d ' % nseq)
                        nseq += 1
                mt.write('#\n')
    return None
#------------------------------------------------------------------------------
