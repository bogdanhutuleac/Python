import requests
content = requests.get("https://adventofcode.com/2016/day/6/input",auth=('user', 'pass'))

print(content.text)