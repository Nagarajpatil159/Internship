#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1: In this question you have to scrape data using the filters available on the webpage You have to use the location and 
#salary filter.You have to scrape data for “Data Scientist” designation.You have to scrape the job-title, job-location, company name, experience required.  



# In[6]:


get_ipython().system('pip install selenium')


# In[7]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[8]:


driver=webdriver.Chrome()


# In[9]:


#OPENING CHROME PAGE

driver.get("https://www.naukri.com/")


# In[10]:


#entering designation and job location

designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[11]:


#entering Location
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')


# In[12]:


#to click on search button
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[13]:


# filtering 3-6 lakh salary
search1=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/label/i")
search1.click()


# In[14]:


job_title=[]
job_location=[]
company_name=[]
experience_need=[]


# In[15]:


#scraping job_title from the given page

titles=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')

for i in titles:
    job_title.append(i.text)


# In[16]:


#scraping job_location from the given page

location=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')

for i in location:
    job_location.append(i.text)


# In[17]:


#scraping company name from the given page

companyname=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')

for i in companyname:
    company_name.append(i.text)


# In[18]:


#scraping experience_need name from the given page

experience=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')

for i in experience:
    experience_need.append(i.text)


# In[19]:


df=pd.DataFrame({'title':job_title[0:10],'location':job_location[0:10],'company_name':company_name[0:10],'experience':experience_need[0:10]})
df


# In[ ]:





# In[25]:


# question 2 did at last


# In[ ]:





# In[46]:


#Q3: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:

# opening flipkart
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=F")


# In[47]:


rating=[]
review_summary=[]
full_review=[]


# In[48]:


for page in range(0,10):
    ratings=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
    for i in ratings:
        rating.append(i.text)                         #to scrape rating


# In[26]:


# to scrape multiple pages using next button


# In[49]:


next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span')
next_button.click()
time.sleep(3)


# In[50]:


for page in range(0,10):
    reviews=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
    for i in reviews:
        review_summary.append(i.text)    # scrape reviews from flikart


# In[27]:


# to scrape multiple pages using next button


# In[51]:


next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span')
next_button.click()
time.sleep(3)


# In[52]:


for page in range(0,10):
    fullreview=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]/div')
    for i in fullreview:
        full_review.append(i.text)                # scrape full review


# In[28]:


# to scrape multiple pages using next button


# In[53]:


next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]/span')
next_button.click()
time.sleep(3)


# In[54]:


df=pd.DataFrame({'Ratings':rating[0:100],'Summary':review_summary[0:100],'Full_review':full_review[0:100]})
df


# In[ ]:





# In[1]:


#Q4: Scrape data forfirst 100 sneakers you find whenyouvisitflipkart.com and search for “sneakers” inthe search field.

get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get("https://www.flipkart.com/")


# In[5]:


sneakers=driver.find_element(By.XPATH,'//input[@class="Pke_EE"]')
sneakers.send_keys('sneakers')

search=driver.find_element(By.XPATH,'//button[@class="_2iLD__"]')
search.click()                                                   #sending sneaker key and clicking on search button


# In[6]:


brands=[]
products_de=[]
prices=[]


# In[7]:


for page in range(0,4):
    brand=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
    for i in brand:
        brands.append(i.text)


# In[29]:


# scraping multiple page data using next button


# In[8]:


search1=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]/span')
search1.click()


# In[9]:


for page in range(0,4):
    product=driver.find_elements(By.XPATH,'//div[@class="hCKiGj"]/a[1]')
    for i in product:
        products_de.append(i.text)                #scraping products details from given pages


# In[30]:


# scraping multiple page data using next button


# In[10]:


search1=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]/span')
search1.click()


# In[11]:


for page in range(0,4):
    price=driver.find_elements(By.XPATH,'//div[@class="Nx9bqj"]')
    for i in price:
        prices.append(i.text)             #scraping price details from given pages


# In[31]:


# scraping multiple page data using next button


# In[12]:


search1=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]/span')
search1.click()


# In[13]:


df=pd.DataFrame({'Brands':brands[0:100],'Product':products_de[0:100],'price':prices[0:100]})
df                                                  # creating data frame


# In[ ]:





# In[ ]:





# In[41]:


#Q5: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image


driver=webdriver.Chrome()


# In[42]:


driver.get("https://www.amazon.com/")


# In[44]:


laptop=driver.find_element(By.XPATH,'//input[@type="text"]')
laptop.send_keys('Laptop')

search=driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]')
search.click()                                                            # passing laptop keyword in search field and clicking on search button


# In[46]:


search1=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[5]/span/li/span/div/div/ul/span[11]/li/span/a/div/label/i')
search1.click()          #filtering intel corei7


# In[58]:


titles=[]
ratings=[]
prices=[]
reviews=[]


# In[63]:


title=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')

for i in title:
    titles.append(i.text)  # scraping titles of laptops


# In[64]:


rating=driver.find_elements(By.XPATH,'//span[@class="a-icon-alt"]')

for i in rating:
    ratings.append(i.text)            #scraping ratings of laptops


# In[65]:


price=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')

for i in price:
    prices.append(i.text)             #scraping prices of laptops


# In[66]:


review=driver.find_elements(By.XPATH,'//span[@class="a-size-base s-underline-text"]')

for i in review:
    reviews.append(i.text)             #scraping prices of laptops


# In[68]:


df=pd.DataFrame({'LAP_title':titles[0:10],'Lap_prices':prices[0:10],'reviews':reviews[0:10],'ratings':ratings[0:10]})
df


# In[ ]:





# In[ ]:





# In[71]:


#Q6: Write a python program to scrape data for Top 1000 Quotes of All Time.
driver=webdriver.Chrome()


# In[72]:


driver.get("https://www.azquotes.com/")


# In[73]:


# clicking on top quotes
search=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
search.click()                                                           


# In[74]:


quotes=[]
authors=[]
types_ofQ=[]


# In[75]:


for page in range(0,10):
    quote=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote:
        quotes.append(i.text)                #scraping top quotes


# In[32]:


# to scrape multiple page data using next button


# In[76]:


search1=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
search1.click()


# In[77]:


for page in range(0,10):
    author=driver.find_elements(By.XPATH,'//div[@class="author"]/a')
    for i in author:
        authors.append(i.text)                #scraping Authors name


# In[33]:


# to scrape multiple page data using next button


# In[78]:


search1=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
search1.click()


# In[79]:


for page in range(0,10):
    types=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in types:
        types_ofQ.append(i.text)                #scraping type of quote


# In[34]:


# to scrape multiple page data using next button


# In[80]:


search1=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
search1.click()


# In[82]:


df=pd.DataFrame({'Top_quotes':quotes[0:1000],'Authors':authors[0:1000],'Types':types_ofQ[0:1000]})
df                                 # creating dataframe        


# In[ ]:





# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[15]:


#Q7: Write a python program to display list of respected former Prime Ministers of India (i.e. Name,Born-Dead, Term of office, Remarks) from 

driver=webdriver.Chrome()


# In[16]:


driver.get("https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1473165149-1")


# In[17]:


names=[]
borndead=[]
term_of_office=[]
remarks=[]


# In[18]:


name=driver.find_elements(By.XPATH,'//div[@class="TableData"]//tr//td[2]')

for i in name:
    names.append(i.text)  # scraping names of PM


# In[19]:


born_dead=driver.find_elements(By.XPATH,'//div[@class="TableData"]//tr//td[3]')

for i in born_dead:
    borndead.append(i.text)  # scraping born_dead date


# In[23]:


terms=driver.find_elements(By.XPATH,'//div[@class="TableData"]//tr//td[4]')

for i in terms:
    term_of_office.append(i.text)  # scraping term of office


# In[22]:


remark=driver.find_elements(By.XPATH,'//div[@class="TableData"]//tr//td[5]')

for i in remark:
    remarks.append(i.text)  # scraping remarks


# In[25]:


df=pd.DataFrame({'NAME':names[0:19],'BnD':borndead[0:19],'TERM':term_of_office[0:19],'REMARKS':remarks[0:19]})
df                                 # creating dataframe        


# In[ ]:





# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[8]:


#Q8: Write a python program to display list of 50 Most expensive cars in the world
#(i.e. Car name and Price) from https://www.motor1.com

driver=webdriver.Chrome()



# In[9]:


driver.get("https://www.motor1.com")


# In[10]:


get=driver.find_element(By.XPATH,'//input[@class="m1-search-panel-input m1-search-form-text"]')
get.send_keys('50 most expensive cars')


# In[17]:


#clicking on search button


# In[11]:


search=driver.find_element(By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
search.click()                                                    


# In[18]:


#clicking on most expensive cars link


# In[12]:


search=driver.find_element(By.XPATH,'/html/body/div[9]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a')
search.click()                                                        


# In[13]:


cars=[]
price=[]


# In[14]:


car=driver.find_elements(By.XPATH,'//div[@class="postBody description e-content"]/h3')

for i in car:
    cars.append(i.text)  # scraping car names


# In[15]:


prices=driver.find_elements(By.XPATH,'//div[@class="postBody description e-content"]/p/strong')

for i in prices:
    price.append(i.text)  # scraping price


# In[16]:


df=pd.DataFrame({'Car_names':cars[0:50],'Prices':price[0:50]})
df                                 # creating dataframe        


# In[ ]:





# In[ ]:





# In[1]:


# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the 
#job-title, job-location, company_name, experience_required.
#1. First get the webpage https://www.shine.com

get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[3]:


driver=webdriver.Chrome()


# In[4]:


# opening shine.com
driver.get("https://www.shine.com")


# In[9]:


job_title=[]
job_location=[]
company_name=[]
experience_need=[]


# In[14]:


#entering designation 

designation=driver.find_element(By.XPATH,'//div[@class="searchForm_search_wrap__cXRj4"]//li[1]/div/input')
designation.send_keys('Data Scientist')


# In[18]:


# inserting location


# In[15]:


Location=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input')
Location.send_keys('Bangalore') 


# In[17]:


# enter search button

search=driver.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button')
search.click()               


# In[19]:


#scraping job_title from the given page

titles=driver.find_elements(By.XPATH,'//strong[@class="jobCard_pReplaceH2__xWmHg"]')
for i in titles[0:10]:
    job_title.append(i.text)
job_title[0:10]


# In[20]:


#scraping job_location from the given page

location=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')

for i in location[0:10]:
    job_location.append(i.text)
job_location[0:10]


# In[21]:


#scraping company_name from the given page

companyname=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')

for i in companyname[0:10]:
    company_name.append(i.text)


# In[22]:


#scraping experience_need name from the given page

experience=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')

for i in experience:
    experience_need.append(i.text)


# In[23]:


df=pd.DataFrame({'title':job_title[0:10],'location':job_location[0:10],'company_name':company_name[0:10],'experience':experience_need[0:10]})
df


# In[ ]:




