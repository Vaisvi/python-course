# WAP to create a list of names and then remove names that contains "a" or "o" char
names = ['Ritesh Kumar Sharma','Vivek Sharma','pope','elex','elin']
names_without_a_or_o = [name for name in names if ('a' not in name.lower() and 'o' not in name.lower())]
print(names_without_a_or_o)



# # create a nested list using user input,the length of list depend on the user
nest_list = []
print('enter values seperated by commas')
while True:
    items = input('enter values >> ').split(',')
    if len(items)>1  and items[0] !='':
        nest_list.append(items)
    else:
        break
print(nest_list)

# write program to store all the armstrong number till 1000000
for num in range(1,100000):
    pow = len(str(num))
    temp = num
    total = 0
    while num >0:
        digit = num % 10
        total += digit ** pow 
        num = num // 10
    if temp == total:
        print(temp, end=',')


#WAP to generate a list of cricketers entered bys user only if the first letter of the name is capital,
#the size will depend upon user
cricketers = []
while True:
    name = input('cricketers name: ')
    if not name:
        break
    elif name[0].isupper():
        cricketers.append(name)
print(cricketers)