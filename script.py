import requests
import re

# downloadedFiles = []

files = input("What files would you like to download? ").split()

filesTotal = len(files)

newDrupalFiles = 'https://www.csustan.edu/sites/default/files/'

for i in range(filesTotal):
    response = requests.get(files[i])
    if response.status_code == 200:

        # If the file is a D10 file, then terminal returns rewritten filepath
        if newDrupalFiles in files[i]:
            pattern = 'https://www.csustan.edu/sites/default/files/' + '[0-9]+' + '-' + '[0-9]+' + '/'
            string = files[i]
            repl = ''

            filePath = re.sub(pattern, repl, string)
            print(filePath)
        # If the file is not a D10 file, then terminal returns message
        else: 
            print('This file is not a D10 file.')

    else:
        print('File not found.')



'''
Accessing the file stored at the link address

response = requests.get(files[i])
file_Path = 'research_Paper_1.pdf'

if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
else:
    print('Failed to download file')'
'''


'''
MISCELLANEOUS

print(files[i])

print(" ".join(fileAddresses))

'''