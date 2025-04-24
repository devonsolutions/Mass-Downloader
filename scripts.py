import requests
import re
import certifi

files = input("What files would you like to download? ").split("https://")

fullnameFiles = []

for file in files:
    renamedFile = "https://" + file
    fullnameFiles.append(renamedFile)

# Need to delete b/c the first element is an invalid URL
del fullnameFiles[0]

for fullnameFile in fullnameFiles:

    response = requests.get(fullnameFile, verify=certifi.where())

    if response.status_code == 200:

        if "/sites/default/files" and ".pdf" in fullnameFile:

            # Maybe add another ifelse statement so that we can download status code [200] Drupal7 files, as well

            pattern = "https://www.csustan.edu/sites/default/files/" + '[0-9]+' + '-' + '[0-9]+' + '/'
            repl = ''
            removeURL = re.sub(pattern, repl, fullnameFile)
            filePath = "Downloads" + str("/") + removeURL

            open(filePath, "wb").write(response.content)

            print(str(filePath) + "has been downloaded.")
        
        elif ".xlsx" in fullnameFile:
            # Maybe add another ifelse statement so that we can download status code [200] Drupal7 files, as well

            pattern = "https://www.csustan.edu/sites/default/files/" + '[0-9]+' + '-' + '[0-9]+' + '/'
            repl = ''
            removeURL = re.sub(pattern, repl, fullnameFile)
            filePath = "Downloads" + str("/") + removeURL

            open(filePath, "wb").write(response.content)

            print(str(filePath) + "has been downloaded.")

        else:
            print("This webpage returns a status code of 200, but isn't a D10 spreadsheet or pdf.")

    elif response.status_code == 404:
        print("This file is not available.")

    else:
       print("This is the page's status code: " + response.status_code)

'''
https://www.csustan.edu/sites/default/files/2023-01/new-standard-room-use-final.pdf
https://www.csustan.edu/sites/default/files/2023-01/faculty-resources-flyer.pdf
https://www.csustan.edu/sites/default/files/2023-01/sharelinkpro-flyer.pdf
https://www.csustan.edu/sites/default/files/2023-01/standard-room-use-flyer.pdf

'''