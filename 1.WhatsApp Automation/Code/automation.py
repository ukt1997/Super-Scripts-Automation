# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 02:46:59 2020

@author: Ujjwal Kumar

program for: Whatsapp Automation 
"""

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('C:/Users/Your Loaction /chromedriver_win32/chromedriver.exe') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

print("Scan QR Code, And then Enter")
print("Logged In")
input("1. Enter To Move Forward :")
  
contact = "Conatct Name" #Replace it with Contacts Name you want to send Text 
text = "Your Message"

print("Contact and message set ")
input("2. Enter To Move Forward :")

inp_xpath_search = "//div[@class='_3FRCZ copyable-text selectable-text']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.send_keys(contact)
time.sleep(2)

print("Conatct Name  passed in Search Box ")
input("3. Enter To Move Forward :")
#input_box_search.click()
print("Search Enter ")
input("4. Enter To Move Forward :")

selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"'][1]")
selected_contact.click()
print("Enterd Chat Window ")
input("5. Enter To Move Forward :")

inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
print("Chat Text Box Found ")
input("6. Enter To Move Forward :")
for i in range(10):
    input_box.send_keys(text + Keys.ENTER)
    time.sleep(2)
driver.quit()