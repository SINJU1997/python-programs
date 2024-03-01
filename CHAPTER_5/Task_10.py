#Implementing Web Scraping in Python with BeautifulSoup IT Companies in Kerala | IT Companies in Infopark - Kochi, Cherthala, & Thrissur https://infopark.in/companies/company

# import requests
# url="https://infopark.in/companies/company"
# r=requests.get(url)
# print(r.content)

import requests 
from bs4 import BeautifulSoup 
URL = "https://infopark.in/companies/company/thrissur"
r = requests.get(URL,verify=False) 
# print(r.content) 
soup = BeautifulSoup(r.content, 'html.parser') 
# print(soup.title) 
company_name=soup.find_all('h3',class_='company-name-hd')
# print(company_name)
for company in company_name:
    companies=company.text.strip()
    print(companies)