import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.ycombinator.com/jobs'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

jobs = soup.find_all('div', class_='job-listing')

with open('job_listings.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company', 'Salary Range', 'Job Type', 'Location', 'Application Link', 'Hiring Manager'])

    for job in jobs:
        #job_title = job.find('h2', class_='title').text.strip()
        company = job.find( class_="shrink-0 md:mr-5").text.strip()
        #salary_range = job.find('span', class_='salary-range').text.strip() if job.find('span', class_='salary-range') else 'N/A'
        job_type = job.find('a', class_="font-semibold text-linkColor").text.strip() if job.find( class_="font-semibold text-linkColor") else 'N/A'
        #location = job.find('span', class_='location').text.strip() if job.find('span', class_='location') else 'N/A'
        #application_link = job.find('a', class_='apply-link')['href']
        #hiring_manager = job.find('span', class_='hiring-manager').text.strip() if job.find('span', class_='hiring-manager') else 'N/A'

        writer.writerow([company, job_type,])

#print('Job listings have been successfully scraped and stored in job_listings.csv')
print('company')
