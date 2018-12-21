#!/usr/bin/python3
"""
Options for command line tools.
"""
#==============================================================================
def optstring_join(optdict):
    """
    Join a dictionary of command line options into a single string.
    """
    optstring = ' '.join([str(param) + ' ' + str(val) for param, val in optdict.items()])
    return optstring
#==============================================================================
#Prodigal options
prodigal_opts = {'-i':'$SOURCE', '-p':'single', '-o':'${TARGETS[0]}',
'-a':'${TARGETS[1]}', '-f':'gff', '-q':''}
#==============================================================================
###---HMMER suite---###
#Hmmsearch options
hmmsearch_opts = {'--domE':10, '-E':10, '--incE':1e-6, '--incdomE':1e-6, '--seed':42}
#Jackhmmer options
jackhmmer_opts = {'--mx':'BLOSUM62', '-E':1e-20, '--domE':1e-20, '-N':20,
'--incE':1e-20, '--incdomE':1e-20, '--F1':0.01, '--seed':42, '--cpu':4,
'--noali':''}
#Hmmbuild options
hmmbuild_opts = {'--cpu':2, '--seed':42}
#==============================================================================
###---CRISPR array mining---###

#Min/Max lengths for CRISPR spacers and repeats
maxSpacerLen = 64
minSpacerLen = 8
maxRepeatLen = 72
minRepeatLen = 16
#------------------------------------------------------------------------------
#MinCED options
minced_opts = {'-searchWL':8, '-minNR':3, '-minRL':minRepeatLen,
'-maxRL':maxRepeatLen, '-minSL':minSpacerLen, '-maxSL':maxSpacerLen}
#------------------------------------------------------------------------------
#PILERCR options
pilercr_opts = {'-minrepeat':minRepeatLen, '-maxrepeat':maxRepeatLen,
'-minspacer':minSpacerLen, '-maxspacer':maxSpacerLen, '-mincons':0.80,
'-minid':0.80, '-minspacerratio':0.75}
#------------------------------------------------------------------------------
#MAFFT options
mafft_opts = {'--auto':'', '--anysymbol':'', 'maxiterate':1000}
#------------------------------------------------------------------------------
#MUSCLE profile-profile alignment options
muscle_pp_opts = {'-seqtype':'auto', '-profile':'', '-in1':'${SOURCES[0]}',
'-in2':'${SOURCES[1]}', '-out':'$TARGET'}
#==============================================================================
#RAxML options
raxml_opts = {'-s':'$SOURCE', '-K':'GTR', '-m':'PROTGAMMAAUTO',
'-T':'10', '-f':'a', '-N':'autoMRE', '-x':'7', '-p':'7'}
#==============================================================================
#BLAST+ output format string
blast_outfmt = '6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'
#BLASTN options
blastn_opts = {'-task':'blastn', '-db':'', '-query':'$SOURCE',
'-out':'$TARGET', '-evalue':1000, '-best_hit_overhang':0.1,
'-best_hit_score_edge':0.1, '-word_size':4, '-gapopen':5, '-gapextend':2,
'-penalty':'-3', '-reward':1, '-dust':'no', '-soft_masking':'false',
'-outfmt':'"%s"' % blast_outfmt}
