import requests
import json

#Variable
APIKey = "ati45mja2ige4zv6u021ri7fto6dxovr"
headers = {'user-agent': 'Chrome/109.0.0.0'}
url = 'https://mushroomobserver.org/api2/observations?children_of=Tulostoma&format=json'

#Outputs
response_API = requests.get(url, headers = headers)
print(response_API.status_code)
print('\n')
print(response_API.raise_for_status())
print('\n')
print(response_API.headers)
print('\n')
print(response_API.content)
#data = response_API.text
data = response_API.json()
print('\n')
print('data = ', data)
print('type de la data = ', type(data))

 #saving

#dictionary = {"results": "sathiyajith"}
#json.loads(data['results'])
data_test = json.dumps(data)

writeFile =open('test_obs.json', 'w')
writeFile.write(data_test)
writeFile.close()
