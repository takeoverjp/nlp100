#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
  sys.exit("USAGE: " + sys.argv[0] + " INFILE TAIL")

INFILE=sys.argv[1]
TAIL=int(sys.argv[2])

with open(INFILE, "r") as hdlr:
  arr=hdlr.read().splitlines()
  for line in arr[-TAIL:]:
    print(line)
