# a = float(input("Please tell me first number: "))
# b = float(input("Please tell me second number: "))

# if a > b:
#     print(f"{a} is greater than {b}")

# elif b > a:
#     print(f"{b} is greater than {a}")

# else:
#     print(f"{a} is equal to {b}")

# gen = input("Please tell me your gender in character (m/f): ")

# if gen == "m" or gen == "M":
#     print("Hello sir how are you, thank you for the check your gender, congratulation aap ek insaan hai")

# elif gen == "f" or gen == "F":
#     print("Hello mam how are you, thank you for the check your gender and congratulation aap ek aurat hai")

# else:
#     print("Wrong input only provide m or f")

# a = int(input("Please tell me any number: "))
# if a % 2 == 0:
#     print("Your number is even")
# else:
#     print("The number is odd")

# name = input("Please tell me your name: ")
# age = int(input("Please tell me your age: "))

# if age >= 18:
#     print(f"Hello {name}, you can vote")

# else:
#     print(f"Hello {name}, sorry you can vote after {18 - age} years")

# a = int(input("Please tell me a first number: "))
# b = int(input("Please tell me a second number: "))
# c = int(input("Please tell me a third number: "))

# if a == b and b == c:
#     print(f"All three numbers are equal.")

# elif a > b and a > c:
#     print(f"{a} is the greatest number. ")

# elif b > a and b > c:
#     print(f"{b} is the greatest number. ")

# elif a == b or a == c or b == c:
#     print("Any two numbers are equal. ")

# else:
#     print(f"{c} is the greatest number. ")

year = int(input("please tell me a year:- "))

if year % 100 == 0 and year % 400 == 0:
    print("This is a leap year.")

elif year % 100 != 0 and year % 4 == 0:
    print("This is a leap year.")

else:
    print("This is not a leap year.")