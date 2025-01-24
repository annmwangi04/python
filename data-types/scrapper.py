# import requests

# from bs4 import BeautifulSoup

# #url = "http://www.jumia.co.ke/mlp-black-friday/phones-tablets/?page=1"
# #url = "https://wellfound.com/jobs"
# #url = "https://app.zinduaschool.com/"
# #url = "https://kilimall.com/"
# url='https://www.ycombinator.com/jobs'

# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# div_tag = soup.find_all('div')
# for div in div_tag:
#     print(div.text)

import requests
from bs4 import BeautifulSoup
import re

#data = requests.get("https://www.masaimara.com/")
data = requests.get("https://www.jumia.co.ke")
soup = BeautifulSoup(data.content, "html.parser")
#print(soup)

# h1_tags = soup.find_all("h1")
# print(h1_tags)

# for tag in h1_tags:
#     print(tag.text)

# products = soup.find_all(class_ = "prd")
# print(products)
prices = re.findall(r"")
clean_price = []

prices = re.findall
print(prices)

for price in prices:
    number_price = price[4:]
    number_price = number_price.replace(",", "")
    number_price = int(number_price)
    clean_price.append(number_price)

    f = open("prices.csv",'w')
    for price in clean_price:
        f.write(str(price))
        f.write(",")

    # min_price = min(clean_price)
    # print(min_price)

    print(clean_price)


