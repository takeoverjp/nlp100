#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
  sys.exit("USAGE: " + sys.argv[0] + " DATA_FILE")

DATA_FILE=sys.argv[1]
col=[[],[],[],[]]

with open(sys.argv[1], "r") as f:
  for line in f.readlines():
    row=line.split()
    for i, elem in enumerate(row):
      col[i].append(elem)

for i, elem in enumerate(row):
  with open("col" + str(i+1) + ".txt", "w") as f:
    for elem in col[i]:
      f.write(elem + '\n')
