# 1st step install and imbort modules
#-- pip\pip3 install lxml
#-- pip\pip3 install requests
#-- pip\pip install bautifulsoup4


import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_names = []
work_requirement = []


# 2st step use request to fetch the url
result = requests.get("https://stackoverflow.com/jobs?q=python")

# 3st step save page content/markup
src = result.content
#print(src)

# 4st create soup object to parse content
soup = BeautifulSoup(src, "lxml")
#print(soup)

# 5st step find the elements containig into we need
#-- job title, job skills, company names, locaction names
job_title = soup.find_all("h2", {"class":"mb4 fc-black-800 fs-body3" } )
company_names = soup.find_all("h3", {"class":"fc-black-700" })
work_requirement = soup.find_all("div", {"class":"d-inline-flex gs4 fw-wrap" })


# 6th step loop over returned lists to extract nedded info into other lists
for i in range(len(job_title)):
    job_title.append(job_title[i].text)
    company_names.append(company_names[i].text)
    work_requirement.append(work_requirement[i].text)
print(company_names)


# 7th 