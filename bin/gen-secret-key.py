from __future__ import print_function

import os
import sys

from django.utils.crypto import get_random_string
from os.path import abspath, dirname, exists, join, pardir, relpath
import argparse

SECRET_FILE_NAME = 'SECRET.key'
CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

DEFAULT_OUTPUT_DIR = join(dirname(abspath(__file__)), pardir, 'run')
DEFAULT_KEY_LEN = 50

# ----------------------------
# main
# ----------------------------
if __name__ == '''__main__''':
    #
    # setup input arguments
    #
    parser = argparse.ArgumentParser(description='Generate a new secret file for a django application',
                                     conflict_handler='resolve',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--output-dir', dest='outdir', default=DEFAULT_OUTPUT_DIR, 
                        help='''output directory from which settings.prd will read '%s' file, must exist. \ndefaults to 'run' ''' 
                             % (SECRET_FILE_NAME))
    parser.add_argument('--length', default=DEFAULT_KEY_LEN, type=int,
                        help='''secret key length, defaults to %s''' % DEFAULT_KEY_LEN)

    # optional arguments
    args = parser.parse_args()
    if not exists(args.outdir):
        parser.error('''Output directory %s does not exist'''%args.outdir)
    
    
    key =  get_random_string(args.length, CHARACTER_SET)    
    outfile = join(args.outdir, SECRET_FILE_NAME)
    with open(outfile, 'w') as fout:
        fout.write(key)    
    print ( '''\nsecret key written to %s \n''' %outfile )
    