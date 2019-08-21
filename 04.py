#!/usr/bin/python3

s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one=[1, 5, 6, 7, 8, 9, 15, 16, 19]
wlen=[]
for i in range(1, 21):
  if i in one:
    wlen.append(1)
  else:
    wlen.append(2)

ret={}
for idx, w in enumerate(s.split()):
  ret[w[0:wlen[idx]]]=idx+1

print(ret)
