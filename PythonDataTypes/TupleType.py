"""
1. immutable
2. other property same as List
"""
t=(1,2,3,4,5)
print(type(t))
print(t)

# print all element
for x in t:print(x)

# slicing<returns tuple>
print(t[1:4])

# multiplying
print(t*2)

# inner list,tuple
l2=[[1,2],[3,4],(5,6)]
for x in l2:print(x)