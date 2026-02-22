# a = "This is Python string methods example."
# print(a)
# print(len(a))
# print(type(a))
# print(a[0])             # Indexing, Accessing first character of the string.
# print(a[-3])            # Indexing, Accessing third last character of the string.
# print(a[0:7:2])         # Indexing[Start : End : Step], Slicing the string to get first 7 characters.
# print(a[::-1])          # Reversing the string using slicing.
# print(a[-8:-4])         # Slicing the string to get characters from index -8 to -4. -ve indexing should always be left to right.
# print (a + " " + "10")  # String concatenation with another string.

# b = "        Python         "
# print(b)
# print(len(b))
# r = b.rstrip()            # rstrip() method removes trailing whitespace from the right end of the string.
# print(r)
# print(len(r))
# p = b.lstrip()            # lstrip() method removes leading whitespace from the left end of the string.
# print(p)
# print(len(p))
# m = b.strip()             # strip() method removes leading and trailing whitespace from both ends of the string.
# print(m)
# print(len(m))

# c = input("Enter a number: ")
# print(c)
# print(type(c))
# d = int(c)                # Converting the string input to an integer using int() function.
# print(type(d))
# print(d + 10)             # Performing addition with the converted integer.

# e = int(input("Enter a number: "))
# print(e + 10)             # Performing addition with the integer input directly without converting it to string.

# f = "PythonDataPythonData"
# print(f)
# result = f.find("Data")    # find() method returns the index of the first occurrence of the specified substring. If not found, it returns -1.
# ans = f.count("Data")      # count() method counts the number of occurrences of the specified substring in the string.
# print(ans)
# print(result)              

# g = "Python is easy, Python is easy, Python is easy"
# print(g)
# i = g.replace("Python", "SQL", 2)
# print(i)

# j = ("C", "C++", "Python")
# print(j)
# k = " ".join(j)
# print(k)

# l = "Learning python"
# m = l.lower()
# print(m)
# n = l.upper()
# print(n)
# o = l.title()
# print(o)
# p = l.capitalize()
# print(p)
# q = l.swapcase()
# print(q)