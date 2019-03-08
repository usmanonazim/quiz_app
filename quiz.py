# TODO Build a trivia app -- jservice.io

import requests
import string
import nltk
import math
from random import *
import random
import re
import turtle

# random_category = str(randint(1, 100))

# US States - 17
# 3 letter words - 105
# The Bible - 31
# Science - 25
# Food - 49
# food and drink - 253


category_list = {'1': '17',
                 '2': '105',
                 '3': '31',
                 '4': '25',
                 '5': '49',
                 '6': '253',
                 '7': '223',
                 '8': '139',
                 '9': '582'
                 }


# fix the random number generator seed
random.seed(10)
p = re.compile(r"[^a-z\d]", re.IGNORECASE)
playing = True
numbers = []


def is_duplicate(numbers,  x):
    for i in range(len(numbers)):
        if numbers[i] == x:
            return True
    return False


while playing:
    # clear the list of numbers each time a category is picked
    numbers.clear()
    print("\nPick a Category: ")
    print("1: US States")
    print("2: 3 letter words\n3: The Bible\n4: Science\n5: Food\n6: Food and Drink\n7: Word Origins\n8: 5 Letter Words\n9: US Geography")

    choice = input("Choose a category: ").lstrip().rstrip()
    response = requests.get(
        "http://jservice.io/api/category?id=" + category_list[choice])
    clues = response.json()['clues']
    category_name = response.json()['title']
    # convert the category name to a title (uppercase for the first letter of each word)
    category_name = string.capwords(category_name)
    print("\nThe current category is: " + category_name)

    while True:
        i = random.randint(0, len(clues))
        if (is_duplicate(numbers, i) == False) and clues[i]['value'] != None and len(clues[i]['question']) > 3:
            numbers.append(i)
            actual_answer = clues[i]['answer']
            ans = re.sub(p, '', actual_answer.lower())
            print("\nQuestion: " + clues[i]['question'])
            user_answer = input("Answer: ")
            uans = re.sub(p, '', user_answer.lower())

            # if the edit distance is < than 1/4 of the length of the actual answer - user answer is correct
            if nltk.edit_distance(uans, ans) <= math.ceil(1/4*len(ans)):
                print("Correct! \nThe answer was: " + actual_answer)
            else:
                print("Incorrect! \nYour answer was: " + user_answer +
                      " \nBut the correct answer was: " + actual_answer)

            print("\n1: Try Another Question\n2: Quit\n3: Change Category")
            user = input()
            user = user.lstrip().rstrip().lower()

            if user == "2":
                playing = False
                print("Thank you for playing")
                break
            elif user == "3":
                break
            elif user != "1":
                playing = False
                break
