import requests
import re
import certifi
import os

with open("scripts/input.txt", "r") as textFile:
    lines = textFile.readlines()

files = []

for line in lines:
    file = line.strip()
    files.append(file)

for file in files:

    response = requests.get(file, verify=certifi.where())

    url = "https://www.csustan.edu/sites/default/files/"
    file = file.replace(url, "")
    
    file = re.sub(r"\d+|/", "", file)
    file = file.replace("-", "")

    if response.status_code == 200:

        file_path = "\\Users\\Work Account\\Downloads\\"
        file = os.path.join(file_path, file)

        open(file, "wb").write(response.content)

        print("Downloaded: " + str(file))

    elif response.status_code == 404:
        print("404 Error: " + file)

    else:
       print(response.status_code + ": " + file)