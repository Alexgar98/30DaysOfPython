#Level 1
empty = ()

brothers = ('Paco', 'Pepe', 'Anselmo', 'Godofredo') #kek
sisters = ('Maruja', 'Pepa', 'Lola', 'Rosi') #kek

siblings = brothers + sisters
print(siblings)

print(len(siblings))

family_members = list(siblings)
family_members.append('Juanito')
family_members.append('Juanita') #kek
family_members = tuple(family_members)
print(family_members)

#Level 2
print(family_members[-2:]) #Parents
print(family_members[0:-2]) #Siblings

fruits = ('Apple', 'Banana', 'Pear')
vegetables = ('Tomato', 'Lettuce', 'Onion')
animal_products = ('Cheese', 'Pork', 'Steak')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print(food_stuff_tp[(int)(len(food_stuff_tp) / 2)])

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)