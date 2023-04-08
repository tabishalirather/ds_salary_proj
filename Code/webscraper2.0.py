from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=%22data%20scientist%22&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0"

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
path = "C:/Users/tabis/OneDrive - Swinburne University/Semester I - 2023/Easter break_Project/ds_salary_proj/chromedriver_win32/chromedriver.exe"
chromedriver_path = path  # Replace with your chromedriver executable path

driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
driver.get(url)

time.sleep(5)  # Wait for the page to load

job_listings = driver.find_elements_by_xpath('//li[contains(@class, "react-job-listing")]')

for job in job_listings:
    try:
        job_title = job.find_element_by_xpath('.//a[@class="jobLink"]/span').text
        company_name = job.find_element_by_xpath('.//div[@class="jobHeader"]/a').text
        print(f"Job Title: {job_title}")
        print(f"Company Name: {company_name}")
        print("-----------------------------")
    except Exception as e:
        print(f"Error: {e}")
        print("-----------------------------")

driver.quit()
