#
x = int(input('enter a list of cricketers:'))
print('enter the name of cricketers:')
y = []
for i in range(x):
    name = input()
    if name == name.title():
        y.append(name)
print(y)        


