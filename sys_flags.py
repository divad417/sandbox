#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Calculate traffic interaction hazard metrics.')
parser.add_argument('-t', '--test',
                    type=float,
                    help='Test input.')

args = parser.parse_args()

print(args.test)
