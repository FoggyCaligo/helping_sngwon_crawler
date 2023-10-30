import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

checkboxes = browser.find_elements(By.NAME,'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

# items_to_select= ['영업이익', '자산총계','매출액']
items_to_select= ['시가', '고가','저가']

for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH,'..')
    label = parent.find_element(By.TAG_NAME, 'label')
    #  
    if(label.text in items_to_select):
        checkbox.click() 

 
btn_apply = browser.find_element(By.XPATH,'//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]')
btn_apply.click()

for index in range(1,40):
    browser.get(url+str(index))


    df = pd.read_html(browser.page_source)[1]

    df.dropna(axis='index',how='all', inplace=True)
    df.dropna(axis='columns',how='all',inplace=True)
    if len(df)==0:
        break
    # print(df.head(10))

    f_name = 'sise.csv'
    if os.path.exists(f_name):
        df.to_csv(f_name, encoding='utf-8-sig',index=False, mode='a', header = False)
    else:
        df.to_csv(f_name,encoding='utf-8-sig', index=False)

    print(f'{index}페이지 완료')

browser.quit()
