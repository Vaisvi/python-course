name = 'vijay deenanath chauhan  '

fname = name[0:5]
print(fname)
mname = name[6:15]
print(mname)
mname = name[6:-8]
print(mname)
lname = name[-7:len(name)]
print(lname)

# for better version
fname = name[ :5]
lname = name[-7:]
print(fname,lname)

# full name
print(name[:])

# reverse 
print(name[::-1])

#every 2 second char in string
print(name[::2])