# Tuple
# tuple has hetrogenous nature
a = (12, 12.4, "hell", print())

# tuple has immutable nature
a = (1, 2, 3, 4, 5)

a[1] = 20 # there will be an error

# tuple can store duoplicate value
a = (1, 2, 3, 3, 11, 2, 2, 2, 2, 2, 2,)

# tuple unpacking
a,b,c = (10,20,30)
print(b)

a = (1)
print(type(a))

a = (10, 20, 30, 40)
print(a[:3])

a = [10, 2, 30, 40]
tup = tuple(a)
print(tup)

t = (10,20,30,40,50)
# 1st way
for i in t:
    print(i)

# 2nd way 
for i in  range(len(t)):
    print(t[i])

a = (10, 20, 30, 40, 40, 40, 50)
print(a.count(40))
print(a.index(30))
