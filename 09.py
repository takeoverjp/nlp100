#!/usr/bin/python3

# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．

import random

s="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(s):
  ret=""
  ar=s.split()
  for w in ar:
    if len(ret) >= 1:
      ret += " "
    if len(w) <=4:
      ret += w
    else:
      ret += w[0] + ''.join((random.sample(w[1:(len(w)-1)], len(w)-2))) + w[-1]
  return ret

assert(typoglycemia("abc") == "abc")
assert(typoglycemia("abcdef")[0] == "a")
assert(typoglycemia("abcdef")[-1] == "f")
assert(typoglycemia("abc def") == "abc def")
print(typoglycemia(s))
