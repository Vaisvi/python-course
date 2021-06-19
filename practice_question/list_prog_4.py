<<<<<<< HEAD
# write program to store all the armstrong number till 1000000

l = 1
u = 1000000
for num in range(l, u+1):
    
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit **3
        temp //= 10
    if num == sum:
=======
# write program to store all the armstrong number till 1000000

l = 1
u = 1000000
for num in range(l, u+1):
    
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit **3
        temp //= 10
    if num == sum:
>>>>>>> fb34d168543fe7992330da7855fff8f06c7a3637
        print(num)     