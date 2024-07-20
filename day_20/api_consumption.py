import re
import requests
import numpy #I'm not calculling standard deviations manually ever again
import pandas #For frequency table

'''romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet)
txt = response.text
cleaned = re.sub(r'[^a-zA-Z ]', '', txt)
split = re.split(' ', cleaned)
dictionary = {}
for word in split:
    if word in dictionary:
        dictionary[word] += 1
    elif len(word) > 0: #Regex might need a fix but I'm not doing it today
        dictionary[word] = 1
word_list = [(count, word) for word, count in dictionary.items()]
word_list.sort(reverse=True)
print(word_list[0:10])'''
#Throws 404, oops! Commenting it out

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats = response.json()
weights = []
lifespans = []
for cat in cats:
    weights.append(cat['weight']['metric'])
    lifespans.append(cat['life_span'])
cleaned_weights = []
cleaned_lifespans = []
for weight in weights:
    to_append = re.findall(r'\d+', weight)
    for number in to_append:
        cleaned_weights.append(number)
cleaned_weights = [int(number) for number in cleaned_weights]
for lifespan in lifespans:
    to_append = re.findall(r'\d+', lifespan)
    for number in to_append:
        cleaned_lifespans.append(number)
cleaned_lifespans = [int(number) for number in cleaned_lifespans]
print("Min weight is", min(cleaned_weights))
print("Max weight is", max(cleaned_weights))
print("Mean weight is", numpy.mean(cleaned_weights))
print("Standard variation of weights is", numpy.std(cleaned_weights))
print("Min lifespan is", min(cleaned_lifespans))
print("Max lifespan is", max(cleaned_lifespans))
print("Mean lifespan is", numpy.mean(cleaned_lifespans))
print("Standard variation of lifespans is", numpy.std(cleaned_lifespans))
dataframe = pandas.DataFrame(cats)
frequency_table = dataframe[['name', 'origin']]
frequency_table.columns = ['Breed', 'Country']
print(frequency_table)

#The countries API throws 404 error. If it worked, it would be the same way of reading the URL then get the data the same way I've done countless times before in this challenge

#The UCI page is also down lol. What an absolute disaster of this day's tasks