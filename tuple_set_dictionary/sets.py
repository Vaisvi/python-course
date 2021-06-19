<<<<<<< HEAD
x = {1,2,3,4,5}
y = {'apple','banana','mango'}
z = {1,1,2,2,3,4,5,4,3,2,5,1}

print(x)
print(y)
print(z)

a = [1,2,3,4,5] #list
b = (2,33,3,4,5) #tuple
# list and tuple are interconvertable
# set values cannot be indexed and slicied

a_set = set(a)
b_set = set(b)
print(a,a_set)
print(b,b_set)

for i in a_set:
=======
x = {1,2,3,4,5}
y = {'apple','banana','mango'}
z = {1,1,2,2,3,4,5,4,3,2,5,1}

print(x)
print(y)
print(z)

a = [1,2,3,4,5] #list
b = (2,33,3,4,5) #tuple
# list and tuple are interconvertable
# set values cannot be indexed and slicied

a_set = set(a)
b_set = set(b)
print(a,a_set)
print(b,b_set)

for i in a_set:
>>>>>>> fb34d168543fe7992330da7855fff8f06c7a3637
    print(i,end='')