import requests
x, y = input("What files would you like to download? ").split()
print(x)
print(y)

response = requests.get(x, y)
file_Path = 'research_Paper_1.pdf'

if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
else:
    print('Failed to download file')