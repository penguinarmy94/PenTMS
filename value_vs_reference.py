import copy

class StringClass:
    def __init__(self, mystring: str):
        self.string: str = mystring

# Call By Value
a: StringClass = StringClass("mystring")
b: StringClass = copy.deepcopy(a)

print(a == b)
print(a)
print(b)

a.string = "I love this new string"

print(b.string)

# Call By Reference
c: StringClass = StringClass("mystring")
d: StringClass = c

print(c == d)
print(c)
print(d)

c.string = "I love my new string"

print(d.string)

numa = [1,2,3]
numb = copy.deepcopy(numa)

print(numb)

numa.append(4)

print(numb)

    
    