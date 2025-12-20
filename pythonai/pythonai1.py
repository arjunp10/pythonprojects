import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
data.keys()
temp = data['current']['temperature_2m']
print(temp)

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data['current']['temperature_2m']

paris_temp = get_weather(48.85, 2.35)
tokyo_temp = get_weather(35.68, 139.76)
print(f"Paris Temperature: {paris_temp}°C")
print(f"Tokyo Temperature: {tokyo_temp}°C")