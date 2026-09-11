# if Else or elif statement is used to check conditions in python.

# question - 1

#a = float(input("Enter a first number: "))
#b = float(input("Enter a second number: "))

#if a > b:
 #   print(f"{a} is greater than {b}")
#
#elif a < b:
 #   print(f"{b} is greater than {a}")

#else:
 #   print(f"{a} is equal to {b}")

# question 2 & 3

#gen = input("Enter your gender in character (m/f): ")

#if gen == 'm' or gen == "M":
 #   print("Hello sir how are you, thank you for the check your gender, congratulation aap ek adami hai")

#elif gen == "F" or gen == "f":
 #   print("Hello mam how are you, thank you for the check your gender and congratulation aap ek mahila hai")

#else:
 #   print("Wrong input only provide m or f")


#question 4

#a = int(input("Enter a number:- "))

#if a % 2 == 0:
 #   print("Your number is Even")

#else: 
 #   print("Your number is odd")

# question 5
#name = input("Please Enter your name: ")
#age = int(input("Please Enter your age: "))

#if age >= 18:
 #   print(f"Hello {name} you can vote")
#else:
 #   print(f"Hello {name} sorry you can vote after {18 - age} years")

#a = int(input("Enter a your lucky day(1 - 7):- "))

#if a == 1:
   # print("Today is Monday")
#elif a == 2:
 #   print("Today is Tuesday")
#elif a == 3:
 #   print("Today is Wednesday")
#elif a == 4:
 #   print("Today is Thursday")
#elif a == 5:
 #   print("Today is Friday")
#elif a == 6:
 #   print("Today is Saturday")
#elif a == 7:
 #    print("Today is Sunday")
#else:
 #   print("Invalid input. Please enter a number between 1 and 7.")

#a = int(input("Enter a number: "))
#b = int(input("Enter a number: "))
#c = int(input("Enter a number: "))

#if a == b and b == c:
 #   print("All three numbers are equal.")
#elif a == b or b == c or c == a:
 #   print("Any two numbers are equal.")
#elif a > b and a > c:
 #   print(f"{a} is the greatest number.")
#elif b > a and b > c:
 #   print(f"{b} is the greatest number.")
#else:
 #     print(f"{c} is the greatest number.")


#year = int(input("Enter a year:- "))

#if year % 100 == 0 and year % 400 == 0:
#    print("its is a leap year.")
#elif year % 100 != 0 and year % 4 == 0:
#    print("its is a leap year.")
#else:
 #   print("its is not a leap year.")

#Bill = int(input("Enter your bill amount:"))
#if Bill >= 1000 and Bill <= 4999:
 #   print(f"you got a discount of 10% your final bill amount is {(Bill * 90) / 100}")
#elif Bill >= 5000:
 #   print(f"you got a discount of 20% your final amount is {(Bill * 80) / 100}")

#else:
 #   print("sorry no discount for you")

#char = input("Enter a character: ")

#if char in "aeiouAEIOU":
 #   print("its a vowel.")
#else:
 #   print("its a consonant.")

# MCQ question

#number = int(input("Enter a number: "))
#if number > 0: 
 #   print("The number is positive. ")
#elif number < 0:
#   print("The number is negative. ")
# else:
#    print("The number is zero.")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even. ")
else:
    print("The number is odd. ")
