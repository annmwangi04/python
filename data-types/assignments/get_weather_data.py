import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables
API_KEY = os.getenv('API_KEY')
city_name = input("Enter the name of the city: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Weather is',data ['weather'][0]['description'])
    print('Current temperature is', data['main']['temp'])
    print('Current temperature feels like is', data['main']['feels_like'])
    print('Current humidity feels like is', data['main']['humidity'])

elif response.status_code == 404:
    print(f"Error {response.status_code}: City not found. Please check the city name and try again.")
elif response.status_code == 401:
    print(f"Error {response.status_code}: Invalid API Key. Please verify your API Key.")
else:
    print(f"Error {response.status_code}: An unexpected error occurred. Please try again later.")   

