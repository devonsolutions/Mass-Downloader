Total: 6

To-Do List
- use os library to redirect downloads to Download folder instead of inside massdownloader downloads folder
- https://www.geeksforgeeks.org/automatically-organize-downloads-folder-in-python/

Sources:
Multiple inputs: https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
For Loops: https://www.w3schools.com/python/python_for_loops.asp
Using RegEx re.sub() to rename filepaths: https://pythonexamples.org/python-re-sub/
Slicing and Indexing: https://www.freecodecamp.org/news/slicing-and-indexing-in-python/
https://www.csustan.edu/sites/default/files/2023-03/asi-vice-pres-finance-position-desc.pdf
https://www.geeksforgeeks.org/simple-multithreaded-download-manager-in-python/
HTTP response statues codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
https://uibakery.io/regex-library/url-regex-python
Adding SSL Verification with Certifi: https://proxiesapi.com/articles/making-https-requests-in-python-with-requests-and-certifi
https://www.geeksforgeeks.org/how-to-use-words-in-a-text-file-as-variables-in-python/

Old Code

# Limit of 1024 characters at a time
# Solution: delete the last letter/character and hit enter
# Possible Solution: alter input from txt file and use input to download

# https://www.geeksforgeeks.org/how-to-use-words-in-a-text-file-as-variables-in-python/
# files = []

# textFile = open("input.txt", "r")
# print(textFile.read())

 
'''
files = input("What files would you like to download? ")
files = files.split("https://")

fullnameFiles = []

for file in files:
    renamedFile = "https://" + file
    fullnameFiles.append(renamedFile)

# Need to delete b/c the first element is an invalid URL
del fullnameFiles[0]
'''

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