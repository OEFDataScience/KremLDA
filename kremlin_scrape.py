
# -*- coding: utf-8 -*-
"""
Scraping http://en.kremlin.ru/events/president/transcripts
@author: Clayton Besaw
Base URL: en.kremlin.ru/president/transcripts/page/N: where N: 1..,N...,417
"""
#libraries

from bs4 import BeautifulSoup
import pandas as pd

import time
from urllib.request import urlopen
import tqdm
import pickle

import csv

#necessary variables
base_url = "http://en.kremlin.ru/events/president/transcripts"
info_list = []
page_vector = list(range(1,418))


links = []
info_list1 = []
pbar = tqdm.tqdm(total = len(page_vector))
#THIS COLLECTS TEXT-VERSION-LINKS
for i in page_vector:
    info_dict1 = {}
    key_name1 = 'URL'
    key_name2 = 'Date'
    master_url = 'http://en.kremlin.ru/events/president/transcripts'
    URL = master_url + '/page/' + str(i)
    base_soup = BeautifulSoup(urlopen(URL), 'html.parser')
    transcript_links = base_soup.find_all('a',
                                      {'class':["tabs_article item big", 
                                                 "tabs_article item medium"]})
    #link tags
    for tag in transcript_links:
        links.append(tag.get('href'))
        info_dict1[key_name1] = tag

    
        
    time.sleep(2)
    
    pbar.update(1)
    
pbar.close()



# #save link_list
# with open('links.pkl', 'wb') as fp:
#     pickle.dump(links, fp)
# #load link_list
# with open('links.pkl', 'rb') as fp:
#     links = pickle.load(fp)


#this collects text and URL
base_url = 'http://www.en.kremlin.ru'
info_list = []
pbar = tqdm.tqdm(total = len(links))
for l in links: 
    info_dict = {}
    #find text version of transcript
    transcript_url = l
    full_url = base_url + transcript_url[:29] + '/copy' + transcript_url[29:]
    full_url = 'http://en.kremlin.ru/events/president/transcripts/63275'
    #BS
    transcript = BeautifulSoup(urlopen(full_url), 'html.parser')
    #text
    text_body = transcript.find('textarea')
    text_body2 = text_body.text
    key_name2 = "Text"
    info_dict[key_name2] = text_body2
    #url
    key_name3 = "URL"
    info_dict[key_name3] = full_url
    #orig_url
    key_name4 = "URL2"
    info_dict[key_name4] = l
    
    #append to master list
    info_list.append(info_dict)
    time.sleep(1)
    pbar.update(1)
pbar.close()    




#THIS COLLECTS THE DATA
base_url = 'http://www.en.kremlin.ru'
info_list = []
pbar = tqdm.tqdm(total = len(links))
for l in links: 
    info_dict = {}
    #find text version of transcript
    transcript_url = l
    full_url = base_url + transcript_url
    #BS
    transcript = BeautifulSoup(urlopen(full_url), 'html.parser')
    #extract title
    key_name1 = 'Transcript Title'
    try:
        title = transcript.find('h1', attrs={'class':'entry-title p-name'})
        info_dict[key_name1] = title.text
    except AttributeError:
        info_dict[key_name1] = ' '
    #summary
    key_name2 = 'Summary'
    try:
        summary = transcript.find('div', attrs={'class':'read__lead entry-summary p-summary'})
        info_dict[key_name2] = summary.text
    except AttributeError:
        info_dict[key_name2] = ' '   
    #date
    key_name3 = 'Date'
    try:
        date = transcript.find('time', attrs={'itemprop':'datePublished'})
        info_dict[key_name3] = date.text
    except AttributeError:
        info_dict[key_name3] = ' '
    #time-published
    key_name4 = 'Pub-Time'
    try:
        ptime = transcript.find('div', attrs={'class':'read__time'})
        info_dict[key_name4] = ptime.text
    except AttributeError:
        info_dict[key_name4] = 'Unknown'
    #location
    key_name5 = "Location"
    try:
        loc = transcript.find('div', attrs={'class':'read__place p-location'})
        info_dict[key_name5] = loc.text
    except AttributeError:
        info_dict[key_name5] = 'Unknown'
    #text
    key_name6 = 'Text'
    try:
        text = transcript.find('div', attrs={'itemprop':'articleBody'})
        info_dict[key_name6] = text.text
    except AttributeError:
        info_dict[key_name6] = ' '
    #url
    key_name7 = "URL"
    info_dict[key_name7] = full_url
    #orig_url
    key_name8 = "URL2"
    info_dict[key_name8] = l    
    #topics
    key_name9 = "Topics"
    try:
        topics = transcript.find('li', attrs={'class':'p-category'})
        info_dict[key_name9] = topics.text
    except AttributeError:
        info_dict[key_name9] = ' '
    
    #append to master list
    info_list.append(info_dict)
    pbar.update(1)
    time.sleep(2)
    
pbar.close()    


#now create pandas data frame and export to .csv
df = pd.DataFrame(info_list)  
df.to_csv("putin_scrape.csv", index = False, header = True, 
          encoding = 'utf-8')
df.to_pickle("putin_scape.pkl")












    


    
