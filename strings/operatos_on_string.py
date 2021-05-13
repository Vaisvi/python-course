fname = ' vaishali'
lname = 'dixit'

# concatination - joining the string
fullname = fname + ' ' + lname + ' is the name'
print(fullname)

# duplication - cloning the string
word = 'ha'
print(word * 10)
print('- | -'* 20)

# for ;oop for pattern printing
for i in range (1,10):
    print('$ ' * i)

# membership operator 
msg = 'the most important thing in this massage'

if 'thing' in msg:
    print('thing --> word found')

if 'very' in msg:
    print('very--> word found')

if 'z' not in msg:
    print('z is not available in msg')