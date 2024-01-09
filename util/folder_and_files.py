from os import mkdir
import json

data = None

with open("data.json", "r") as file:
	data = json.loads(file.read())

for key, value in data.items():
	tagName = f'[{key.replace("_", " ").upper()}]'
	for each in value:
		fileName = " ".join(map(lambda x: x.upper() if x in ['i', 'ii'] else x[0].upper() + x[1:], each.replace("_", " ").split(" ")))
		path = f'../{tagName} {fileName}.py' 
		with open(path, "x") as file:
			pass