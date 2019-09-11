#!/usr/bin/python3

import sys
import math

if len(sys.argv) != 2:
  sys.exit("USAGE: " + sys.argv[0] + " INFILE")

INFILE=sys.argv[1]

with open(INFILE, "r") as hdlr:
  arr=hdlr.read().splitlines()
  col1=map(lambda x: x.split()[0], arr)
  print(list(set(col1)))
