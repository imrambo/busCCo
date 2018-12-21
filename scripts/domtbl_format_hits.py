#!/usr/bin/python3.5
import sys
import os

"""
Format HMMER domtbl hits from grep output - add the file name
from grep output as the first column.
"""
for i in sys.stdin:
    i = i.rstrip()
    iList = i.split(':')
    profile_id = os.path.splitext(os.path.basename(iList[0]))[0]

    sys.stdout.write('%s %s\n' % (profile_id, iList[1]))
    sys.stdout.flush()
