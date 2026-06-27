# %%

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
x = requests.get(url)
y = x.json()

print(y)

print(type(y))    # so this is dictionary
# since this json is dict type then we can use all the dict methods

print(y.keys())

print(y['current']['temperature_2m'])  