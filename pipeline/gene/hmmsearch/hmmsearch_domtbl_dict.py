import pickle
import os
import argparse
"""
Parse hmmsearch domain table output
and output the dictionary as a pickle binary.
-------------------------------------------------------------------------------
Ian Rambo
Last updated: 2018-12-11
Thirteen... that's a mighty unlucky number... for somebody!
"""
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, dest='input_file', action='store',
help='input hmmsearch domain results. Required.')
parser.add_argument('--output', type=str, dest='output_file', action='store',
help='output pickle binary. Required.')
opts = parser.parse_args()
#------------------------------------------------------------------------------
def parse_domtbl(domtbl):
    """
    Parse a hmmsearch domain table output.
    Returns a nested dictionary.
    """
    hit_dict = {}
    with open(domtbl, 'r') as dtblhit:
        for hit in dtblhit:
            hit = hit.rstrip()
            hit_fields = hit.split()
            target_id = hit_fields[0]
            hmmname = hit_fields[3]
            if hmmname in hit_dict:
                if not target_id in hit_dict[hmmname]:
                    hit_dict[hmmname]['target_ids'].append(target_id)
                else:
                    pass
            else:
                hit_dict[hmmname] = {'target_ids':[target_id]}
    return hit_dict
#------------------------------------------------------------------------------
def pickle_dump(pickle_out, object):
    """
    Save a pickle object.
    """
    pickle.dump( object, open( pickle_out, 'wb' ) )
    return None
#------------------------------------------------------------------------------
if not os.stat(opts.input_file).st_size == 0:
    domtbl_dict = parse_domtbl(opts.input_file)
    pickle_dump(pickle_out = opts.output_file, object = domtbl_dict)
else:
    pass
