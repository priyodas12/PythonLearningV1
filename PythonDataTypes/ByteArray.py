"""
1. bytearray is mutable
2. range is (0,256)
"""
v=[1,2,3,4,255]
b=bytearray(v)
b[0]=123

for x in b:print(x)