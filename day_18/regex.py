import re

#Level 1
"""paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
word_list = []
split_paragraph = re.findall(r'\b\w+\b', paragraph)
cleaned_paragraph = ''
for word in split_paragraph:
    cleaned_paragraph += (word + ' ')
for word in split_paragraph:
    pattern = '\\b' + word + '\\b'
    matches = re.findall(pattern, cleaned_paragraph)
    to_include = (len(matches), word)
    if not to_include in word_list:
        word_list.append(to_include)
word_list.sort(reverse=True)
print(word_list)"""

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
pattern = r'-?\d+\b'
points = re.findall(pattern, text)
print(points)
sorted_points = [int(point) for point in points]
sorted_points.sort() #Just in case
print(sorted_points)
distance = sorted_points[-1] - sorted_points[0]
print(distance)

#Level 2
def is_valid_variable(name):
    pattern = r'^[a-z][A-Za-z0-9_]+$'
    match = re.findall(pattern, name)
    return len(match) > 0

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

#Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(text):
    cleaned = re.sub(r'[^a-zA-Z ]', '', text)
    return cleaned
def most_frequent_words(text):
    word_list = []
    split_text = re.split(' ', text)
    for word in split_text:
        pattern = '\\b' + word + '\\b'
        matches = re.findall(pattern, text)
        to_include = (len(matches), word)
        if not to_include in word_list:
            word_list.append(to_include)
    word_list.sort(reverse=True)
    most_frequent = word_list[0:3]
    return most_frequent
cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))