import requests

from bs4 import BeautifulSoup

#url = "http://www.jumia.co.ke/mlp-black-friday/phones-tablets/?page=1"
#url = "https://wellfound.com/jobs"
#url = "https://app.zinduaschool.com/"
#url = "https://kilimall.com/"
url='https://www.ycombinator.com/jobs'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

a_tag = soup.find_all('a')
for div in a_tag:
    print(div.text)



