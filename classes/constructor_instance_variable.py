<<<<<<< HEAD

class Pet:
    
    def __init__(self, name, age, pettype):
        # instance variable  (object varizble)

        self.name = name
        self.age = age
        self.pettype = pettype
#### class finish

p1 = Pet('cabby','dog',3)
p2 = Pet('scooby','cat',5)
joey = Pet('joey','cow',8)

print(p1.name, p1.age, p1.pettype)
print(p2.name, p2.age, p2.pettype)
print(joey.name,joey.age,joey.pettype)

p1.age = 11
=======

class Pet:
    
    def __init__(self, name, age, pettype):
        # instance variable  (object varizble)

        self.name = name
        self.age = age
        self.pettype = pettype
#### class finish

p1 = Pet('cabby','dog',3)
p2 = Pet('scooby','cat',5)
joey = Pet('joey','cow',8)

print(p1.name, p1.age, p1.pettype)
print(p2.name, p2.age, p2.pettype)
print(joey.name,joey.age,joey.pettype)

p1.age = 11
>>>>>>> fb34d168543fe7992330da7855fff8f06c7a3637
print(p1.name,p1.age,p1.pettype)