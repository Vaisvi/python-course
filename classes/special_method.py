class Student:

    def __init__(self,name,cls,marks):
        self.name = name
        self.cls = cls
        self.marks = marks

    def show(self):
        print('name =>',self.name)
        print('cls =>',self.cls)
        print('marks =>',self.marks)
    # convert object to string when printed
    def __str__(self):
        return f'{self.name} in {self.cls}'

    def __gt__(self,other):
        return self.marks >  other.marks    

    #def __lt__(self,other):
        return self.marks <  other.marks    

    #def __gt__(self,other):
        return self.marks ==  other.marks    

    #def __add__(self,other):
        return self.marks +  other.marks    

    #def __repr__(self):
        return self.name    
           

s1 = Student('vaishali',12,78)        
s2 = Student('nidhi',11,88)        
s3 = Student('smita',12,98)        
s4 = Student('gauravi',12,68)        
s5 = Student('nikita',10,98)  

print(s1)
print(s2)

if s3 > s1:
    print(f'{s3} got more marks')

Student = [s1,s2,s3,s4,s5]  
Student.sort()  


    