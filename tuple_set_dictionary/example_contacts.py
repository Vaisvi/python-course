# program where user can add contacts for contact book
#user has to enter the contact name
# if contact is availabe then the number is shown
#else if the contact is not available the number is asked fron the user to save

contacts = {'help':1001}
print('your temp contact book')
while True:
    print('-*-' * 25)
    name = input('=> enter contact name:')
    if name:
        if name in contacts:
            print('=> contact found')
            print(f'=> {name}:{contacts[name]}')
        else:
            print('=>contact not found')
            update = input('do you want to add the contact()Y/N? :')
            if update.lower() == 'y':
                number = input(f'>> enter contact number for {name} :')
                contacts[name] = number
                print(f'>> contact update for {name}')
            else:
                print('closing contacting book')
                break    
