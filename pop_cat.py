#!/usr/bin/env python
# coding: utf-8


#chrome 要改成94版本
from time import sleep
from selenium import webdriver


import os
path = "/Users/linyuci/Downloads/chromedriver 3"

print(path)


driver = webdriver.Chrome(path)
driver.get("https://popcat.click/")
a=driver.find_element_by_xpath('//*[@id="app"]/div')
while True:
    a.click()
    sleep(0.055)

