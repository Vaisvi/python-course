name = 'vaishali'

def who():    #outside fun
    print('who ami')
    print(f'i am {name}')    #can be accessed inside fun

who()    

def what():
    print('what are you?')
    name = 'God King'     #python can not change value of variable created outside directly
    print(f'I am {name}')  # this is just local value of name var

def update_name():
    global name           #this keyword tells python, that we want to use global var and also modify
    print('old name',name)  
    name = 'Nikita'
    print('new name',name)  

who()
print('global varibale =>',name)
what()
print('global varibale =>',name)   
update_name()
print('global variable',name) 