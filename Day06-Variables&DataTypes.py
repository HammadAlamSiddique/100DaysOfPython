# Variables are containers to store data

# Different variables with different data types
a = "Hammad"
b = 123
c = 33.921
d = True
e = complex(3,4)
f = None

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))


# Sequenced Data Type (list, tuple, set, dictionary)
l = [1,3,"Sara",9.0,[2,4]]
print(l, type(l))

t = (1,3,"Sara",9.0,(2,4))
print(t, type(t))

s = {1,3,"Sara", 9.0}   # you can't put set inside a set
print(s, type(s))

d = {"name":"Sara",
     "age":25,
     "canVote":True,
     "OtherDeatils":{"education":"BS CS", "section":"C"}}
print(d, type(d))