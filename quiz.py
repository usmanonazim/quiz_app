#TODO Build a trivia app -- jservice.io
#selection a

import requests
import string
import nltk
import math
from random import *

random_category = str(randint(1,100))
response = requests.get("http://jservice.io/api/category?id=" + random_category)

clues = response.json()['clues']

for clue in clues:
    print(clue['question'])


category_name = response.json()['title']

#convert the category name to a title (uppercase for the first letter of each word)
category_name = string.capwords(category_name)

question = response.json()['clues'][0]['question']


actual_answer = response.json()['clues'][0]['answer']
print("The category you have chosen is: " + category_name)
print("Question: " + question)

user_answer = input("Answer: ")
user_answer = user_answer.lower().lstrip().rstrip()  # strip whitespace and make lower

# if the edit distance is < than 1/4 of the length of the actual answer - user answer is correct

if nltk.edit_distance(user_answer, actual_answer.lower()) < math.ceil(1/4*len(actual_answer)):
    print("Correct!")
else:
    print("Incorrect! The correct answer was: " + actual_answer)




