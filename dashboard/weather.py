import arrow
import requests

# Get first hour of today
start = arrow.now().floor('day')

# Get last hour of today
end = arrow.now().ceil('day')

response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 58.7984,
    'lng': -74.006,
    'params': ','.join(['waveHeight', 'airTemperature']),
    'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
    'end': end.to('UTC').timestamp()  # Convert to UTC timestamp
  },
  headers={
    'Authorization': 'example-api-key'
  }
)

# Do something with response data.
json_data = response.json()