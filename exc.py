import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/3542996c4f49c9a2b05816ed/pair/USD/UZS'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
		