#!/usr/bin/python3
import math
import functools

s="I am an NLPer"


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

assert(['I ', 'am', ' a', 'n ', 'NL', 'Pe', 'r'] == cngram(s, 2))
assert(['I a', 'm a', 'n N', 'LPe', 'r'] == cngram(s, 3))
assert(['I am', 'an NLPer'] == wngram(s, 2))
assert(['I am an', 'NLPer'] == wngram(s, 3))

print(cngram(s, 2))
print(wngram(s, 2))
