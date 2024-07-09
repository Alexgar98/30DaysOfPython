#Level 1
"""age = (int) (input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need {} more years to learn to drive.".format(18 - age))

my_age = 25
your_age = (int) (input("Enter your age: "))
if my_age > your_age:
    if my_age - your_age == 1:
        print("I am 1 year older than you")
    else:
        print("I am {} years older than you".format(my_age - your_age))
elif my_age < your_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me")
    else:
        print("You are {} years older than me".format(your_age - my_age))
else:
    print("We have the same age")

one = (int) (input("Enter number one: "))
two = (int) (input("Enter number two: "))
if one > two:
    print("{} is greater than {}".format(one, two))
elif one == two:
    print("{} is equal to {}".format(one, two))
else:
    print("{} is smaller than {}".format(one, two))

#Level 2
score = (int) (input("Enter the score: "))
if score >= 0 and score < 50:
    print("F")
elif score >= 50 and score < 60:
    print("D")
elif score >= 60 and score < 70:
    print("C")
elif score >= 70 and score < 90:
    print("B")
elif score >= 90 and score <= 100: #There is a typo in the subject I guess
    print("A")
else:
    print("Invalid score")

month = input("Enter the month: ")
if month == "September" or month == "October" or month == "November":
    print("Autumn")
elif month == "December" or month == "January" or month == "February":
    print("Winter")
elif month == "March" or month == "April" or month == "May":
    print("Spring")
elif month == "June" or month == "July" or month == "August":
    print("Summer")
else:
    print("Invalid month")

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a new fruit: ")
if not new_fruit in fruits:
    fruits.append(new_fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')"""

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True, #There was a typo here
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person.keys():
    print(person['skills'][(int)(len(person['skills']) / 2)])
    if 'Python' in person['skills']:
        print("This person knows Python!")
    else:
        print("This person doesn't know Python...")
    #I think I didn't understand well this part of the subject
    if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    elif len(person['skills']) == 3 and 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')
if person['is_married'] and person['country'] == 'Finland':
    print("{} {} lives in Finland. He is married".format(person['first_name'], person['last_name']))