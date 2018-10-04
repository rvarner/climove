#!/usr/bin/env python

import glob
import sys
import os
import os.path
from tqdm import tqdm


def moveAll(globStr, dest):
    for g in tqdm(glob.glob(globStr), ):
        os.rename(g, os.path.join(dest, g))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage: move <globstr> <dest>"
        exit(1)

    globStr = sys.argv[1]
    dest = sys.argv[2]
    if not os.path.isdir(dest):
        print "error: dest directory does not exist: %s" % dest
        exit(1)

    moveAll(globStr, dest)
