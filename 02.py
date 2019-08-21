#!/usr/bin/python3

s0="パトカー"
s1="タクシー"
ret=""
for idx, c in enumerate(s0):
  ret+=c+s1[idx]
print(ret)
