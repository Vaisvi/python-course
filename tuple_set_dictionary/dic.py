emp = {
    'name':'vaishali Dixit',
    'designation':'assistan level 3',
    'salary':{
        'basic':'10000',
        'da':'8000',
        'hra':'5000',
        'misc':'10000'

    },
    'dept':'Account',
    'doj':{
        'year':'2003',
        'month':'o9',
        'date':'09'
    },
}
print(emp)
print(emp['name'])
print(emp['salary']['hra'])
print(emp['dept'])
print(emp['doj']['year'])

stockprices = dict(google=234,facebook=211.23,netflix=200.1)
print('another dictonary')
print(stockprices)

#add value
stockprices['disney']=250.23
print(stockprices)

emp['phone']='3479243843'
print(emp)

#update
print('update a value')

stockprices['facebook']=180.23
print(stockprices)

emp['dept']='Sales'
print(emp)
