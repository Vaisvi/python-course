start=100
while start >=0:
    print(start)
    start -=5

print('the end')  

# Example_2 sum of all digits

num = 12435467
total=0
while num > 0:
    r = num % 10
    total += r
    num = num // 10
print('total',total) 

# Example_3 Infinite loop

while True:
    password = input('enter the secret password:')
    if password == 'open sesame':
     print('welcome master')
     break
else:
    print('haha, keep trying')