dictionary = {
    'name': ['admin', 'user'] ,
    'type': 'univ'
}

print(dictionary)

print(dictionary['name'])

dictionary['price'] = 5000

print(dictionary)

del dictionary['name'][0]

print(dictionary)
