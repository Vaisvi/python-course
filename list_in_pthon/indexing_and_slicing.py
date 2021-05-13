numbers = [1,2,3,4,5,6]
names = ['ravi','vaishali','mahima','ruchi','saumya','shreya']

heights = ['ravi',5.6,'vaishali',5.2,'mahima',4.8,'ruchi',5.2,'saumya',4.9,'shreya',5.5]
info = [True,True,False,True,False]

marks_per_year = [[45,46,22],[22,48,45],[66,77,43]]
team = [['raju','ramu','nand'],['khrisna','shyam','prasad']]
primes = [2,3,5,4,6,7,97,57,68,456,910,89]

#indexing
x = numbers[0]
print(x)

winner = names[3]
print(winner)

print(heights[1])
print(heights[2])
print(heights[-2])

print(marks_per_year[0])
print(marks_per_year[1])
print(marks_per_year[0][2])
print(marks_per_year[-1][-1])
print(marks_per_year[0][-1])

extra_number = team[0][-1]
print(extra_number)

# slicing
first_two_numbers = numbers[:2]
last_two_numbers = numbers[-2:]
print (first_two_numbers)
print(last_two_numbers)

first_three_names = names[:3]
even_idx_name = names[::2]
print(first_three_names)
print(even_idx_name)
print(primes[::-1])

first_year_2_subject_marks = marks_per_year[0][:2]
last_year_last_2_subject_marks = marks_per_year[-1][-2:]
print(first_year_2_subject_marks)
print(last_year_last_2_subject_marks)
