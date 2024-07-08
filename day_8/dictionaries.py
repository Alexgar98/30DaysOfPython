dog = {}

dog['name'] = 'Pipo'
dog['color'] = 'Black'
dog['breed'] = 'Chihuahua'
dog['legs'] = 4
dog['age'] = 3
print(dog)

student = {'first_name':'Pepe', 'last_name': 'Perez', 'gender':'Male', 'age':15, 'marital_status':'Single', 'skills':['Failing'], 'country':'Spain', 'city':'Motilla del Palancar', 'address':'Calle Falsa, 123'}
print(student)

print(len(student))

print(student['skills'])
print(type(student['skills']))

student['skills'].append('Lurking on internet')
student['skills'].append('Draining money')
print(student['skills'])

print(student.keys())
print(student.values())

print(student.items())

del student['marital_status']
print(student)

del dog