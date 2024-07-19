import re
import json
import csv

def count_lines(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    return len(lines)
def count_words(file):
    f = open(file)
    txt = f.read()
    cleaned = re.sub(r'[^a-zA-Z ]', '', txt)
    split = re.split(' ', cleaned)
    f.close()
    return len(split)
print(count_lines('./data/obama_speech.txt'))
print(count_words("./data/obama_speech.txt"))
print(count_lines('./data/michelle_obama_speech.txt'))
print(count_words("./data/michelle_obama_speech.txt"))
print(count_lines('./data/donald_speech.txt'))
print(count_words("./data/donald_speech.txt"))
print(count_lines('./data/melina_trump_speech.txt'))
print(count_words("./data/melina_trump_speech.txt"))

def most_spoken_languages(file, nbr):
    f = open(file, encoding='utf8')
    file_json = f.read()
    dictionary = json.loads(file_json)
    language_dict = {}
    for element in dictionary:
        for language in element['languages']:
            if language in language_dict:
                language_dict[language] += 1
            else:
                language_dict[language] = 1
    language_list = [(count, language) for language, count in language_dict.items()]
    language_list.sort(reverse=True)
    f.close()
    return language_list[0:nbr]
print(most_spoken_languages("./data/countries_data.json", 10))

def most_populated_countries(file, nbr):
    f = open(file, encoding='utf8')
    file_json = f.read()
    dictionary = json.loads(file_json)
    population_list = [{'country' : country['name'], 'population' : country['population']} for country in dictionary]
    population_list.sort(reverse=True, key=lambda x : x['population'])
    f.close()
    return population_list[0:nbr]
print(most_populated_countries("./data/countries_data.json", 10))

def addresses(file):
    f = open(file)
    txt = f.read()
    pattern = r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+' #Assuming an address looks like 'something@something'. Which may be too much assumption but anyway
    address_list = re.findall(pattern, txt)
    unique_addresses = []
    for address in address_list:
        if not address in unique_addresses:
            unique_addresses.append(address)
    f.close()
    return unique_addresses
#print(addresses("./data/email_exchanges_big.txt")) #I'm commenting this out to not become even more crazy

def find_most_common_words(file, nbr):
    f = open(file)
    txt = f.read()
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
    f.close()
    return word_list[0:nbr]

print(find_most_common_words("./data/obama_speech.txt", 10))
print(find_most_common_words("./data/michelle_obama_speech.txt", 10))
print(find_most_common_words("./data/donald_speech.txt", 10))
print(find_most_common_words("./data/melina_trump_speech.txt", 10))

def check_text_similarity(txt_a, txt_b):
    def clean_text(txt):
        try:
            f = open(txt)
            read_text = f.read()
            cleaned = re.sub(r'[^a-zA-Z ]', '', read_text)
        except:
            cleaned = re.sub(r'[^a-zA-Z ]', '', txt)
        finally:
            return re.split(' ', cleaned)
    def delete_stop_words(txt):
        stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        cleaned_text = []
        for word in txt:
            if not word.lower() in stop_words:
                cleaned_text.append(word)
        return cleaned_text
    def word_count(txt):
        dictionary = {}
        for word in txt:
            if word in dictionary:
                dictionary[word] += 1
            elif len(word) > 0: #Regex might need a fix but I'm not doing it today. Yup, this is also copied from above C:
                dictionary[word] = 1
        word_list = [(count, word) for word, count in dictionary.items()]
        word_list.sort(reverse=True)
        return word_list
    cleaned_a = delete_stop_words(clean_text(txt_a))
    cleaned_b = delete_stop_words(clean_text(txt_b))
    count_a = word_count(cleaned_a)[0:100]
    count_b = word_count(cleaned_b)[0:100]
    coincidences = 0
    for word_a in count_a:
        for word_b in count_b:
            if word_a[1] == word_b[1]:
                coincidences += 1
                break
    return "There are {} coincidences in the 100 most used words by both texts".format(coincidences) #I would like to have an example on what exactly was the objective of this task. I'm doing whatever here

print(check_text_similarity("./data/michelle_obama_speech.txt", "./data/melina_trump_speech.txt"))

print(find_most_common_words("./data/romeo_and_juliet.txt", 10))

hacker_news = "./data/hacker_news.csv"
with open(hacker_news) as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    python_lines = 0
    js_lines = 0
    java_lines = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            title = row[1].lower()
            if 'python' in title:
                python_lines += 1
            elif 'javascript' in title:
                js_lines += 1
            elif 'java' in title:
                java_lines += 1
    print("Lines with Python: {}".format(python_lines))
    print("Lines with JS: {}".format(js_lines))
    print("Lines with Java: {}".format(java_lines))
    f.close()