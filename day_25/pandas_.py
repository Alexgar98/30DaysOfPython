import pandas as pd
import numpy as np

df = pd.read_csv('hacker_news.csv')
print(df)

head = df.head()
print(head)

tail = df.tail()
print(tail)

titles = df['title']
print(titles)

shape = df.shape
print("There are", shape[0], "rows and", shape[1], "columns")

py_titles = [title for title in titles if 'python' in title.lower()]
print(len(py_titles))

js_titles = [title for title in titles if 'javascript' in title.lower()]
print(len(js_titles))