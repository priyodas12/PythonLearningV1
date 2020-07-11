"""
1. insertion order maintained.
2. duplicates are allowed.
3. list convention []
4. heterogeneous object is allowed.
5. growable
6. mutable
"""
l=[1,2,3,4,5,6,'abc',True,1.0,1,None]
print(len(l))

# alter elements
# l[10]=10

# type of
print(type(l))

# print all elements
for x in l:print(x)

# slice operation<returns List>
print(l[1:4])

# multiply of element
print(l*2)

# inner list
l2=[[1,2],[3,4],[5,6]]
for x in l2:print(x)