from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import urllib.request
from PIL import Image
from fastbook import *
import requests
import numpy

data = pd.read_csv('link.csv')

links = data['Links'].values.tolist()

driver = webdriver.Chrome()
driver.maximize_window()

df = []
cnt=0
for link in links:
    
    print(cnt,'=====>',link)
    
    try:
        driver.get(link)
        pic_link = driver.find_element(By.XPATH,'//*[@id="landingImage"]').get_attribute('src')
        
        
        img = Image.open(requests.get(pic_link, stream = True).raw)
        name = pic_link.split('/')[-1]
            
        img = img.resize((200,200))
        img.save(f'images/{name}')
        img = numpy.array(img)
        
        try:
            rating = driver.find_element(By.XPATH,'//*[@id="reviewsMedley"]/div/div[1]/span[1]/span/div[2]/div/div[2]/div/span').text.split()[0]
        except:
            rating = None
        try:
            price =  driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]').text
        except:
            price = None
        try:
            description = driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/ul').text
        except:
            description= None
        
        
        print(rating)
        df.append([img,rating,price,description])
        time.sleep(1)
        if cnt%100 == 0:
            data = pd.DataFrame(df,columns=['imges','rating','price','description'])
            data.to_csv(f'data\description{cnt}.csv',index=False)
            df=[]

            
        cnt+=1
    except:
        continue
    
    
    


