names = ['ravi','vaishali','mahima','ruchi','saumya','shreya']
numbers = [4,3,5,6,77,8]

heights = ['ravi',5.6,'vaishali',5.2,'mahima',4.8,'ruchi',5.2,'saumya',4.9,'shreya',5.5]
info = [True,True,False,True,False]

marks_per_year = [[45,46,22],[22,48,45],[66,77,43]]
team = [['raju','ramu','nand'],['khrisna','shyam'],['prasad','shreyam']]

print(numbers)
numbers.remove(5)
print(numbers)

marks_per_year[0].remove(45)
print(marks_per_year)

names.remove('mahima')
print('remove mahima',names)

names.pop()#last value is removed by default
print('last value',names)
names.pop(1)#pop out value at index 1
print('value at index 1',names)

marks_per_year.clear()
team.clear()
print(marks_per_year)
print(team)

