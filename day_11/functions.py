#Level 1
from math import sqrt


def add_two_numbers(first, second):
    return first + second

def area_of_circle(radius):
    return 3.14 * radius * radius

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if not type(num) == int:
            return "Found something that isn't a number"
        else:
            sum += num
    return sum

def convert_celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
        return 'Autumn'
    elif month == 'December' or month == 'January' or month == 'February':
        return 'Winter'
    elif month == 'March' or month == 'April' or month == 'May':
        return 'Spring'
    elif month == 'June' or month == 'July' or month == 'August':
        return 'Summer'
    else:
        return "Invalid month"
    
def calculate_slope(point_a, point_b):
    return (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])

def solve_quadratic_eqn(a,b,c):
    return ((-b + sqrt(b**2 - 4*a*c))/ (2*a), (-b - sqrt(b**2 - 4*a*c))/ (2*a))

def print_list(list):
    for element in list:
        print(element)

def reverse_list(list):
    to_return = []
    count = -1
    while not list[count] == list[0]:
        to_return.append(list[count])
        count -= 1
    to_return.append(list[count])
    return to_return

def capitalize_list_items(list):
    to_return = []
    for element in list:
        to_return.append(element.upper())
    return to_return

def add_item(list, item):
    list.append(item)
    return list

def remove_item(list, item):
    list.remove(item)
    return list

def sum_of_numbers(num):
    to_return = 0
    for number in range(num + 1):
        to_return += number
    return to_return

def sum_of_odds(num):
    to_return = 0
    for number in range(num + 1):
        if (number % 2 == 1):
            to_return += number
    return to_return

def sum_of_even(num):
    to_return = 0
    for number in range(num + 1):
        if (number % 2 == 0):
            to_return += number
    return to_return

#Level 2
def evens_and_odds(num):
    evens = 0
    odds = 0
    for number in range(num + 1):
        if (number % 2 == 0):
            evens += 1
        else:
            odds += 1
    return "The number of odds is {}.\nThe number of evens is {}.".format(odds, evens)

def factorial(num):
    if num < 0:
        return "Could not do this"
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1) #Recursivity!
    
def is_empty(param):
    return len(param) == 0 #Boolean results in one line!

def calculate_mean(list):
    sum = 0
    for element in list:
        sum += element
    return sum / len(list)

def calculate_median(list):
    ordered = sorted(list)
    if len(list) % 2 == 0:
        return (ordered[(int) (len(ordered) / 2)] + ordered[(int)(len(list) / 2 + 1)]) / 2
    else:
        return ordered[(int) (len(list) / 2 + 1)]
    
def calculate_mode(list):
    dict = {}
    for element in list:
        if not element in dict.keys():
            dict[element] = 1
        else:
            dict[element] += 1
    sorted_dict = sorted(dict.items(), reverse=True, key=lambda x: x[1])
    return sorted_dict[0][0]

def calculate_range(list):
    return (min(list), max(list))

def calculate_variance(list):
    sum = 0
    for element in list:
        sum += (element - calculate_mean(list)) ** 2
    return sum / (len(list) - 1)

def calculate_std(list):
    return sqrt(calculate_variance(list))

#Level 3
def is_prime(nbr):
    for number in range(1, (int)(nbr / 2)): #No need to check beyond half the number
        if nbr % number == 0 and not number == 1 and not nbr == 2:
            return False
    return True

def all_unique(list):
    i = 0
    j = 0
    while i < len(list):
        while j < len(list):
            if list[i] == list[j] and not i == j:
                return False
            j += 1
        i += 1
    return True

def same_type(list):
    i = 0
    j = 0
    while i < len(list):
        while j < len(list):
            if type(list[i]) != type(list[j]) and not i == j:
                return False
            j += 1
        i += 1
    return True

def valid_variable(variable):
    return variable.isidentifier() #Was about to overcomplicate this

#Oh damn...

print(valid_variable('a123'))