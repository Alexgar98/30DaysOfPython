#Level 1
numbers = [0,1,2,3,4,5,6,7,8,9,10] #Pain
for number in numbers:
    print(number)
count = 0
while count <= 10:
    print(count)
    count += 1

numbers = [10,9,8,7,6,5,4,3,2,1,0] #PAIN
for number in numbers:
    print(number)
count = 10
while count >= 0:
    print(count)
    count -= 1

hashtag = 1
to_print = "#"
while hashtag <= 7:
    print(to_print)
    hashtag += 1
    to_print += "#"

i = 0
j = 0
to_print = ""
while i < 8:
    while j < 8:
        to_print += "# "
        j += 1
    print(to_print)
    i += 1
    j = 0
    to_print = ""

numbers = [0,1,2,3,4,5,6,7,8,9,10] #PAAAIN
for number in numbers:
    print("{} x {} = {}".format(number, number, number * number))

languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in languages:
    print(language)

count = 0
while count <= 100:
    print(count)
    count += 2 #I think the spirit was to nest a conditional here but this is more efficient and I'll stick to it

count = 1
while count <= 100:
    print(count)
    count += 2 #I mean, nobody is correcting me like in 42 (?)

#Level 2
sum = 0
for number in range(101): #I realised just now that I could've used range() before lol
    sum += number
else:
    print("The sum of all numbers is {}.".format(sum))

evens = 0
odds = 0
for number in range(101):
    if number % 2 == 0:
        evens += number
    else:
        odds += number
else:
    print("The sum of all evens is {}. And the sum of all odds is {}.".format(evens, odds))

#Level 3
#I refuse to paste this thing again so I'll just use countries.py instead

fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in range(len(fruits) - 1, -1, -1):
    print(fruits[fruit]) #Nobody told me to create another list

#How could you possibly create an even more unpastable file!? Jeez