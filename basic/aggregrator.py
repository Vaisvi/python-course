end= 10000

#oddtotal = 0
#eventotal = 0

#for i in  range(end+1):
 #   if i % 2 == 0: 
  #      eventotal += 0
   # else:
  #    oddtotal += 0

#print('sum of all odds',oddtotal)
#print('print sum of all even',eventotal)  

#pythonic

print('sum of all evens',sum(range(0,end+1,2)))           
print('sum of all odds',sum(range(1,end+1,2)))           
             
