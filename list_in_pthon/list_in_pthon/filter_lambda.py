x = [1,3,4,6,7,8,9,30,10,4,1,2,2,2,3,3,3,1,3,2]

# normal
x3 = []
for i in x:
    if i % 3 == 0:
        x3.append(i)

m3 = lambda i : i %3 == 0
output = list(filter(m3, x))

print(x)
print(m3)
print(output)
