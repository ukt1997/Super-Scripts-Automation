# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 13:56:10 2021

@author: Ujjwal Kumar
"""

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

def Open_URL():

	# Replace below path with the absolute path 
	# to chromedriver in your computer 
   #C:\Users\<User Name>\Downloads\chromedriver_win32_new
   driver = webdriver.Chrome('C:/Users/<User Name>/Downloads/chromedriver_win32_new/chromedriver.exe')
   driver.get("< Link to Web E_Book > ")
   wait = WebDriverWait(driver, 600)
   
   
   
   # Entering UserID 
   inp_xpath_search = "/html/body/div[1]/div/md-card/form/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/div[2]/div/md-input-container/input"
   input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
   input_box_search.send_keys('<User-ID>')
   time.sleep(2)
   #/html/body/div[1]/div/md-card/form/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/div[3]/button
   inp_xpath_search = "/html/body/div[1]/div/md-card/form/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/div[3]/button"
   next_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
   next_btn.click()
   time.sleep(2)

   # Entering Password
   inp_xpath_search = "/html/body/div[1]/div/md-card/form/md-tabs/md-tabs-content-wrapper/md-tab-content[4]/div/div[2]/md-input-container/input"
   input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
   input_box_search.send_keys('<Password>')
   time.sleep(2)
   #/html/body/div[1]/div/md-card/form/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/div[3]/button
   inp_xpath_search = "/html/body/div[1]/div/md-card/form/md-tabs/md-tabs-content-wrapper/md-tab-content[4]/div/div[3]/button[2]"
   next_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
   next_btn.click()
   time.sleep(2)
   
   # Selecting Course 
   inp_xpath_search = "/html/body/div[1]/div/md-content/div/div/md-card/div"
   next_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
   next_btn.click()
   time.sleep(10)
   
   cont = input("Continue ? [Y/N] :")
   if cont in ['Y','y']:
       print("continued----")
   else:
       return

   # Removing  Page List  
   """inp_xpath_search = "/html/body/div[1]/md-sidenav/md-content/div/div/div/div/ul/li[1]/ul/li[1]/div/div/div[1]"
   next_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
   next_btn.click()
   time.sleep(2)
   """
   for page_no in range(1,350):
       pic_path = 'E_Book/Page'+ str(page_no)+'.png'
       
       inp_xpath_search = "/html/body/div[1]/div/md-content/div/div/md-card/div/div/div/md-content/div/div[2]/div/div"
       next_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
       next_btn.screenshot(pic_path)
       time.sleep(2)
       
       inp_xpath_search = "/html/body/div[1]/div/button[2]"
       next_btn = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
       next_btn.click()
       time.sleep(10)
       
   
   #driver.execute_script("window.print();")
   
if __name__ == '__main__':
	# Launch Automation 
	Open_URL()
else:
	print("Called with Name "+__name__)