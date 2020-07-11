import cmath
a=2+4j
print(a**2)
print(type(a))
# type casting error<TypeError: can't convert complex to float,int>
print(float(a))

# phase(x) is equivalent to math.atan2(x.imag, x.real),The result lies in the range [-π, π]
print(cmath.phase(a))
# representation of a in polar coordinates
print(cmath.polar(a))
# Return the complex number a,=r * (math.cos(phi) + math.sin(phi)*1j
print(cmath.rect(-1.0, 1.0))
# Returns the logarithm of a to the given base
print(cmath.log10(12))
# Trigonometric  value
print(cmath.cos(45)+cmath.sin(45)+cmath.tan(60))