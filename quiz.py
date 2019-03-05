# TODO Build a trivia app -- jservice.io

import requests
import string
import nltk
import math
from random import *

#random_category = str(randint(1, 100))

# US States - 17
# 3 letter words - 105
# The Bible - 31
#Science - 25
#Food - 49


category_list = {'1': '17',
                 '2': '105',
                 '3': '31',
                 '4': '25',
                 '5': '49'
                 }

print("Categories: ")
print("1: US States")
print("2: 3 letter words\n3: The Bible\n4: Science\n5: Food")

choice = input("Choose a category: ").lstrip().rstrip()


response = requests.get(
    "http://jservice.io/api/category?id=" + category_list[choice])


clues = response.json()['clues']
category_name = response.json()['title']
# convert the category name to a title (uppercase for the first letter of each word)
category_name = string.capwords(category_name)
print("The current category is: " + category_name)
for i in clues:
    if i['value'] != None:
        actual_answer = i['answer']
        print("\nQuestion: " + i['question'])
        user_answer = input("Answer: ")
        user_answer = user_answer.lower().lstrip().rstrip()
        # if the edit distance is < than 1/4 of the length of the actual answer - user answer is correct
        if nltk.edit_distance(user_answer, actual_answer.lower()) < math.ceil(1/4*len(actual_answer)):
            print("Correct!")
        else:
            print("Incorrect! The correct answer was: " + actual_answer + "\n")

        print("\nWould you like another question?")
        user = input("Yes or No: ")
        user = user.lstrip().rstrip().lower()

        if user == "no":
            break
