#WAP a prog to count the number  of even and odd numbers from a series of number.
even=0
odd=0

for i in range(1,200):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1   
        
print('All the even',even)
print('All the odd',odd)  

#program:-4  

word = input("Input a word to reverse:")

for char in range(len(word)-1,-1,-1):
    print(word[char],end=" ")


# fabonacci series
x=0
y=1
print(x)
while(y<50):
    z=x
    x=y
    y=x+z
    print(y)




