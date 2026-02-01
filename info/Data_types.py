a = 10
print(a)
print(type(a))

f = 3.14
print(f)
print(type(f))

c = "Hello World"
print(c)
print(type(c))

b = True
print(b)
print(type(b))

e = 3 + 5j                              # j is used to represent the imaginary part in Python. 'J' or 'j' can be used.
print(e)
print(type(e))
print(e.real)                           # Accessing the real part of the complex number.
print(e.imag)                           # Accessing the imaginary part of the complex number.

l = [5, 5.5, "Hello", True, 3 + 5j]     # List Declaration with multiple data types.
print(l)
print(type(l))
print(len(l))

t = (5, 5.5, "Hello", True, 3 + 5j)     # Tuple Declaration with multiple data types. If want to create with single element then use, after element.
print(t)
print(type(t))
print(len(t))

s = {5, 5, 5.5, "Hello", True, 3 + 5j}  # Set Declaration with multiple data types.
print(s)                                # Prints data in unordered manner and removes duplicates.
print(type(s))
print(len(s))

d = {'Key': 'Value', 1: 'One', 2: 'Two', 'name': 'Yash'}  # Dictionary Declaration with multiple data types.
print(d)
print(type(d))
print(len(d))