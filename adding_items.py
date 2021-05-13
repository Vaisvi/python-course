x = []
y = [1,2,3]

# adding single values to list
x.append(10)
x.append(20)
x.append(30)

x.append(4)
x.append(6)
x.append(8)
#onser single value to list
z = [1,3,5,7,9,10]
z.insert(1,2) #insert 2 at indesx 1
z.insert(3,20) #insert 20 at index 3

print(x)
print(y)
print(z)

# replace a value at an index (no fun, direct assignment)
x[0] = 100
x[-1] = 400
z[3] = 3

print(x)
print(y)
print(z)


