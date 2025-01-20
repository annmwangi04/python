import requests

city_name = 'Nairobi'
API_Key = '1652c0ef9bdc02e019e5b836cbcde67a'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Weather is',data ['weather'][0]['description'])
    print('Current temperature is', data['main']['temp'])
    print('Current temperature feels like is', data['main']['feels_like'])
    print('Current humidity feels like is', data['main']['humidity'])

