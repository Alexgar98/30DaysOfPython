#Level 1
from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#map iterates over a list and does something; filter checks a boolean condition over the list and reduce returns a single value

#A higher order function is a function that returns another function or takes another function as a parameter; a closure is a nested function which is returned by the main function and a decorator is a function that is applied to an object

plus_one = map(lambda x : x + 1, numbers)
print(list(plus_one))
great_numbers = filter(lambda x : x > 5, numbers)
print(list(great_numbers))
def sum_numbers(a, b):
    return a + b
sum_all = reduce(sum_numbers, numbers)
print(sum_all)

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

#Level 2
upper_countries = map(lambda x : x.upper(), countries)
print(list(upper_countries))

square_numbers = map(lambda x : x **2, numbers)
print(list(square_numbers))

upper_names = map(lambda x : x.upper(), names)
print(list(upper_names))

land_countries = filter(lambda x : 'land' in x, countries)
print(list(land_countries))

six_countries = filter(lambda x : len(x) == 6, countries)
print(list(six_countries))

long_countries = filter(lambda x : len(x) >= 6, countries)
print(list(long_countries))

e_countries = filter(lambda x : x[0] == 'E', countries)
print(list(e_countries))

cap_land = map(lambda x : x.upper(), filter(lambda x : 'land' in x, countries))
print(list(cap_land))

def get_string_list(lst):
    return list(filter(lambda x : type(x) == str, lst))

print(get_string_list([1,2,3,4,'Holiwi','Pruebo cosas', 1,2,3,4]))

#I've already done task 10 in level 1. Not repeating it again.

def concat(a, b):
    return a + ', ' + b
reduced = reduce(concat, countries)
print("{} are north European countries".format(reduced))

#Welp. Going back to the damn long files C: