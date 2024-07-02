#Level 1
#Day 2: 30 Days of python programming

first_name = 'Alex'
last_name = 'Garcia'
full_name = 'Alex Garcia'
country = 'Spain'
city = 'Malaga'
age = 25
year = 1998
is_married = False
is_true = True
is_light_on = False
github, repositories, forty_two = 'Alexgar98', 27, 42.0

#Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(github))
print(type(repositories))
print(type(forty_two))

print(len(first_name))

print(max(len(first_name), len(last_name))) #Subject was kinda ambiguous so I just slapped in the max between both lengths

num_one = 5
num_two = 4
total = num_one + num_two
print(total) #I'm just gonna print all of this so everything is fine
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

radius = 30
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
new_radius = int(input("Give me the radius "))
new_area = 3.14 * (new_radius ** 2)
new_circum = 2 * 3.14 * new_radius
print(new_area)
print(new_circum)

new_first_name = input("Give me your first name ")
new_last_name = input("Give me your last name ")
new_country = input("Give me your country ")
new_age = int(input("Give me your age "))
print(new_first_name)
print(new_last_name)
print(new_country)
print(new_age)

help('keywords')