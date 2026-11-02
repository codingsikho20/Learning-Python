# s = {10, "hello", (1,2,3,4), 12,34, True, print()}
# you can only store hashable values inside set

# unordered nature
# s = {10, 20, 30, 50, 70, 60}
# print(s[0])

# you cannot have duplicate value
# s = {10,10,101,1,1,1,1, 320, 203,3,23,2032,4,32}
# print(s)

# a = [13,314,1,4,45,52,454,545,45,6,67,6,76,6,574]
# s = set(a)
# print(s)

# traversing on the set
# s = {13,1,41,4,14,1,563,56,54,7,45,74,764}
# for i in s:
#     print(i)

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1 | s2)