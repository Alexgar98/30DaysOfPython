numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives = [i for i in numbers if i <= 0]
print(negatives)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [number for row in list_of_lists for number in row]
complete_flatten = [number for row in flattened for number in row] #I have the feeling I could've done this in a single line but it was going to be chaos
print(complete_flatten)

tuple_list = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(tuple_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened = [[i[0][0].upper(), i[0][0].upper()[0:3], i[0][1].upper()] for i in countries]
print(flattened)

#Same list; not copying it again
dict_list = [{'country': i[0][0].upper(), 'city' : i[0][1].upper()} for i in countries]
print(dict_list)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_list = [i[0][0] + ' ' + i[0][1] for i in names]
print(name_list)

slope = lambda a, b : (b[1] - a[1]) / (b[0] - a[0])
print(slope((2,1), (3,0)))
y_intercept = lambda a : (0, a[1])
print(y_intercept((3, 1)))