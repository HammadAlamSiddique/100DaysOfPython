# Strinf Functions
## Strings are immutable

name = "Hammad"

# length of a string len()
print(len(name))

# Upper case upper()
print(name.upper())

# Lowercase lower()
print(name.lower())

# lstrip() removes characters from left-side of the string
a = "!!!!Shadman"
print(a.lstrip("!"))

# rstrip() removes characters from right-side of the string
b = "Shadman@@@@@"
print(b.rstrip("@"))

# strip() removes characters from both sides of the string
c = "####Shadman####"
print(c.strip("#"))



# replace() replaces string into another string
a = "Haris"
print(a.replace("Haris", "Qazi"))

# split() splits string at the specified instance
b = "This string is splitted"
print(b.split(" "))

# capitalize() make first letter capital
c = "this string iS capitAlize"
print(c.capitalize())

# center() aligns the string as per the parameters given by the user
d = "This sring is aligned"
print(d.center(50))

# count() returns the number of times the given value has occured within the given string
e = "Shah jee is Shah jee, No one can replace him"
print(e.count("Shah jee"))

# endswith() returns the boolean value if the string ends with certain value or not
f = "This string is ends with Hammad"
print(f.endswith("Hammad"))
# We can also even check the value in-between the string
print(f.endswith("ing", 8,11))
# startswith()returns the boolean value if the string starts with certain value or not
print(f.startswith("This"))

# find() searches the first occurences of the given value and returns its index position. If not found, returns -1
g = "Hammad in its first occurence"
print(g.find("Hammad"))
# index() method also do the same. But if the string is not found, it gives error instead of -1.

# isalnum() returns True only if the entire string only consists A-Z, a-z, 0-9. Returns False if any other characters or punctuations are present.
h = "IsThisTheRealLife009"
print(h.isalnum()) 

# isalpha() returns True only if the entire string only consists A-Z and a-z. Returns False if any other characters or punctuations are present.
i = "IsThisTheRealLife009"
print(h.isalpha())


j = "lower string"  # returns True if the whole string is in lower case
k = "UPPER STRING"  # returns True if the whole string is in upper case
l = "Proper String" # returns True if the whole string is in proper case
print(j.islower())
print(k.isupper())
print(l.istitle())


# isprintable() returns True if the string has printable characters
m = "Wish you happy birthday\n"
print(m.isprintable())

# isspace() returns True if the string has wide spaces
n = "      "
print(n.isspace())

# swapcase() changes every character cases of the string. Upper to lower or lower to upper
o = "this is a string"
print(o.swapcase())

# title) changes every first character of the word to Capital.
p = "this is so good to have"
print(p.title())
