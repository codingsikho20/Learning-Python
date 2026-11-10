# question no1. count the frequency of array elements
# count how many times each element appears using a dictionary or hash map

a = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,7,7,7,7,7]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)