s='abcdefghij'
# 1st one is inclusive,2nd one exclusive
print(s[2:5])
print(s[1:-1])
# positive indexing(left to right)
print(s[0])
# negative indexing(right to left)
print(s[-1])

# out of range
# print(s[10])
# IndexError: string index out of range

# capture rest
print(s[4:])

