import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Crawler:
    def __init__(self):
        self.driver = webdriver.Chrome() 
        #driver.get('https://www.google.co.kr/')
        self.driver.get('https://finance.naver.com/')
        time.sleep(0.5)

    def get_stockprice(self,stockCode):
        searchbox = self.driver.find_element(By.XPATH, '//*[@id="stock_items"]')
        searchbox.send_keys(stockCode)
        searchbox.send_keys(Keys.RETURN)
        time.sleep(1)
        
        price = self.driver.find_element(By.XPATH, '//*[@id="chart_area"]/div[1]/div/p[1]/em')
        price_txt = price.text
        rsult = ""
        for c in price_txt:
            if(c == ',' or c=="\n"): continue
            else : rsult += c
        return int(rsult)





crawler = Crawler()

stock_ls = ['005930', '005940', '005950']
for i in stock_ls:
    print(crawler.get_stockprice(i))

