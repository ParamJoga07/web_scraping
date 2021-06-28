from bs4 import BeautifulSoup
import requests
from csv import writer

pages = int(input("Enter number of pages you want to search : "))
print()
i = 0
with open('JOBS.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)
    header = ['JOB TITLE', 'COMPANY NAME']
    thewriter.writerow(header)
    while i <= ((pages * 10) - 10):
        url = "https://au.indeed.com/jobs?q=Developer&start=" + str(i)
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'lxml')
        jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

        for job in jobs:

            job_title = job.find('a', class_='jobtitle').text.replace("\n", "")
            company = job.find('span', class_='company').text.replace("\n", "")

            print(job_title)
            print(company)
            print()

        for job in jobs:
            job_title = job.find('a', class_='jobtitle').text.replace("\n", "")
            company = job.find('span', class_='company').text.replace("\n", "")
            jobs_ = [job_title, company]

            thewriter.writerow(jobs_)
        i = i + 10
