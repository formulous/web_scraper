import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit={LIMIT}&sort&psf=advsrch&from=advancedsearch&vjk=77c60ac6046ec6c7"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    n = 0
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    print(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("td", {"class": "resultContent"})
    print(results)
    for result in results:
        '''title = result.find("h2", {"class": "jobTitle jobTitle-color-purple jobTitle-newJob"})
        if title is not None and title.string is not None:
            span = title.find_all("span")["title"]
            print(n, span, "나 출력 되고있슴")'''
        jobs = result.find("div", {"class": "heading4 color-text-primary singleLineTitle tapItem-gutter"})
        companies = result.find("div", {"class": "heading6 company_location tapItem-gutter"})
        if jobs is not None and jobs.string is not None:
            span = jobs.find("span")["title"]
            print(n, span)
        if companies is not None:
            print(n, companies.string)
        n += 1
    return jobs
# h2 - jobTitle
# heading4 color-text-primary singleLineTitle tapItem-gutter