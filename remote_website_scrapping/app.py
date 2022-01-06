# from pandas.core.indexes.base import Index
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from openpyxl import Workbook
from IPython.display import display, HTML
import pandas as pd

driver= webdriver.Chrome()
driver.get("https://remotive.io/remote-companies")
all_links=[]


# To Click all the load more tag in website----------
while True:
    try:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="morecompanies"]/button'))))
        print('success')
    except:
        print('failed')
        break     
print('completed')


# get all link of the company from Href ------------------
element = driver.find_element_by_id("hits")


# get the tag<a> values---------------
all_options = element.find_elements_by_tag_name("a")
for option in all_options:
    if option.get_attribute("href") != None:
        all_links.append(option.get_attribute("href"))


# website link------------------------------------------------  
var_website=''
def website():
    global var_website
    var_website='-'
    try:
        website=driver.find_element_by_xpath('//*[@id="wrapwrap"]/main/section/div[1]/div[3]/div[2]/div[2]/div[1]')
        all_options = website.find_elements_by_tag_name("a")
        for option in all_options:
            try:
                if option.get_attribute("href") != None:
                    var_website=option.get_attribute("href")
            except:
                pass
    except:
        pass
    try:
        for website2 in driver.find_elements(By.XPATH ,'//*[@id="detail-side-banner"]/a[1]'):
            c=website2.text
            if c.find('Website') != -1: 
                var_website=website2.get_attribute('href')
    except:
        pass

# get the company name---------------------------------------------------------------
var_company_name=''
def company_name():
    global var_company_name
    var_company_name='-'
    try:
        Company_name=driver.find_element_by_class_name('company-name')
        var_company_name=Company_name.text
        print(Company_name.text)
    except:
        pass
    try:
        Company_name=driver.find_element(By.XPATH,'//*[@id="detail-side-banner"]/h2')
        var_company_name=Company_name.text
        print(Company_name.text)
    except:
        pass

# get the number employee required-----------------------
var_employees_required=''
def employees_required():
    global var_employees_required
    var_employees_required='-'
    for employee in driver.find_elements_by_xpath('/html/body/div[1]/main/section/div[1]/div[3]/div[2]/div[1]/div[1]/span'):
        try:
            var_employees_required=employee.text
            print(employee.text)
        except:
            pass
    for employee2 in driver.find_elements(By.XPATH ,'//*[@id="detail-side-banner"]/p[2]/span'):
        try:
            c=employee2.text
            if c.find('-') != -1: 
                var_employees_required=employee2.text
                print(employee2.text)
        except:
            pass  

# get the job and hiring location------------------------------------
var_location=''
var_jobs_count=''
def number_job_location():
    global var_location,var_jobs_count
    var_location='-'
    var_jobs_count='-'
    for job in driver.find_elements_by_xpath('//*[@id="wrapwrap"]/main/section/div[1]/div[3]/div[2]/div[1]/div[2]/span'):
        c=job.text
        # print(c)
        if c.find('job') != -1:
            var_jobs_count=job.text
            # print(job.text)
        if c.find('Hiring') != -1:
            var_location=job.text
            # print(var_location)
            for job2 in  driver.find_elements_by_xpath('//*[@id="wrapwrap"]/main/section/div[1]/div[3]/div[2]/div[1]/div[3]/span'):
                var_jobs_count=(job2.text)
                # print(job2.text)
        else:
            pass 

# get the twitter link--------------------
var_twitter='';
def twitter():
    global var_twitter
    var_twitter='-'
    try:
        twitter=driver.find_element_by_xpath('//*[@id="wrapwrap"]/main/section/div[1]/div[3]/div[2]/div[2]/div[2]')
        all_options = twitter.find_elements_by_tag_name("a")
        for option in all_options:
            try:
                if option.get_attribute("href") != None:
                    # print(option.get_attribute("href"))
                    var_twitter=(option.get_attribute("href"))
            except:
                pass
    except:
        pass
    
    for twitter2 in driver.find_elements(By.XPATH ,'//*[@id="detail-side-banner"]/a[2]'):
        try:
            c=twitter2.get_attribute("href")
            if c.find('twitter') != -1: 
                print(twitter2.get_attribute("href"))
                var_twitter=(twitter2.get_attribute("href"))
        except:
            pass
    
    
# get the linkdin link ------------------------
var_linkdin='';
def linkdin():
    global var_linkdin
    var_linkdin='-'
    try:
        linkdin=driver.find_element_by_xpath('//*[@id="wrapwrap"]/main/section/div[1]/div[3]/div[2]/div[2]/div[3]')
        all_options = linkdin.find_elements_by_tag_name("a")
        try:
            for option in all_options:
                if option.get_attribute("href") != None:
                    # print(option.get_attribute("href"))
                    var_linkdin=(option.get_attribute("href"))
        except:
            pass
    except:
        pass
    try:
        for linkdin in driver.find_elements(By.XPATH ,'//*[@id="detail-side-banner"]/a[3]'):
            c=linkdin.get_attribute("href")
            if c.find('linkedin') != -1: 
                # print(linkdin.get_attribute("href"))
                var_linkdin=(linkdin.get_attribute("href"))
    except:
        pass
        
        
# get all Job_titles ---------------------------------------------------------- 
var_job_titles=[] 
def job_titles():
    global var_job_titles
    var_job_titles.clear()
    for job_titles in driver.find_elements(By.XPATH ,'/html/body/div[1]/main/section/div[2]/div[1]/div[2]/div[1]/ul/li/div[1]/div[2]/a/span'):
        try:
            # print(job_titles.text)
            var_job_titles.append(job_titles.text)
        except:
            pass
        
for x in all_links:
    print(x)
    driver.get(x) 
    
    company_name()   
    employees_required()  
    number_job_location()
    website()   
    linkdin()   
    twitter()  
    job_titles() 
    
    # Company DATA  
    print('company name = '+var_company_name)
    print('website = '+var_website)
    print(var_job_titles)
    print('linkdin = '+var_linkdin)
    print('twitter = '+var_twitter)
    print('jobs_count = '+var_jobs_count)
    print('location = '+var_location)
    print('employee_required = '+var_employees_required)
    print()
    print()
    print()
    # Email()   #8
    # phone()   #9
    # country()  #10
    if var_company_name != '-':
        file = pd.ExcelFile('Remotive Leads.xlsx')
        df = pd.read_excel(file)
        df1 = pd.DataFrame(df)
        row_to_add = pd.DataFrame({'Web Site':[var_website],'Company Name':[var_company_name],'Company Size':[var_employees_required],'Jobs':[var_job_titles],'Linkedin Page':[var_linkdin],'Twitter Page':[var_twitter],'Country':[var_location]})
        df_final = df1.append(row_to_add)
        datatoexcel= pd.ExcelWriter('Remotive Leads.xlsx',engine='xlsxwriter')
        df_final.to_excel(datatoexcel,sheet_name='sheet1',index = False)
        datatoexcel.save()
driver.close()   