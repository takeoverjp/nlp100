#!/usr/bin/python3

s="パタトクカシーー"
ret=""
for idx, c in enumerate(s):
  if idx % 2 == 1:
    ret+=c
print(ret)
