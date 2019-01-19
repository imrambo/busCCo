#!/usr/bin/python3
import sys
import os

"""
Format HMMER domtbl hits from grep output - add the profile file name
from grep output as accession.
"""
for i in sys.stdin:
    i = i.rstrip()
    iList = i.split(':')
    profile_id = os.path.splitext(os.path.basename(iList[0]))[0]

    out = ' '.join(iList[1][:3] + [profile_id] + iList[1][5:])
    sys.stdout.write('%s\n' % out)
    #sys.stdout.write('%s %s\n' % (profile_id, iList[1]))
    sys.stdout.flush()
