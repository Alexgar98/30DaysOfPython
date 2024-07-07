# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Level 1
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Yahoo', 'Adobe'])
print(it_companies)

it_companies.discard('asdasd') #Testing discard with an item which doesn't exist. Will not do this with remove
it_companies.discard('Yahoo')
print(it_companies)

#Level 2
joint = A.union(B)
print(joint)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B

#Level 3
set_ages = set(age)
print(set_ages)
print(len(age))
print(len(set_ages))

#Strings are just chains of characters; the rest are collections of any type of data. Lists are ordered and modifiable; tuples are ordered but immutable; and sets are unordered and immutable

teacher = "I am a teacher and I love to inspire and teach people"
teacher_list = teacher.split()
teacher_set = set(teacher_list)
print(len(teacher_set))