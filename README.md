# busCCo
BusCCo is a CRISPR-Cas mining pipeline designed for UNIX and Linux
operating systems. The pipeline accepts a nucleotide FASTA file
(https://en.wikipedia.org/wiki/FASTA_format). Currently, the pipeline
is being built for individual bacterial or archaeal genomes,
but will later be usable with metagenomic
read data.

It's in the development stage so don't try anything yet.

This pipeline is written in Python and utilizes SCons for reproducible builds and analyses.
#---------------------------------
Prerequisites
#---------------------------------
Install these dependencies first:
Python 3:
    pandas
    ggpy (not yet implemented)
    Biopython
SCons v3.0.1
Prodigal v2.x or higher
HMMER v3.1 or higher
MinCED
PilerCR
MUSCLE
MAFFT
RAxML v8.2X
#-----------------------------------
Usage
#-----------------------------------
The components of the pipeline include
Database and Pipeline builds.

The Database build will construct
profile Hidden Markov Models (HMMs) from
single multiple sequence alignments (MSA) or
several corresponding MSAs.

The Pipeline build mines the FASTA file
for Cas genes and CRISPR arrays, finds clusters,
and updates profile HMMs with newly discovered proteins.

The SConstruct files control the builds:
pipeline/SConstruct
database/SConstruct

To run, use:
scons --fasta=<file.fna>

#-----------------------------------
Authors
#-----------------------------------
Ian Rambo - The University of Texas at Austin Marine Science Institute

#-----------------------------------
Acknowledgements
#-----------------------------------
https://www.scons.org/
https://github.com/ctSkennerton/minced
http://eddylab.org/software/hmmer/hmmer.org
https://www.drive5.com/muscle/
https://www.drive5.com/pilercr/
https://github.com/hyattpd/Prodigal
