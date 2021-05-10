#datatypes
#integer (int)
a=1
b=2342
c=+372636
d=-774873393284

print(type(a),type(b),type(c),type(d))

#float
a=1.1
b=+273.45
c=-8472.434
d=.4040323

print(type(a),type(b),type(c),type(d))

#bool

a=True
b=False
c=a and b
d=a or b

print(type(a),type(b),type(c),type(d))

#string

a='apple'
b="banana"
c='''what is your name
how are you'''
d="""hi
how
are
you
"""

print(type(a),type(b),type(c),type(d))

#None

a=None
b=None
print(type(a),type(b))
z=None
print(z)

#data - structure

#list
a=[1,2,3,4,5,6]
print(type(a))

#tupple

a=(1,2,3,4,5,6)
b=(4,65,3,6)
print(type(a),type(b))

#set
a={1,5,4,6,3,4}
b={3,5,6,3,7,8,2,4,5,7}
print(type(a),type(b))

#dictonary
d={"name":'apple','price':200}
c={1:1000,2:2000,3:3000}
print(type(c),type(d))

#programmatically check type
a=10
out=isinstance(a,int)
print("is an integer",out)
out=isinstance(a,float)
print("is a float",out)

price=input('enter the price of mouse you bought')
print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,str))
