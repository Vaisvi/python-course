x = [1,2,13,44,56,61,72,88]

odd_sqr = []
for i in x:
    if i % 2!=0:
        odd_sqr.append(i**2)

print(x)
print(odd_sqr)

# comprehension
even_sqr = [i**2 for i in x if i % 2==0]

print(x)
print(even_sqr)