import requests

url  = input('Enter your url:')
nameimg = input('Enter your image name:')

x = requests.get(url=url)

file = open(nameimg, 'wb')
file.write(x.content)
