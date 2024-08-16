#notes web-scrapping

from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with")
unfamilier_skill = input('>')
print(f'filtering out {unfamilier_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=java+spring+boot&txtLocation=&cboWorkExp1=0').text
    soup = BeautifulSoup(html_text , 'lxml')
    jobs = soup.find_all('li' , class_="clearfix job-bx wht-shd-bx")
    for index , job in enumerate(jobs):    
        job_published_date = job.find('span' , class_ = "sim-posted").span.text
        if 'few' in job_published_date:
            copmpany_name = job.find('h3' , class_="joblist-comp-name").text.replace(' ' , '')
            skills = job.find("span" , class_="srp-skills").text.replace(' ' , '')
            more_info = job.header.h2.a['href']
            if unfamilier_skill not in skills:
                with open(f'posts/{index}.csv' , 'w') as f:    
                    f.write(f'company name: {copmpany_name.strip()} \n') 
                    f.write(f'Required skills: {skills.strip()} \n')
                    f.write(f'more info: {more_info} \n')
                print(f'file saved {index}')
                    


if __name__ == '__main__':
    while True:
        find_jobs()
        time.sleep(6000)

    

# with open('home.html' , 'r') as html_file:
#     content = html_file.read()
    

#     soup = BeautifulSoup(content , 'lxml')
    # print(soup.prettify())
    # tag = soup.find_all('h1')
    # table_columns = soup.find_all('td')

    # for td in table_columns:
    #     print(td.text)

    # price = soup.find_all('tr' , class_="price")
   
    # for p in price:
    #     pri = price.td.text.split()[-1]
    #     print(pri)
    #     print(f'{pri}')

        



