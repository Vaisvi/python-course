msg = 'my name is vaishali dixit, i am from raebareli '

words = msg.split()
print(words)
print(len(words))

words = msg.split(',')
print(words)
print(len(words))

words = msg.split('vaishali')
print(words)
print(len(words))

msg = 'apple,banana,mango,cheese,maggie'
words = msg.split(',',3)
print(words)

#rsplit
msg = 'apple,banana,mango,cheese,maggie'
words = msg.rsplit(',',3)
print(words)


