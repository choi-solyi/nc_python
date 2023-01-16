# 4.5 For Loops

websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tictoc.com"
)

websites[0]

# tuple 의 갯수만큼 반복
for website in websites:
    print("Hello", website)

# 일반적으로 tuple이나 list를 만들 때 복수형으로 만든다
# websites, movies, users, photos ,...
# for 에서는 단수형으로 쓴다. 
# website, movie, user, photo



# 4.6 URL Formatting

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  print(website)


# if not 조건 : 조건이 아닐때


# 4.7 Requests

# python standard library 에 포함되어 있지 않은 라이브러리를 사용해볼거다

# https://pypi.org/
# 다른 사람들의 프로젝트나 모듈을 모아둔 곳


# https://pypi.org/project/requests/
# 이번 강의에서 쓸 라이브러리는 이거!

# visual studio code에서 설치할때: pip install requests
from requests import get


# 4.8 status codes

results= {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  print(response.status_code) # 200 

  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "FAILED"  
print(results)


#  httpstat.us