import requests  # Import the requests library to make HTTP requests.

# Define the city name and API key for the OpenWeatherMap API.
city_name = 'Mombasa'  # The name of the city for which weather data is requested.
API_Key = '1652c0ef9bdc02e019e5b836cbcde67a'  # Your unique API key for authentication.

# Construct the URL for the API request with the city name, API key, and unit (metric system).
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

# Make an HTTP GET request to the API.
response = requests.get(url)

# Check the HTTP status code of the response.
if response.status_code == 200:  # If the status code is 200, the request was successful.
    data = response.json()  # Parse the JSON response from the API.
    
    # Extract and print relevant weather information.
    print('Weather is', data['weather'][0]['description'])  # Description of the weather (e.g., clear sky).
    print('Current temperature is', data['main']['temp'])  # Current temperature in Celsius.
    print('Current temperature feels like is', data['main']['feels_like'])  # Feels-like temperature.
    print('Current humidity is', data['main']['humidity'])  # Current humidity percentage.

elif response.status_code == 404:  # Handle the case where the city is not found.
    print(f"Error {response.status_code}: City not found. Please check the city name and try again.")

elif response.status_code == 401:  # Handle the case where the API key is invalid.
    print(f"Error {response.status_code}: Invalid API Key. Please verify your API Key.")

else:  # Handle any other unexpected errors.
    print(f"Error {response.status_code}: An unexpected error occurred. Please try again later.")
