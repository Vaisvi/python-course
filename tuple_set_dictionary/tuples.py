x = (1,2,3,4,5,6)
y = 12,34,54,22,65

print(type(x))
print(type(y))
 
a = [1,23,45,32] 
at = tuple(a)    # list to tuple conversion
print(a,at)

name = 'vaishali'
namet = tuple(name)
print('string =>',name,'tuple =>',namet)

a = 1
b = 2
c = 3
d = a,b,c
print(d)

# function
#count
#index
a = (11,1,2,32,2,4,1,2,3,4,3,2,4,5,3,2,4,3)
print('count all the 3s =',a.count(3))
print('index if 32 =',a.index(32))