print("hello")

a = "NURURE BEAUTIFUL"

print(a[7])

a = "Sheryians Coding School"

#print(a[0:9:1])

#there are default values aswell

print(a[:9:])

# thore are challenge aswel 

b = "Hello i am a Data Scientist"

# Extract Hello
print(b[0:5:1])

# Extract Data
print(b[13:17:1])

# Extract Scintist
print(b[18:27:1])

c = 45
print(c)

c = "hello"
#print(c[1])
c[1] = "e" # this will give an error because string is immutable in python

# What is a formatted string
age = 22
Des = "Data Scientist"
print(f"My name is Manish and my age is {age} and my designation letter is {Des}")

# escape sequence
print("Hello\nWorld")   

#type conversion
a = 12
print(type(a))  

a = 58
a = float(a)  # converting integer to float
print(type (a))

# input
age = input("Enter your age: ")
print(f"your age is {age}")


a = "Hello"
print(a[4])