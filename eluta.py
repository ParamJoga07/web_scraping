from bs4 import BeautifulSoup
import requests
from csv import writer


def find_jobs():
    pages = int(input("Enter number of pages you want to search : "))
    print()
    i = 1
    with open('JOBS.csv', 'w', newline='', encoding='utf8') as f:
        thewriter = writer(f)
        header = ['JOB TITLE', 'COMPANY NAME']
        thewriter.writerow(header)
        while i <= pages:
            url = "https://www.eluta.ca/search?q=zoho+sort%3Apost&pg=" + str(i)
            html = requests.get(url)
            soup = BeautifulSoup(html.content, 'lxml')
            jobs = soup.find_all('div', class_='organic-job')

            for job in jobs:
                job_title = job.find('h2', class_='title').text
                company = job.find('a', class_='employer').text
                print(job_title)
                print(company)

            for job in jobs:
                job_title = job.find('h2', class_='title').text
                company = job.find('a', class_='employer').text
                jobs_ = [job_title, company]
                thewriter.writerow(jobs_)
            i = i + 1


if _name_ == '_main_':
    find_jobs()
