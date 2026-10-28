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

# a = [12, 13, 14, 15, 16, 17, 18, 19, 23, 43, 45, 55, 67]

# for i in range(len(a)-1):
#     if a[i] < a[i + 1]:
#         continue
#     else:
#         print("your list is not sorted in ascending order")
#         break
# else:2
#     print("your list is sorted in ascending order")

# question no5. left rotation by list
# shift all elements one position to the left, with the first elemrnt to the end.

# a = [10, 20, 30, 40, 50]

# for i in range(len(a)-1):
#     a[i], a[i+1] = a[i+1], a[i]

# print(a)

# k = int(input("how many times you want to rotate :"))
# a = [10, 20, 30, 40, 50]

# for j in range(k):
#     for i in range(len(a)-1):
#         a[i], a[i+1] = a[i+1], a[i]

# print(a)

# question no6. right rotation by list

# a = [10, 20, 30, 40, 50]

# for i in range(len(a)-1, 0, -1):
#     a[i], a[i-1] = a[i-1], a[i]

# print(a)

# question no7. Reverse list in-place
# reverse the entire list without using extra space. (i.e. swap elements)

# a = [10, 20, 30, 40, 50]
# b = len(a)-1

# for i in range(len(a)//2):
#     a[i], a[i+b] = a[b], a[i]
#     b = b -1

# question no8. linear search in list
# search for a giving element by checking each element one by one.

# a = [1,2,3,12,4,21,34,11,412,421,14,12,41,32,434,33,65,51,645,63,55,64,56,45,69,43,754,67]
# search = int(input("enter the number you want to search :"))

# for i in range(len(a)):
#     if a[i] == search:
#         print(f"your number {search} is found at index {i}")
#         break
# else:
#     print(f"your number {search} is not found in the list")

# question no9. binary search in list
# effiecintly search for an element in a sorted list using the divide and conquer approach.

# a = [12, 13, 14, 23, 24, 43, 45, 55, 67, 78, 89, 90]

# search = 23

# start = 0
# last = len(a)-1
# mid = (start + last) // 2

# while start <= last:
#     if a[mid] == search:
#         print(f"your number {search} is found at index {mid}")
#         break
#     elif a[mid] < search:
#         start = mid + 1
#         mid = (start + last)//2

#     elif a[mid] > search:
#         last = mid - 1
#         mid = (start + last)//2

# else:
#     print(f"your number {search} is not found in the list")

# question no10. Bubble short in list
# short the list by rapidly swaping adjust element if they are in the wrong order.

# a = [12,213,21,312,3213,12,32,1321,2,3,32,56345,6,53,5,65,654,3,345,346,3456,3456,]

# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a [i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]

# print(a)


# question no11. selection sort
# sort the list by selecting the smallest element in each pass and placing it the correct position.

a = [12,213,21,312,3213,12,32,1321,2,3,32,56345,6,53,5,65,654,3,345,346,3456,3456,]

for i in range(len(a)-1):
    j = i + 1
    min = i
    for k in range(j, len(a)):
       if a[k] < a[min]:
           min = k

    a[i], a[min] = a [min], a[i]

print(a)