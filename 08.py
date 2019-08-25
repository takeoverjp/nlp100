#!/usr/bin/python3
def cipher(s):
  ret=""
  for c in s:
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
      ret += chr(219-ord(c))
    else:
      ret += c
  return ret

assert(cipher("ABC") == "ABC")
assert(cipher("abc") == "zyx")
assert(cipher("AaBbCc") == "AzByCx")
assert(cipher("あaいbうc") == "あzいyうx")
assert(cipher("ａaｂbｃc") == "ａzｂyｃx")
print("AaBbCc ->", cipher("AaBbCc"),
      "->", cipher(cipher("AaBbCc")))
