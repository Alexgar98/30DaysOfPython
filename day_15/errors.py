#print 'hello world' #SyntaxError
print ('hello world')

#print(age) #NameError
age = 25
print(age)

numbers = [1,2,3,4,5]
#print(numbers[5]) #IndexError

#import maths #ModuleNotFoundError
import math

#print(math.PI) #AttributeError
print(math.pi)

users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])
#print(users['county']) #KeyError
print(users['country'])

#print(4 + '3') #TypeError
print(4 + int('3'))

#from math import power #ImportError
from math import pow
print(pow(2,3))

#print(int('12a')) #ValueError
print(int('12'))

#print(1/0) #ZeroDivisionError
print(1/1)