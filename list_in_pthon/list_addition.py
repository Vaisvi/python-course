#add each item from 2 list and store result in 3rd list

x = [3,5,4,3,6,3,7,8,]
y = [22,66,55,44,88,59,44,83,33]

z = []
for i,j in zip(x,y):
    z.append(i+j)

print(x)    
print(y)    
print(z)    