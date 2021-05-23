a = {1,2,3,4,6,7,8,9,10}
b = {1,2,3,4}
c = {6,7,8,9,10}
d = {3,4,5,6,7,8}
e = {11,22,33}

#set functions
 #add
 #remove
 # clear 
 # pop
 # issubset
 # issuperset
 # isdisjoint

# union
# intersection
# difference
# symmetric_difference  

e.add('apple')
c.remove(9)
d.update([1,2,3,6,77,8,78])
e.pop() # pop out a random value from a set

print(a)
print(b)
print(c)
print(d)
print(e)

print(a.issuperset(c),'a is superset of c')
print(a.issuperset(d),'a is superset of d')

if b.issubset(a):
    print('b is subset of a')
else:
    print('b is not subset a')    

if e.issubset(d):
    print('e is subset of d')
else:
    print('e is not subset d')    

if b.isdisjoint(d):
    print('b is disjoint of d')
else:
    print('b is not disjoint d' )        

if a.isdisjoint(e):
    print('a is disjoint of e')
else:
    print('a is not disjoint e' )  

#set maths

# union, take every unique values from the set

print('union')
print(a.union(d))
print(a|d)          

print('difference')
print(a.difference(d))
print(a-d)          

print('intersection')
print(a.intersection(d))
print(a & d)          

print('symmetric differnce')
print(a.symmetric_difference(d))
print(a ^ d)          