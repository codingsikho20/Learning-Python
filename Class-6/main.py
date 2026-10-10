# if else statement in python

#age = int(input("Enter your age: "))
#if age >= 18:
 #   print("You are eligible to vote.")
#else:
 #   print("You are not eligible to vote.")


# age = int(input("Enter your age:" ))
# print("You are elegible for voting." if age >= 18 else "You are not eligible for voting.")

money = int(input("Enter the amount of money you have: "))

if money == 10:
    print("you can buy a choco")

elif money == 20:
    print("you can buy a choco and buiscuts" )

elif money == 30:
    print("You can buy a choco, buiscuts and chips")

else:
    print("You don't have enough money to buy anything.")


    "even" if 10 % 2 == 0 else "odd"
    print("The number is even." if 10 % 2 == 0 else "The number is odd.")

a = 10
b = 40
c = 30

if a > b and a > c:
    print("A is the largest number")

elif b > a and b > c:
    print("B is the largeat number")


#Repeat question

# Question no 1.
a = float(input("Please tell me first number: "))
b = float(input("Please tell me second number: "))

if a > b:
    print(f"{a} is greter then {b}")
elif b > a:
    print(f"{b} is greater then {a}")