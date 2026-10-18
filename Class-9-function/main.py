# def greet():
#     print("Hello! Welcome to the program.")

# greet()

# def add ():
#     return "This function is return statement."
# result = add()
# print(result)

# def addition(a, b):
#     print(a + b)
# addition(5, 10)
# addition(20, 30)
# addition(200, 100)

# def addition():
#     a = 12
#     b = 13
#     print(a + b)
# addition()

# def check_palindrome(x):
#     rev = 0
#     copy = x
#     while x > 0:
#         rev = (rev * 10) + (x % 10)
#         x = x // 10
#     if rev == copy:
#         return True
#     else:
#         return False

# print(check_palindrome(121))
# print(check_palindrome(123))
# print(check_palindrome(212))
# print(check_palindrome(12321))

# def addition(a, b, c):
#     print(a + b + c)

# addition(13, 43, 25)

# keyword arguments

# def addition(a, b, c):
#     print(a + b + c)

# addition(c=13, a=43, b=32)

# def addition(a, b, c=12):
#     print(a + b + c)

# addition(12, 23, 54)

def addition(a, c, b=12):
    print(a + b + c)

addition(12, 43, 56)
