import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import matplotlib.pyplot as plt
import numpy as np

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



class Main:
    def __init__(self):
        self.crawler = Crawler()
        self.stock_ls = ['005930', '005940', '005950']
        self.price_ls = []

    def update(self):
        self.price_ls = []
        for each in self.stock_ls:
            self.price_ls.append(self.crawler.get_stockprice(each))
            
    def show_graph(self):
        self.update()
        x = np.arange(len(self.stock_ls))
        plt.bar(x,self.price_ls)
        plt.xticks(x,self.stock_ls)
        plt.show()
        pass




main = Main()

main.update()
main.show_graph()

