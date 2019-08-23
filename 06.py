#!/usr/bin/python3
import math
import functools

s="I am an NLPer"
s1="paraparaparadise"
s2="paragraph"


def cngram(s, n):
  ret=[]
  for i in range(math.ceil((len(s)/n))):
    ret.append(s[i*n:((i+1)*n)])
  return ret

def wngram(s, n):
  warray=s.split()
  ret=[]
  for i in range(math.ceil((len(warray)/n))):
    ret.append(functools.reduce(lambda x, y: x+' '+y,
                                warray[i*n:((i+1)*n)]))
  return ret

x=set(cngram(s1, 2))
y=set(cngram(s2, 2))

print("x|y = " + str(x|y))
print("x&y = " + str(x&y))
print("x^y = " + str(x^y))
print("'se' in x = " + str('se' in set(x)))
print("'se' in y = " + str('se' in set(y)))

