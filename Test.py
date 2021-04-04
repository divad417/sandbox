#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import argcomplete
import argparse

def completer(**kwargs):
    return ['a', 'b', 'c']

parser = argparse.ArgumentParser()
parser.add_argument('test').completer = completer

argcomplete.autocomplete(parser)
args = parser.parse_args()

print(args.test)
