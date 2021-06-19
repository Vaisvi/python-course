<<<<<<< HEAD
# WAP to create a list of names and then remove names that contains "a" or "o" char
names = ['vaishali','smita','vaibhav','nikita','nidhi','nikit','omkar,sid']
print(names)

names_containing_a = [name for name in names if 'a' in name]
names_containing_o = [name for name in names if 'o' in name]

print(names_containing_a)
=======
# WAP to create a list of names and then remove names that contains "a" or "o" char
names = ['vaishali','smita','vaibhav','nikita','nidhi','nikita','omkar']
print(names)

names_containing_a = [name for name in names if 'a' in name]
names_containing_o = [name for name in names if 'o' in name]

print(names_containing_a)
>>>>>>> fb34d168543fe7992330da7855fff8f06c7a3637
print(names_containing_o)