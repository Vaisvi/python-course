<<<<<<< HEAD
# wAP to create a list of 50 prime numbers
x = [1,50]
#upper = [50]
for num in range(1 , 50):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
=======
# wAP to create a list of 50 prime numbers
x = [1,50]
#upper = [50]
for num in range(1 , 50):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
>>>>>>> fb34d168543fe7992330da7855fff8f06c7a3637
            print(num)    