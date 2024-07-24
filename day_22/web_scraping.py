import requests
from bs4 import BeautifulSoup
import json
import re

'''url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
items = soup.find_all('ul', class_='custom-stat-list')
data = dict()
for item in items:
    labels = item.find_all('span', 'stat-label')
    figures = item.find_all('span', 'stat-figure')
    i = 0
    while (i < len(labels)):
        data[labels[i].text] = figures[i].text
        i += 1
with open("boston.json", "w") as outfile:
    json.dump(data, outfile)'''

#Exercise 2 is down :(

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
labels = soup.find_all('th', {'scope' : 'col'})
cleaned_labels = [label.text.strip('\n') for label in labels]
cleaned_labels = cleaned_labels[0:-3]
pattern_to_drop = r'\[[a-z0-9]+\]'
neat_labels = [re.sub(pattern_to_drop, '', label) for label in cleaned_labels] #['No.', 'Portrait' (0, 8...), 'Name(Birth–Death)' (1), 'Term' (2), 'Party' (4), 'Election' (5), 'Vice President'(6)]
rows = soup.find_all('td')
#cleaned_rows = [row.text.strip('\n') for row in rows]
#print(rows[0].text)
presidents = []

#TODO THIS EXERCISE IS A HELL AND I'M TWO DAYS BEHIND WHEN I'M WRITING THIS, THERE'S NO WAY I'M FINISHING THIS IF I WANT TO END THE CHALLENGE IN TIME