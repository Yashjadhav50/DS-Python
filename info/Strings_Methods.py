a = "This is Python string methods example."
print(a)
print(len(a))
print(type(a))
print(a[0])             # Indexing, Accessing first character of the string.
print(a[-3])            # Indexing, Accessing third last character of the string.
print(a[0:7:2])         # Indexing[Start : End : Step], Slicing the string to get first 7 characters.
print(a[::-1])          # Reversing the string using slicing.
print(a[-8:-4])         # Slicing the string to get characters from index -8 to -4. -ve indexing should always be left to right.
print (a + " " + "10")  # String concatenation with another string.