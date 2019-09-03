#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
  sys.exit("USAGE: " + sys.argv[0] + " DATA_FILE")

DATA_FILE=sys.argv[1]

count=0
with open(sys.argv[1], "r") as f:
  for line in f.readlines():
    print(line.translate(str.maketrans('\t', ' ')), end='')
