
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as r
import urllib.request
import os
import re
import cv2
import numpy as np
import glob

team_urls = []
teams_page = r.get('http://mclachbot.com/passmap_for_league/EPL/2022')
team_soup = bs(teams_page.text, 'html.parser')
for link in team_soup.find_all('a'):
    l = link.get('href')
    if 'passmap_list' in l:
        team_urls.append(l)
for t in team_urls:
            
    #extract team name from team url
    result = re.search('http:\/\/.+?\/.+?\/(.+?)\/', t)
    team_name = result.group(1)
    
    #create directory for team if it doesn't exist and set dir variable
    if not os.path.exists(f'/Users/noahherring-black/Desktop/epl-pass-maps/{team_name}'): 
        os.mkdir(f'/Users/noahherring-black/Desktop/epl-pass-maps/{team_name}')
    
    dir = f'/Users/noahherring-black/Desktop/epl-pass-maps/{team_name}'


    # create soup for team pages
    page = r.get(t)
    soup = bs(page.text, 'html.parser')
    

    #download pass map images and save in team directory
    for link in soup.find_all('a'):
        l = link.get('href').replace(' ','_')
        if '/passmap/' in l:
            l_result = re.search('http:\/\/.+?\/.+?\/.+?\/(.+)', l)
            file_name = l_result.group(1)
            try:
                if not os.path.exists(f'{dir}/{file_name}.jpg'):
                    urllib.request.urlretrieve(l, f'{dir}/{file_name}.jpg')
            except:
                pass

    #generate video            
    img_array = []
    for filename in sorted(glob.glob(f'/Users/noahherring-black/Desktop/epl-pass-maps/{team_name}/*.jpg')):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    fps = 0.5
    out = cv2.VideoWriter(f'/{dir}/videos/{team_name}_passmaps.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
