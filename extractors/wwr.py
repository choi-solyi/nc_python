from requests import get
from bs4 import BeautifulSoup



def extract_wwr_jobs(keyword):
  base_url ="https://weworkremotely.com/remote-jobs/search?term="
  reseponse = get(f"{base_url}{keyword}")
  # 
  if reseponse.status_code != 200:
    print("Can't request website")
  else:
    results = []

    soup = BeautifulSoup(reseponse.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    # print(len(jobs))
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']

        company, kind, region = anchor.find_all('span', class_="company")

        title = anchor.find('span', class_="title")
        print(company.string, kind.string, region.string, title.string)

        print("///////////////////")

        job_data = {
          "company": company.string,
          "region": region.string,
          "position": title.string
        }
        results.append(job_data)

    # print(results)
    # for result in results:
    #   print(result)
    #   print("///////")
    return results


