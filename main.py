from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs # function 을 import 
# from 폴더명.파일명 import function명

# jobs = extract_wwr_jobs("python")
# print(jobs)

# base_url = "https://kr.indeed.com/jobs?q="
# search_term = "python"

# response = get(f"{base_url}{search_term}")

# print(response)
# if response.status_code != 200:
#   print("Fail")
# else:
#   print(response.text)


# 403 권한없음이 표시된다.
# $ pip install selenium 
# url download -> https://sites.google.com/a/chromium.org/chromedriver/downloads
# 크롬드라이버는 내가 사용중인 크롬과 같은 버전을 다운로드 해야한다. 
# 안될시 작성중인 py 와 같은 경로에 chromedriver.exe를 추가한다.


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

results = []
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False) 
# recursive가 없으면 하위 모든 li를 찾는다. False를 추가하면 바로 하위의 li만!
# print(len(jobs))

for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
  if zone == None:  # None 은 데이터가 없다는 의미의 데이터 타입. False 와는 다르다.
    # print("job li")
  # else:
  #   print("mosaic li")
    anchor = job.select_one("h2 a")     # 다음 두 줄을 select 로 한번에 가져올 수 있다.
    # h2 = job.find("h2", class_="jobTitle")
    # a = h2.find("a")
    title = anchor['aria-label']
    link = anchor['href']
    # print(title, link)
    # print("\n\n\n")
    company = job.find("span", class_="companyName").string
    location = job.find("div", class_="companyLocation").string

    # print(company, location)

    job_data = {
      "link" : f"https://kr.indeed.com{link}",
      "company" : company,
      "location" : location,
      "position" : title,
    }

    # print(job_data)
    # print("\n\n\n")
    results.append(job_data)
    
for result in results:
  print(result)

# print(job_list)



# 크롬이 자꾸 꺼질때는 코드 제일 하단에 다음 코드를 추가해준다.
while (True):
  pass