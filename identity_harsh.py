# Integer
a = 10
print("Integer Before:", id(a))
a = a + 5
print("Integer After:", id(a))


# Float
f = 3.14
print("\nFloat Before:", id(f))
f = f + 1.0
print("Float After:", id(f))


# String
s = "hello"
print("\nString Before:", id(s))
s = s + " world"
print("String After:", id(s))


# List
lst = [1, 2, 3]
print("\nList Before:", id(lst))
lst.append(4)
print("List After:", id(lst))


# Tuple
t = (1, 2, 3)
print("\nTuple Before:", id(t))
t = t + (4,)
print("Tuple After:", id(t))


# Set
st = {1, 2, 3}
print("\nSet Before:", id(st))
st.add(4)
print("Set After:", id(st))

print("\nThis is updated version")
