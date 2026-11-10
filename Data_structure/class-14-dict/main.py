# dict

# d = {"Hello":100, "bro":200, "sunday":300}
# print(d["bro"]) accessing value using key
# print(d["sunday"]) 

# changing value of key
# d = {"Hello":100, "bro":200, "sunday":300}
# d["bro"] = 400
# print(d["bro"])

# d = {10:100, 20:200, 30:300, 40:400, 50:500}
# print(d[10])
# print(type(d))

# d = dict(name="Manish", age=20, city="Ballia")
# print(d)
# print(type(d))

# d = dict([("name", "Manish"), ("age", 20), ("city", "Ballia")])
# print(d)
# print(type(d))

# dictionary Traversing
# d = {10:100, 20:200, 30:300, 40:400, 50:500}
# for i in d:
#     print(i)

# help(dict)

a = {10:100, 20:200, 30:300, 40:400, 50:500}
b = {60:600, 70:700, 80:800, 90:900, 100:1000}
a.update(b)
print(a)
