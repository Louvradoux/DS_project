import json
import pandas as pd
 
# Opening JSON file
with open('test_obs.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print('JSON keys are = ', json_object.keys())
df = pd.DataFrame(json_object.get('results'), columns = ['Results'])

df