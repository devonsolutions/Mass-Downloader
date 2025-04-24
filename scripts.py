import requests
import re
import certifi
from os import listdir
from os.path import isfile, join
import os
import shutil

# add file path to downloads folder
# filePath = 'D:\Downloads'

with open("input.txt", "r") as textFile:
    lines = textFile.readlines()

files = []

for line in lines:
    file = line.strip()
    files.append(file)

for file in files:

    response = requests.get(file, verify=certifi.where())

    if response.status_code == 200:

        pattern = "https://www.csustan.edu/sites/default/files/" + '[0-9]+' + '-' + '[0-9]+' + '/'
        repl = ''
        removeURL = re.sub(pattern, repl, file)
        fileName = removeURL

        open(fileName, "wb").write(response.content)

        print(str(fileName) + "has been downloaded.")

    elif response.status_code == 404:
        print("This file is not available.")

    else:
       print("This is the page's status code: " + response.status_code)

"""
# Works on media that begins with the patterns listed below

        drupalPattern = "https://www.csustan.edu/sites/default/files/"

        if drupalPattern in file:

            d10Pattern = '[0-9]+' + '-' + '[0-9]+' + '/'

            if d10Pattern in file: 
                pattern = "https://www.csustan.edu/sites/default/files/" + '[0-9]+' + '-' + '[0-9]+' + '/'
                repl = ''
                removeURL = re.sub(pattern, repl, file)
                fileName = removeURL

                open(fileName, "wb").write(response.content)

                print(str(fileName) + "has been downloaded.")

            else:
                pattern = "https://www.csustan.edu/sites/default/files/"
                repl = ''
                removeURL = re.sub(pattern, repl, file)
                fileName = removeURL

                open(fileName, "wb").write(response.content)

                print(str(fileName) + "has been downloaded.")

        else:
            print("This page returns the status code 200, but is not a D7 or D10 page.")


check for matching patterns

string = "your_string_here"
match = re.search(pattern, string)
if match:
    # Pattern found
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())
    print("Matched string:", match.group())
else:
    # Pattern not found
    print("Match not found.")

"""