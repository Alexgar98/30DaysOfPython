import math

my_age = 25

my_height = 1.90

nbr = 1+1j #Declaring some random complex because there's no way to declare an uninitialized variable

base = (int) (input("Enter base: "))
height = (int) (input("Enter height: "))
print("The area of the triangle is", 0.5*base*height)

a = (int) (input("Enter side a: "))
b = (int) (input("Enter side b: "))
c = (int) (input("Enter side c: "))
print("The perimeter of the triangle is", a+b+c)

rect_length = (int) (input("Enter the length: "))
rect_width = (int) (input("Enter the width: "))
print("The area of the rectangle is", rect_length * rect_width)
print("The perimeter of the rectangle is", 2 * (rect_length + rect_width))

radius = (int) (input("Enter the radius: "))
print("The area of the circle is", 3.14 * (radius ** 2))
print("The circumference of the circle is", 2 * 3.14 * radius)

x_a = 1
x_b = 2
y_a = 2 * x_a - 2
y_b = 2 * x_b - 2
slope_a = (y_a - y_b) / (x_a - x_b)
print(slope_a)
x_intercept = (0 + 2) / 2
print(x_intercept)
y_intercept = 2 * 0 - 2
print(y_intercept)
#What a pain, lol

slope_b = (10 - 2) / (6 - 2)
print(slope_b)
distance = math.sqrt((2-6)**2 + (2-10)**2)
print(distance)

print("The first slope was bigger than the second slope:", slope_a > slope_b)
print("The first slope was smaller than the second slope:", slope_a < slope_b)
print("The first slope was equal to the second slope:", slope_a == slope_b)

#Never thought quadratic equations were going to be useful
solution = (-6 + math.sqrt((6 ** 2) - (4*1*9)))/ (2 * 1)
print(solution)

len_python = len("python")
len_dragon = len("dragon") #Hic sunt dracones!
print(len_dragon > len_python)

print("on" in "python" and "on" in "dragon")

print("jargon" in "I hope this course is not full of jargon")

print("on" not in "python" and "on" not in "dragon")

#Length already found before as len_python
len_pyfloat = (float) (len_python)
len_pystring = (str) (len_pyfloat)
print(len_pystring)

even = (int) (input("Introduce a number: "))
print("The number is even:", even % 2 == 0)

print((7 // 3) == (int)(2.7))

print(type('10') == type(10))

print(int(9.8) == 10) #int('9.8') crashes

hours = (int) (input("Enter hours: "))
rate = (int) (input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate)

years = int (input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds")

row = 1
print(row, row ** 0, row ** 1, row ** 2, row **3)
row += 1
print(row, row ** 0, row ** 1, row ** 2, row **3)
row += 1
print(row, row ** 0, row ** 1, row ** 2, row **3)
row += 1
print(row, row ** 0, row ** 1, row ** 2, row **3)
row += 1
print(row, row ** 0, row ** 1, row ** 2, row **3)
#Would've normally used a loop for this