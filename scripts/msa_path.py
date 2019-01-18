#!/usr/bin/python3
"""
Ian Rambo
Functions to search for MSA paths and build a dictionary of paths to use in
MSA and HMM building.
"""
import pickle
import os
import re
import warnings
#==============================================================================
def find_re(pattern, path):
    '''
    Find files using a regular expression.
    '''
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if re.match(pattern, name):
                result.append(os.path.join(root, name))
                #result.extend(os.path.join(root, name))
    return result
#------------------------------------------------------------------------------
def build_path_dict(file_table, search_dirs, ext):
    '''
    Return a dictionary with paths for corresponding files
    (e.g. HMM profiles from several databases for the same protein)
    '''
    path_dict = {}
    with open(file_table, 'r') as ftbl:
        ftbl.readline()
        for c in ftbl:
            cList = c.split('\t')
            cdd = cList[0]
            pfam = cList[1]
            tigr = cList[2]
            cog = cList[3]
            function = cList[4]
            gene = cList[5]
            group = cList[6]
            subtype = cList[7]
            subtype = subtype.replace(',', '_')
            id = '--'.join([gene, subtype, cdd])
            dbPathList = []
            for db in [cdd, pfam, tigr, cog]:
                if db != 'NA':
                    db_pattern = '%s\.%s|%s\.%s' % (db, ext.lower(), db, ext.upper())
                    dbPath = [find_re(db_pattern, s) for s in search_dirs]
                    if dbPath:
                        dbPathList.extend(dbPath)
                    else:
                        warn_message = 'file %s not found' % db
                        warnings.warn(warn_message)
            if dbPathList:
                #Flatten the list
                dbPathList = [item for sublist in dbPathList for item in sublist]
                path_dict[id] = dbPathList
            else:
                pass
    return path_dict
#------------------------------------------------------------------------------
def pickle_dump(pickle_out, object):
    '''
    Save a pickle object.
    '''
    pickle.dump( object, open( pickle_out, 'wb' ) )
    return None
