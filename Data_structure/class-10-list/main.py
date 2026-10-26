# question no1. sum and average of list
# Create a list of numbers, then calculate and print the total sum and average.

# a = [10, 20, 30, 40, 50]
# sum = 0
# for i in a:
#     sum = sum + i

# print(f"sum of list numbers is {sum}")
# print(f"average of list numbers is {sum/len(a)}")

# question no2. maximum element with index
# find the largest element in list along with its position (index).

# a = [1, 54, 85, 14, 98, 25, 99, 456, 548]

# max = a[0]
# index = 0

# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i

# print(f"maximum element in list is {max} and its index is {index}")

# question no3. second greatest element in list
# identify the second largest element in the list without sorting directly.

# a = [1, 54, 85, 14, 98, 25, 99, 456, 548, 40, 50, 780, 876]

# max = a[0]
# max2 = a[0]
# index = 0
# index2 = 0

# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         index2 = index
#         max = a[i]
#         index = i

#     elif a[i] > max2:
#         max2 = a[i]
#         index2 = i

# print(f"max {max} at {index} and max 2 is {max2} at {index2}")

# question no4. check if list is sorted (Increasing)
# verify wheather the list elements are in ascending order.

a = [12, 13, 14, 15, 16, 17, 18, 19, 23, 43, 45, 55, 67]

for i in range(len(a)-1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("your list is not sorted in ascending order")
        break
else:
    print("your list is sorted in ascending order")