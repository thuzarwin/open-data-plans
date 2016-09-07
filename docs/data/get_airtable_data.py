from utils import call_airtable


def main():
	c = call_airtable.AirtableDataGetter()
	m = c.mission_statements()
	print('fetched ' + str(len(m)) + " records" )
	print(m)

if __name__ == '__main__':
	main()
