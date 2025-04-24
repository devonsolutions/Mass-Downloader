import requests
import re
import certifi

# Limit of 1024 characters at a time
# Solution: delete the last letter/character and hit enter
# Possible Solution: alter input from txt file and use input to download
files = input("What files would you like to download? ")
files = files.split("https://")

fullnameFiles = []

for file in files:
    renamedFile = "https://" + file
    fullnameFiles.append(renamedFile)

# Need to delete b/c the first element is an invalid URL
del fullnameFiles[0]

for fullnameFile in fullnameFiles:

    response = requests.get(fullnameFile, verify=certifi.where())

    if response.status_code == 200:

        # Maybe add another ifelse statement so that we can download status code [200] Drupal7 files, as well

        # Works on D10 media that begins with the pattern listed below

        pattern = "https://www.csustan.edu/sites/default/files/" + '[0-9]+' + '-' + '[0-9]+' + '/'
        repl = ''
        removeURL = re.sub(pattern, repl, fullnameFile)
        filePath = "downloads" + str("/") + removeURL

        open(filePath, "wb").write(response.content)

        print(str(filePath) + "has been downloaded.")

    elif response.status_code == 404:
        print("This file is not available.")

    else:
       print("This is the page's status code: " + response.status_code)

'''
Examples for Downloading

https://www.csustan.edu/sites/default/files/2023-01/new-standard-room-use-final.pdf
https://www.csustan.edu/sites/default/files/2023-01/faculty-resources-flyer.pdf
https://www.csustan.edu/sites/default/files/2023-01/sharelinkpro-flyer.pdf
https://www.csustan.edu/sites/default/files/2023-01/standard-room-use-flyer.pdf

Examples for 404 Errors

https://www.csustan.edu/sites/default/files/groups/Office%20of%20Information%20Technology/via_classroom_training_guide.pdf
https://www.csustan.edu/sites/default/files/groups/Office%20of%20Information%20Technology/legacy_classroom_guide.pdf
https://www.csustan.edu/sites/default/files/groups/Office%20of%20Information%20Technology/oit_tech_tip_turn_off_teams_meeting_by_default.pdf
https://www.csustan.edu/sites/default/files/groups/Office%20of%20Information%20Technology/documents/global_protect_vpn_guide_sso.pdf
https://www.csustan.edu/sites/default/files/groups/Office%20of%20Information%20Technology/documents/global_protect_vpn_guide_sso_mac.pdf
https://www.csustan.edu/sites/default/files/groups/Office%20of%20Information%20Technology/documents/how_to_access_office.com_.pdf
https://www.csustan.edu/sites/default/files/groups/Office%20of%20Information%20Technology/documents/how_to_access_microsoft_teams_on_personal_devices_web.pdf

'''

