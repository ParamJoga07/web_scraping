from bs4 import BeautifulSoup
import requests
from csv import writer

pages = int(input("Enter number of pages you want to search : "))
print()
i = 1
with open('JOBS.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)
    header = ['JOB TITLE', 'COMPANY NAME']
    thewriter.writerow(header)
    while i <= pages:
        url = "https://www.seek.com.au/devloper-jobs-in-information-communication-technology/in-Canada?page=" + str(i)
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'lxml')
        jobs = soup.find_all('div', class_='_1UfdD4q')

        for job in jobs:
            job_title = job.find('a', class_='_2S5REPk').text
            company = job.find('a', class_='_17sHMz8').text
            print(job_title)
            print(company)

        for job in jobs:
            job_title = job.find('a', class_='_2S5REPk').text
            company = job.find('a', class_='_17sHMz8').text
            jobs_ = [job_title, company]
            thewriter.writerow(jobs_)
        i = i + 1
