s='abcdefghij'

# positive indexing(left to right)
print(s[0])
# negative indexing(right to left)
print(s[-1])

# out of range
# print(s[10])
# IndexError: string index out of range

# capture rest
print(s[4:])

# capture from first up to
print(s[:4])

# 1st one is inclusive,2nd one exclusive
print(s[2:5])
print(s[1:-1])

# slice by section
print(s[1:10:3])

# string multiply or concatenation
print(s*3)

# length a string
print(len(s))

# reverse a string
print(s[::-1])

#

