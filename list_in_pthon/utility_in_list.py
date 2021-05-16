x = [1,2,3,4,5]
colors = ['red','blue','green']
randomval = [29,83,88,92,22]

print('normal ->',x)
x.reverse()
print('reverse ->',x)
x.reverse()
print('back to normal ->',x)

print('normal ->',colors)
colors.reverse()
print('alphabetical sort ->',colors)

randomval.sort()
print('sorted',randomval)

#colors.reverse()
#print('normal ->',colors)
#colors.reverse()

randomval.sort(reverse=True)
print('sorted',randomval)

#count function work the same as string count
y = [1,2,3,4,3,4,2,5,6,4,6,7,4,3,5,6,7,8,6,4,6,7,8,6]
two_count = y.count(2)
three_count = y.count(3)
eight_count = y.count(8)

print('2 occurs ->',two_count)
print('3 occurs ->',three_count)
print('8 occurs ->',eight_count)

