import json
import os
print(os.getcwd())
f = open("./modules/functions.json","r")

data = json.load(f)

for i in data:
    print(i)

f.close()