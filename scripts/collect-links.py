from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time


# driver = webdriver.Edge()
# driver.maximize_window()

# data = []

# web = ['https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_72%3A1248882011&s=review-rank&dc&qid=1677507872&rnid=1248877011&ref=sr_pg_3',
#        'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456%2Cn%3A11548956011%2Cn%3A12879431%2Cp_72%3A1248882011&dc&ds=v1%3A%2BTHnNU%2F8j5VYp%2B3K%2BMx2eFTa2cGOEOUOGfrQqVAOXrc&qid=1677508601&rnid=11548956011&ref=sr_nr_n_1',
#        'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456%2Cn%3A11548956011%2Cn%3A11036491%2Cp_72%3A1248882011&dc&qid=1677508880&rnid=1248877011&ref=sr_nr_p_72_4&ds=v1%3AvS4YI5fOEiGNaj11SqctJoiZp9OQ2gFT3hHbY2kzMlo',
#        'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011%2Cp_72%3A1248882011&dc&ds=v1%3AUjgJK81tG6lcG%2FfMJMe9HkNu%2F71AYcjT2PD02yWiac4&qid=1677509387&rnid=1248877011&ref=sr_nr_p_72_4',
#        'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292115011%2Cp_72%3A1248882011&dc&ds=v1%3AUjgJK81tG6lcG%2FfMJMe9HkNu%2F71AYcjT2PD02yWiac4&qid=1677509387&rnid=1248877011&ref=sr_nr_p_72_4',
#        'https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A196601011%2Cp_72%3A1248870011&dc&ds=v1%3AjeglV9TwgcFx2ee60dk0ZeVrJfI8knM7%2F%2Famb%2FOcpXU&qid=1677510546&rnid=1248865011&ref=sr_nr_p_72_4',
#        'https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A239225011%2Cp_72%3A1248870011&dc&ds=v1%3AONU8Fa7Wd7b44fT9Of7dLFh%2BVzcayp7oASqq1P7fQ%2FE&qid=1677510861&rnid=1248865011&ref=sr_nr_p_72_4',
#        'https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A679255011%2Cp_72%3A2661621011&dc&qid=1677511055&rnid=2661617011&ref=sr_pg_1',
#        'https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A2474936011%2Cp_72%3A2661621011&s=price-asc-rank&dc&qid=1677511455&rnid=2661617011&ref=sr_st_price-asc-rank&ds=v1%3AKPf33IisPiAWxv5QdDu4IcRSuUnIM00rw9uqt%2FSYDcU',]


# # driver.get(web[0])
# # for i in range(100):
# #     try:
# #         print(i)
# #         links = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
# #         print(len(links))

# #         for link in links:
# #             data.append(link.get_attribute('href'))


# #         next_button = driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
# #         action = ActionChains(driver)
# #         action.click(next_button).perform()

# #         time.sleep(3)
# #     except:
# #         break
    

# # data = pd.DataFrame(data,columns=['Links'])
# # data.to_csv('links1.csv',index=False)
# # # data = []

# driver.get(web[8])
# for i in range(100):
#     try:
#         print(i)
#         links = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
#         print(len(links))

#         for link in links:
#             data.append(link.get_attribute('href'))


#         next_button = driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
#         action = ActionChains(driver)
#         action.click(next_button).perform()

#         time.sleep(3)
#     except:
#         break

# data = pd.DataFrame(data,columns=['Links'])
# data.to_csv('links9.csv',index=False)
# data = []

# driver.get(web[2])
# for i in range(400):
#     try:
#         print(i)
#         links = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

#         for link in links:
#             data.append(link.get_attribute('href'))


#         next_button = driver.find_element(By.XPATH,'//a[@class = "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
#         action = ActionChains(driver)
#         action.click(next_button).perform()

#         time.sleep(3)
#     except:
#         break

# data = pd.DataFrame(data,columns=['Links'])
# data.to_csv('links3.csv',index=False)
# data = []

# driver.get(web[3])
# for i in range(400):
#     try:
#         print(i)
#         links = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')

#         for link in links:
#             data.append(link.get_attribute('href'))


#         next_button = driver.find_element(By.XPATH,'//a[@class = "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
#         action = ActionChains(driver)
#         action.click(next_button).perform()

#         time.sleep(3)
#     except:
#         break

# data = pd.DataFrame(data,columns=['Links'])
# data.to_csv('links4.csv',index=False)
# data = []


# driver.close()


files = ['links1.csv','links2.csv','links3.csv','links4.csv','links5.csv','links6.csv','links7.csv','links8.csv']

data = []

for file in files:
    x = pd.read_csv(file)
    data.append(x)
    
data = pd.concat(data)
data.to_csv('link.csv',index=False)


