#fun 1- take no argument
def hello():
    '''
    this is very serious information
    '''
    print('hello friends,happy')
hello()   


# loop in fun

for i in range(10):
    hello()

def world():
    print('this is a awsome fun') 
    hello()
    print('now you are also awsome')
world()

def divide():
    '''
    taking input inside the function is super stupid, but you can still do it
    '''
    x = int(input('enter a number:'))
    y = int(input('another number:'))
    print(x/y)
divide()    
