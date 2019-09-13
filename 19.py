#!/usr/bin/python3

# cut -f1 data/hightemp.txt | sort | uniq -c | sort -r

import sys
import math
import pandas as pd

if len(sys.argv) != 2:
  sys.exit("USAGE: " + sys.argv[0] + " INFILE")

INFILE=sys.argv[1]

with open(INFILE, "r") as hdlr:
  arr=hdlr.read().splitlines()
  df=pd.DataFrame(list(map(lambda x: x.split(), arr)))
  print(df.groupby(0).count().sort_values(by=2, ascending=False)[[1]])
