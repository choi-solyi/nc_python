# 5.0 웹 스크래핑 
# beautiful soup (웹사이트의 데이터를 받아올 수 있게 해주는 python 라이블러리)


# 5.1 다운로드
# $ pip install beautifulsoup4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start

# 5.2 주의사항 
# 웹스크래핑으로 상업적 이용시 주의해야한다.


from requests import get
from bs4 import BeautifulSoup

base_url ="https://weworkremotely.com/remote-jobs/search?term="
search_term ="vue"

reseponse = get(f"{base_url}{search_term}")
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
  for result in results:
    print(result)
    print("///////")







