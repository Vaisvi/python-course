# functions
 #update
 #pop
 #popitem
 #get
 #keys
 #values
 #items
 #clear

fruits = {'apple':100,'banana':40,
         'cherry':150,'dragonfruit':200} 
print('updating values in dict')
new_fruits = {'mango':100,'peach':80}
print(fruits)

print('removing values from dict')

fruits.pop('cherry')
print(fruits)

#better version
if 'orange' in fruits:
    fruits.pop('orange')
    print(fruits)
else:
    print('orange not found')    

last_item_remove = fruits.popitem()
print(fruits)
print(f'{last_item_remove} remove from item')

#accessing value from dict
print(fruits['apple'])
#print(fruits['Apple'])  #error

#better version to access values from dict
print('using the get method in dict')
print(fruits.get('apple'))
print(fruits.get('Apple'))

print('using the get( with default value, in dict')
print(fruits.get('apple','prince not found'))
print(fruits.get('banana','prince not found'))

#access keys values and pair wise items in dict
print(fruits.values())
print(fruits.keys())
print(fruits.items())

print('looping in dict ')
print('normal loop get only keys')

for i in fruits:
    print(i)

print('=>only get vlues')
for i in fruits.values():
    print(i)

print('=> get only values') 
for k,v in fruits.items():
    print(k,'-->',v)          
