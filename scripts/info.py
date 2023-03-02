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

data = pd.read_csv('data\link.csv')

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
        img.save(f'images/{name}')
        img = f'images/{name}'
        
        try:
            rating = driver.find_element(By.XPATH,'//*[@id="reviewsMedley"]/div/div[1]/span[1]/span/div[2]/div/div[2]/div/span').text.split()[0]
        except:
            rating = None
        try:
            price =  driver.find_element(By.XPATH,'//*[@id="corePrice_feature_div"]/div/span/span[2]').text
            print(price)
        except:
            price = None
        try:
            description = driver.find_element(By.XPATH,'//*[@id="feature-bullets"]/ul').text
        except:
            description= None
        
        df.append([img,rating,price,description])
        
        if cnt%100 == 0:
            data = pd.DataFrame(df,columns=['Image','Ratings','Price','Description'])
            data.to_csv(f'data\description{cnt}.csv',index=False)
            df=[]
        cnt+=1 
    except:
        continue




            
           
    


