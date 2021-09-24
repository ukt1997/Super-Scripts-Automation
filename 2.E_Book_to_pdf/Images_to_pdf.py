# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 15:41:59 2021

@author: Ujjwal Kumar

File to Convert Images into PDF File 
images Should be Names as page<start_page_no>.png ---to ---page<end_page_no>.png
 It will Take Base Directory as Present Working Directory 
 
 
"""

from PIL import Image
import os

start = int(input('Create PDF Starting From Page :'))
end = int(input('END PDF on Page :'))

pdf_file_name = input('Enter PDF File Name :')

imglist = []

source_path = os.getcwd()
"""
Update Directory Storing Images Here as per your Directory Name 
"""
directory = '\\<Directory Storing Images>\\'

img_name        = 'page' + str(start) + '.png'
full_img_path   = source_path + directory + img_name
    
img = Image.open(full_img_path)
img1 = img.convert('RGB') # 1st Image 

output_path = source_path + '/' + pdf_file_name + '.pdf'


for i in range(start + 1, end+1):
    img_name        = 'page' + str(i) + '.png'
    full_img_path   = source_path + directory + img_name
    
    img = Image.open(full_img_path)
    img2 = img.convert('RGB')
    imglist.append(img2)

print('Output File : ',output_path)

img1.save(output_path,save_all=True, append_images=imglist)

print('Done')


    
    
    