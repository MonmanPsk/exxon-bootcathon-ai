import json
import requests


data = requests.get("https://bootcathon.blob.core.windows.net/public/MobilOne-location.txt")
print(data.text)
data = data.content.decode('utf-8')
#text = data.text
json_data = json.loads(data)

print(json_data)
json_data = json.dumps()