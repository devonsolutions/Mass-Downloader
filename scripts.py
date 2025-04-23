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

    response = requests.get(fullnameFile, verify=False)

    if response.status_code == 200 or 403:

        # Maybe add another ifelse statement so that we can download status code [200] Drupal7 files, as well

        pattern = "https://www.csustan.edu/sites/default/files/" + '[0-9]+' + '-' + '[0-9]+' + '/'
        repl = ''
        removeURL = re.sub(pattern, repl, fullnameFile)
        filePath = "Downloads" + str("/") + removeURL

        open(filePath, "wb").write(response.content)

        print(str(filePath) + "has been downloaded.")

    else:
       print("File not available")