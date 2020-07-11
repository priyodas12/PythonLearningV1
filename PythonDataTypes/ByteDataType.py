#
"""
1.in the range of 0-256
2.represents group of byte numbers,just like array
3.bytes data type is immutable
"""
v=[1,2,3,4]
b=bytes(v); # ValueError: bytes must be in range(0, 256)
print(type(b))
print(b)
print(b[0])
print(b[-1])
for x in b:print(x)