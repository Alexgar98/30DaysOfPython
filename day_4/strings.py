thirty_days = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(thirty_days))

coding = ['Coding', 'For', 'All']
print(' '.join(coding))

company = "Coding For All"

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:]) #The other way is to split and join again without the first word

print(company.index('Coding'))
print(company.find("Coding"))

company = company.replace("Coding", "Python")
print(company)

every_python = "Python for Everyone"
print(every_python.replace("Everyone", "All"))

code = "Coding For All"
print(code.split(' '))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

print(code[0])

print(code.rindex(code[-1:]))

print(code[10])

python_everyone = 'Python For Everyone'
print(python_everyone[0:len(python_everyone):4]) #Sort of?

print(code[0:len(code):4])

print(code.index('C'))

print(code.index('F'))

all_people = "Coding For All People"
print(all_people.rindex('l'))

because = 'You cannot end a sentence with because because because is a conjunction'
print(because.index('because'))

print(because.rindex('because'))

print(because.replace('because because because ', '')) #Adding a space for aesthetic reasons

print(because.index('because')) #lol

print(because.replace('because because because ', '')) #Somebody messed this up and it wasn't me!

print(code.startswith("Coding"))

print(code.endswith("coding"))

spaces = '   Coding For All      '
print(spaces.strip(' '))

nbr = "30DaysOfPython"
thirty = "thirty_days_of_python"
print(nbr.isidentifier())
print(thirty.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(libraries).replace(' ', '/'))

challenge = "I am enjoying this challenge."
print(challenge.replace(' ', '\n'))
next = "I just wonder what is next."
print(next.replace(' ', '\n')) #Don't know if I understood the subject correctly here. Anyway

print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

radius = 10
pi = 3.14
area = 3.14 * radius ** 2
print("radius = {}".format(radius))
print("area = {} * radius ** 2".format(pi))
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area)) #Probably doing more than I should've

num_a = 8
num_b = 6
result = 8 + 6
print("{} + {} = {}".format(num_a, num_b, result))
result = 8 - 6
print("{} - {} = {}".format(num_a, num_b, result))
result = 8 * 6
print("{} * {} = {}".format(num_a, num_b, result))
result = 8 / 6
print("{} / {} = {:.2f}".format(num_a, num_b, result))
result = 8 % 6
print("{} % {} = {}".format(num_a, num_b, result))
result = 8 // 6
print("{} // {} = {}".format(num_a, num_b, result))
result = 8 ** 6
print("{} ** {} = {}".format(num_a, num_b, result))