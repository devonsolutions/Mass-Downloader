import requests
import re

files = input("What files would you like to download? ").split("https://")

fullnameFiles = []

for file in files:
    renamedFile = "https://" + file
    fullnameFiles.append(renamedFile)

# Need to delete b/c the first element is an invalid URL
del fullnameFiles[0]

for fullnameFile in fullnameFiles:

    response = requests.get(fullnameFile)

    if response.status_code == 200 or 403:
       # print(fullnameFile)
       pass

    else:
       # print("File not available")
       pass