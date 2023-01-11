from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_job

keyword = input("What do you want to search for? ")

file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")

wwr = extract_wwr_jobs(keyword)
indeed = extract_indeed_job(keyword)
jobs = indeed + wwr

file.write("Position,Company,Locatixon,URL\n")

for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
  
file.close()