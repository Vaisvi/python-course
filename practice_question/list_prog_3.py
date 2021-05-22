# create a nested list using user input,the length of list depend on the user
x = []
y = int(input('Enter size of list:'))
for i in range(y):
    xa = []
    for j in range(y):
        ya =int(input('Enter the value:'))
        xa.append(ya)
    x.append(xa)
print(x)        

    



    
  
   
   
