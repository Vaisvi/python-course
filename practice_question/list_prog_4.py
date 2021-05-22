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
        print(num)     