#!/usr/bin/python3

s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ret=list(map(lambda x: len(x), s.split()))
print(ret)
