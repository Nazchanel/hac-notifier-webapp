from lxml import html
from bs4 import BeautifulSoup
import requests
import pandas as pd
import functions


def returnGradeTables(username, password):
  login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'

  session_requests = requests.session()

  urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"

  result = session_requests.get(login_url)
  print(result)
  tree = html.fromstring(result.text)
  authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]

  payload = {
    "VerificationOption": "UsernamePassword",
    "Database": "10",
    "LogOnDetails.Password": password,
    "__RequestVerificationToken": authenticity_token,
    "LogOnDetails.UserName": username
  }
  session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
  )

  result = session_requests.get(urls, headers=dict(referer=urls))

  soup = BeautifulSoup(result.text, "html.parser")

  h1 = soup.find_all(class_="sg-header-heading sg-right")

  h2 = soup.findAll('a', {"class": ["sg-header-heading"]})

  df = pd.read_html(result.text)

  index_list = []
  for i in range(len(df)):
    if len(df[i].columns) == 10:
      index_list.append(i)

  j = 1
  for i in index_list:
      name = f"class{j}.html"
      f = open(f"templates/{name}", "w")
      f.write(df[i].to_html())
      f.close()
      j+=1