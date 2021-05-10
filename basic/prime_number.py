# prog to find if nuber is prime
num= int(input('enter the number:'))

for i in range(2, num):
    print(num,'%','i','=',num%i)
    if num % i == 0:
        print("non prime")
        break
else:
    print('prime')    

