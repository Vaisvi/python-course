#eg with basic logic

x = [1,2,13,44,56,61,72,88]

x2 = []                      #blank list 
for  i in x:                 #loop
    sqr = i**2
    x2.append(sqr)

print(x)
print(x2)   

#can be done with comprehension with one line #comprehension makes code smaller

x = [2,44,2,55,26,21,11]
#new_list = [operation loop]
x2 = [i**2 for i in x]

print(x)
print(x2)