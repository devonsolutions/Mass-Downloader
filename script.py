import requests
import re

# need to fix input format (need to split input to add separate links as seperate items in the list)
# links only register as individual items when separated by a space

files = input("What files would you like to download? ")

filesTotal = len(files)

drupalFiles = 'https://www.csustan.edu/sites/default/files/'

sharepointFiles = 'https://csustan.sharepoint.com/:b:/s/StanStatePublicDocs/'

for i in range(filesTotal):

    response = requests.get(filesTotal[i])

    # If requested page has been fetched, then the program will determine if the file is a Drupal 10, SharePoint, or other type of file
    if response.status_code == 200:

        print(filesTotal[i])
        '''
        # If the file is a Drupal 10 file, then the file will be downloaded
        if drupalFiles in files[i]:
            
            pattern = 'https://www.csustan.edu/sites/default/files/' + '[0-9]+' + '-' + '[0-9]+' + '/'
            string = files[i]
            repl = ''

            filePath = re.sub(pattern, repl, string)

            with open(filePath, 'wb') as file:
                file.write(response.content)
            
            print(str(filePath) + "has been downloaded.")
        # If the file is a SharePoint file, then the file will be downloaded
        else: 
            print("Not a Drupal file")
        '''

    # If the requested page returns a different HTTP status code, then the terminal returns message
    # Drupal 7 files will return this message
    else:
        print('File not found.')

'''

indvFiles = re.findall("https://", files)

# drupalFiles = 'https://www.csustan.edu/sites/default/files/'

for indvFile in indvFiles:
    response = requests.get(indvFile)

    # If requested page has been fetched, then the program will determine if the file is a Drupal 10, SharePoint, or other type of file
    if response.status_code == 200:

        print(indvFile)

        # If the file is a Drupal 10 file, then the file will be downloaded
        if 'sites/default/files/' in files:

            print("This is a Drupal file")

            
            pattern = 'https://www.csustan.edu/sites/default/files/' + '[0-9]+' + '-' + '[0-9]+' + '/'
            string = indvFile
            repl = ''

            filePath = re.sub(pattern, repl, string)

            with open(filePath, 'wb') as file:
                file.write(response.content)
            
            print(str(filePath) + "has been downloaded.")
            

        # If the file is a SharePoint file, then the file will be downloaded
        else: 
            print("Not a Drupal file")

    # If the requested page returns a different HTTP status code, then the terminal returns message
    # Drupal 7 files will return this message
    else:
        print('File not found.')

________

for file in drupalLinks:
    totalLinks.append(file.get('href'))

sharepointLinks = files.findall(href=re.compile("/StanStatePublicDocs"))
for link in sharepointLinks:
    totalLinks.append(link.get('href'))

print(totalLinks)
________

Accessing the file stored at the link address

response = requests.get(files[i])
file_Path = 'research_Paper_1.pdf'

if response.status_code == 200:

    with open(file_Path, 'wb') as file:
        file.write(response.content)

    print('File downloaded successfully')
else:
    print('Failed to download file')'

MISCELLANEOUS

print(files[i])

print(" ".join(fileAddresses))

'''

'''
Variable filePath not accessible within the loop > if response statement > if drupalFiles statement

def rename_drupalFiles():
    pattern = 'https://www.csustan.edu/sites/default/files/' + '[0-9]+' + '-' + '[0-9]+' + '/'
    string = files[i]
    repl = ''

    filePath = re.sub(pattern, repl, string)
    print(filePath)

'''