#!/usr/bin/python3
"""
Ian Rambo
Functions for pairwise and multiple sequence alignments.
"""

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
