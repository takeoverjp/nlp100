#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
  sys.exit("USAGE: " + sys.argv[0] + " COLUMN1 COLUMN2")

COLUMN1=sys.argv[1]
COLUMN2=sys.argv[2]

with open(COLUMN1, "r") as c1:
  with open(COLUMN2, "r") as c2:
    arr1=c1.read().splitlines()
    arr2=c2.read().splitlines()
    for idx,elem1 in enumerate(arr1):
      print(elem1 + "\t" + arr2[idx])
