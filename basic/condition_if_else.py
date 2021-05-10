a=int(input("enter a number"))
if a>100:
    print("well done,you got that right")
else:
    print("nice try, but not enough")  

#if_else_2

a=input("enter the number")
b=input("enter the another number")

if a.isnumeric() and b.isnumeric():
    a=int(a)
    b=int(b)
    if a>b:
        print(a+b)
    else:
        print(a-b) 
else:
    print("we need number not anything else")           