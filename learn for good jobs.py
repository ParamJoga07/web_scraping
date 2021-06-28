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
            url = "https://www.learn4good.com/jobs/index.php?controller=job_list&action=display_search_results&page_number=" + str(i)
            html = requests.get(url)
            soup = BeautifulSoup(html.content, 'lxml')
            jobs = soup.find_all('td', class_='job_cell')

            for job in jobs:
                job_title = job.find('a', class_='job_title').text.replace()
                company = job.find('div', class_='additional_job_info').text
                print(job_title)
                print(company)

            for job in jobs:
                job_title = job.find('a', class_='job_title').text
                company = job.find('div', class_='additional_job_info').text
                jobs_ = [job_title, company]
                thewriter.writerow(jobs_)
            i = i + 1


if _name_ == '_main_':
    find_jobs()
