"""
set:
----
1. represented by {}
2. no insertion order maintained
3. duplicates not allowed
4. index,slicing terminology not applicable for set
5. mutable,growable
"""
s={10,20,30,40,10}
s.add(123)
s.remove(40)

for x in s:print(x) # duplicate will not be added.
# print(s[0]) # TypeError: 'set' object is not subscriptable

