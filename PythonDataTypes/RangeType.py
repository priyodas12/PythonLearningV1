"""
range():
------
1. sequence of values
2. immutable
3.
"""
r1=range(10)
print(type(r1))
# for x in r:print(x)
# r[0]=23  #TypeError: 'range' object does not support item assignment

for x in range(11):print(x)

r2=range(10,31)
for x in r2:print(x)

r3=range(10,31,5)
for x in r3:print(x)


# r4=range(12.4)
# for x in r3:print(x) # TypeError: 'float' object cannot be interpreted as an integer



