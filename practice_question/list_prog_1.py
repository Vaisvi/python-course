# wAP to create a list of 50 prime numbers
x = [1,50]
#upper = [50]
for num in range(1 , 50):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print(num)    