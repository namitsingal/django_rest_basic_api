import json
import requests


IGNORED_FIELDS = ["Item", "Sub-Total (Software)"]
stream = open('data.json','r').read()
data = json.loads(stream)


url='http://namitsingal.com/api/items/'
year = []


for temp in data['fields']:
	if temp['label'] not in IGNORED_FIELDS:#!= "Item":
		year.append(temp['label'])

for temp in data['data']:
	item_type = temp[0]
	if item_type in IGNORED_FIELDS:
		continue
	for i, temp1 in enumerate(temp[1:]):
		post_data= {'item_type':item_type, 'year': year[i], 'revenue':temp1}
		response= requests.post(url, data=post_data)
	
