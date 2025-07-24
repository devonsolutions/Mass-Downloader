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

    # replace with the link pattern, check for csustan.edu vs live-stan-state
    url = "https://csustan.edu/sites/default/files/2023-03/"
    file = file.replace(url, "")
    
    # d10: r"\d+|/" - removes numbers from the file name
    # d7: "/" - can be used when there's no numbers in the file name
    file = re.sub("/", "", file)
    file = file.replace("-", "")

    if response.status_code == 200:

        # replace with appropriate file path
        file_path = "/Users/jerynnecenario/Downloads/ABS"
        file = os.path.join(file_path, file)

        open(file, "wb").write(response.content)

        print("Downloaded: " + str(file))

    elif response.status_code == 404:
        print("404 Error: " + file)

    else:
       print(response.status_code + ": " + file)