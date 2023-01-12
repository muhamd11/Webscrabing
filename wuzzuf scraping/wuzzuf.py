import csv
from itertools import zip_longest
import lxml
import requests
from bs4 import BeautifulSoup
job_title = []
company_name = []
locations_name = []
job_skill = []
links = []

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb") # use requests to fetch url

src = result.content # save page content?markup

soup = BeautifulSoup(src, "lxml")
job_titles = soup.find_all("h2",{"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
locations_names = soup.find_all("span",{"class":"css-5wys0k"})
job_skills = soup.find_all("div",{"class":"css-y4udm8"})

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    links.append("https://wuzzuf.net")
    links.append(job_titles[i].find("a").attrs['href'])
    locations_name.append(locations_names[i].text)
    job_skill.append(job_skills[i].text)

file_list = [job_title,company_name,locations_name,job_skill,links]
exp = zip_longest(*file_list)


with open("D:\PythonProjects\Web scrabing\jobdataset.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title","company name ", "location","job skills","links"])
    wr.writerows(exp)

