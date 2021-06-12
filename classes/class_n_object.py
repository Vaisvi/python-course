
# example of a simple class
class Fooditem:
    pass

#properties and behaviour
class Cat:
    # property -> class variable
    breed = 'persian'
     

class product:  # method -> class method -> used diesctly with class
    # class varibale
    # instance variable
    # constructor
    def help():
        print('this is class under construction')

# creation object
# object = Classname

maggie = Fooditem()
name = 'vaishali'


print(type(maggie))
print(type(name))
billu = Cat()
tommy = Cat()

print(billu,tommy)
print(billu.breed)
print(tommy.breed)

#class function
product.help()

#should not be used by object
#keyboard.help()
#monitor.help

