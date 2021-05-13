a = input('enter something')
if a.isupper():
    print('a is upper')

if a.islower():
    print('a is lower')

if a.istitle():
    print('a is in title case')

if a.isalpha():
    print('a contains only alphabet')

if a.isalnum():
    print('a contains only number and alphabet ')

if a.isnumeric():
    print('a contains number only ')

if a.isspace():
    print('a contains spaces ')

if a.isprintable():
    print('a can pe printed ')

if a.isdigit():
    print('a contains digits only ')

if a.isdecimal():
    print('a contains decimal only ')

if a.isascii():
    print('a ascii character')

#check if input is float
b = input('enter a float')
if b.count('.') ==1 and b.replace('.','').isnumeric():
    print("b is float")
else:
    peint('b is not float')        