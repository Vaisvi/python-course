class Person:

    def __init__(self,name,age,gender):
        self.name= name 
        self.age = age
        self.gender = gender

    def work(self):
        print(f'the {self.name} is working')

    def eat(self):
        print(f'the {self.name} is eating')  

    def sleeping(self):
        print(f'the {self.name} is sleeping') 

    def purchase(self,item):
        print(f'{self.name} purchased {item}')         

class Student(Person):

    def __init__(self, name, age, gender, college,cls):
        super().__init__(name, age, gender)
        self.college = college
        self.cls = cls

    def study(self):
        print(f'{self.name} is studying') 

    def work(self):
        print(f'{self.name} is working on a project')    

    def purchase(self, item):
        super().purchase(item)  
        print('with the help of pocket money')     
    
if __name__ =="__main__":
    p = Person('Rahul',20,'Male')
    p.work()
    p.purchase('mobile')

    s = Student('Rohit',12,'Male','NSPS','8th')
    s.work()
    s.sleeping()
    s.purchase('book')
        