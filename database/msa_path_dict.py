# import pickle
# import os
# import re
# import warnings
# import argparse
"""
I AM HAVING ISSUES INTEGRATING THIS SCRIPT INTO AN SCONS COMMAND. NO IDEA WHY...
THE SCRIPT ALONE IS NOT WORKING. 
"""
# #------------------------------------------------------------------------------
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', type=str, dest='input_file', action='store',
# help='input database table file. Required.')
# parser.add_argument('--output', type=str, dest='output_file', action='store',
# help='output pickle binary. Required.')
# parser.add_argument('--search_dir', type=str, dest='search_dirs', action='store',
# help='source file directory to search. Required.')
# parser.add_argument('--extension', type=str, dest='extension', action='store',
# help='extension of files to find.')
#
# opts = parser.parse_args()
# #------------------------------------------------------------------------------
# ###---Functions.
# def find_re(pattern, path):
#     '''
#     Find files using a regular expression.
#     '''
#     result = []
#     for root, dirs, files in os.walk(path):
#         for name in files:
#             if re.match(pattern, name):
#                 result.append(os.path.join(root, name))
#     return result
# #------------------------------------------------------------------------------
# def build_path_dict(file_table, search_dirs, ext):
#     '''
#     Return a dictionary with paths for corresponding files
#     (e.g. HMM profiles from several databases for the same protein)
#     '''
#     path_dict = {}
#     with open(file_table, 'r') as ftbl:
#         ftbl.readline()
#         for c in ftbl:
#             cList = c.split('\t')
#             cdd = cList[0]
#             pfam = cList[1]
#             tigr = cList[2]
#             cog = cList[3]
#             function = cList[4]
#             gene = cList[5]
#             group = cList[6]
#             subtype = cList[7]
#             subtype = subtype.replace(',', '_')
#             id = '--'.join([gene, subtype, cdd])
#             dbPathList = []
#             for db in [cdd, pfam, tigr, cog]:
#                 if db != 'NA':
#                     db_pattern = r'%s\.%s|%s\.%s' % (db, ext.lower(), db, ext.upper())
#                     dbPath = [find_re(db_pattern, s) for s in search_dirs]
#                     print(dbPath)
#                     if dbPath:
#                         dbPathList.extend(dbPath)
#                     else:
#                         warn_message = 'file %s not found' % db
#                         warnings.warn(warn_message)
#                 else:
#                     pass
#             if dbPathList:
#                 print(dbPathList)
#                 path_dict[id] = dbPathList
#             else:
#                 pass
#     return path_dict
# #------------------------------------------------------------------------------
# def pickle_dump(pickle_out, object):
#     '''
#     Save a pickle object.
#     '''
#     pickle.dump( object, open( pickle_out, 'wb' ) )
#     return None
# #------------------------------------------------------------------------------
# path_dict = build_path_dict(file_table = opts.input_file,
# search_dirs = opts.search_dirs, ext = opts.extension)
#
# pickle_dump(pickle_out = opts.output_file, object = path_dict)
