#!/usr/bin/python3

import sys
import math

if len(sys.argv) != 3:
  sys.exit("USAGE: " + sys.argv[0] + " INFILE NUM")

INFILE=sys.argv[1]
NUM=int(sys.argv[2])

with open(INFILE, "r") as hdlr:
  arr=hdlr.read().splitlines()
  unit=math.ceil((len(arr) / NUM))
  for idx,line in enumerate(arr):
    if idx%unit == 0:
      print("-------------------------------")
    print(line)
