# ----- Arithmetic Operators -----
x = 10
y = 4
p = x + y 
print(p)

q = x - y
print(q)

r = x * y
print(r)

s = x / y
print(s)

t = x % y # Remainder when x is divided by y
print(t)

u = x ** y # x raised to the power y
print(u)

v = x // y # Only the integer part of the quotient is stored.(floor division)
print(v)

# ----- Comparison Operators -----
m = 10
n = 20
print(m == n)  # Equal to
print(m != n)  # Not equal to
print(m > n)   # Greater than
print(m < n)   # Less than
print(m >= n)  # Greater than or equal to
print(m <= n)  # Less than or equal to

# ----- Logical Operators -----
A = True
B = False
print(A and B)  # Logical AND
print(A or B)   # Logical OR
print(not A)    # Logical NOT

e = 5 
f = 10
print(e < 10 and f > 5)  # Both conditions are true
print(e < 10 and f < 5)  # One condition is false, so output is false
print(e < 10 or f < 5)   # At least one condition is true then output is true
print(not (e < 10))     # Negation of the condition

# True value is treated as '1' and False value is treated as '0' in arithmetic operations
print( True + True )   # Output: 2
print( True - True)    # Output: 0
print( True * True)    # Output: 1
print(True / True)     # Output: 1.0

# ----- Assignment Operators -----
a = 10 
b = 2
a += b     # a = a + b  # Variable a is increased by the value of b and stored back in a.
print(a)

c = 10
d = 2
c -= d     # c = c - d  # Variable c is decreased by the value of d and stored back in c.
print(c)   

A = 10
B = 2
A *= B     # A = A * B  # Variable A is multiplied by the value of B and stored back in A.
print(A)

C = 10
D = 2
C /= D     # C = C / D  # Variable C is divided by the value of D and stored back in C.
print(C)

# ----- Bitwise Operators -----
g = 12
print(g >> 2) # Right shift the bits of g by 2 positions, in binary 12 is 1100, after right shift it becomes 0011 which is 3 in decimal.
print(g << 2) # Left shift the bits of g by 2 positions, in binary 12 is 1100, after left shift it becomes 110000 which is 48 in decimal.

# ----- Membership Operators -----
S = "Python"
print('y' in S)     # Checks if 'y' is present in the string S (case-sensitive).
print('Y' not in S) # Checks if 'Y' is not present in the string S (case-sensitive).

T = "Hello"
U = "ello"
print(U in T)      # Checks if string U is a substring of string T.
print(U not in T)  # Checks if string U is not a substring of string T

S = "Python"
print(len(S))  # Returns the length of the string S.
print(type(S)) # Returns the type of variable S.

V = "10"
print(len(V))  # Returns the length of the string V.
print(type(V)) # Returns the type of variable V.

W = 14
print(type(W)) # Returns the type of variable W.

# length cannot be used with integer or float values

# ----- Identity Operators ----
a = 10
b = 10
print(a is b)      # Checks if both a and b refer to the same object in memory.
print(a is not b)  # Checks if a and b do not refer to the same object in memory.

z = "Hello"
Z = "Hello"
print(z is Z)      # Checks if both z and Z refer to the same object in memory.
print(z is not Z)  # Checks if z and Z do not refer to the same object in memory.