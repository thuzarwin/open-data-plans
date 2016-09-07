import requests, json, secrets

class AirtableDataGetter:
	def __init__(self):
		self._base_url = 'https://api.airtable.com/v0/appy0kezt1dXtExJr'
		self._headers = {'Authorization': 'Bearer ' + secrets.AIRTABLE_API_KEY}

	def mission_statements(self): # fetches and processes mission statements into python dictionary
		query = '/plans?view=viw8IPwMsvzcPKodd&fields[]=Name&fields[]=Mission'
		r = requests.get(self._base_url + query, headers=self._headers)
		d = r.json() # use built in function to write json response as a dictionary structure
		mission_data = []
		for i in d['records']:
			dept = i['fields']['Name']
			try: 
				mission = i['fields']['Mission']
			except:
				mission = 'data not yet added to airtable'
			mission_data.append((dept, mission))
		mission_dict = dict(mission_data)
		return mission_dict