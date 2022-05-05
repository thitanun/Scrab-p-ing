import re
import os
import json
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from collections import Counter


class testThaiger:

    def __init__(self):
        self.data = {}
        self.data['web'] = {}
        self.webdata = {}
        # self.webdata['website'] = {}
        # self.webdata['website'] = {}
        self.setup_dir()
        self.load_meta_data()


    def setup_dir(self):
        if not os.path.exists('./data/webdata.json'):
            data = {'website' : {}}
            with open('./data/webdata.json', 'w', encoding="UTF-8") as file: #utf-16
                metafile = json.dumps(data, indent=4)
                file.write(metafile)
        
        
    def load_meta_data(self):
        webdata_json = open('./data/webdata.json',encoding="UTF-8")
        self.webdata = json.load(webdata_json)


    def data_domain_for_ref(self, session, url):
        with session.get(url) as response:
            if not response.ok:
                return
            domain = urlparse(url).netloc
            bs = BeautifulSoup(response.text, 'html.parser')
            bs = self.remove_unuse_tag(bs)
            # print('test bs domain', bs)

            news_link = []
            list_link = []
            for li in bs.find_all('li', {'class' : 'mvp-blog-story-wrap left relative infinite-post'}):
                a = li.find('a')
                news_link.append(a.attrs['href'])
                for i in news_link:
                    list_link.append(i)


            self.webdata['website']['thethaiger.com'] = list_link


    def scrap_for_ref(self):
        pages_list = [f'https://thethaiger.com/th/entertainment/korean-entertainment/page/{i}' for i in range(1, 11)]
        n = len(pages_list)
        print('test page', pages_list)
        with ThreadPoolExecutor(max_workers=n) as executor:
            with requests.Session() as session:
                executor.map(self.data_domain_for_ref, [session]*n, pages_list)
                executor.shutdown(wait=True)

    
    def remove_unuse_tag(self, bs : BeautifulSoup):
        unuse_tag = ['script', 'style ', 'noscript', 'head', 'footer', 'iframe']
        for tag in unuse_tag:
            for s in bs.select(tag):
                if s != None:
                    s.extract()
        return bs

    def clean_html(self, html : str):
        clean = re.compile('<.*?>')
        clean_text = re.sub(clean, '', html)
        for char in ['\n', '\t', '\r']:
            clean_text = clean_text.replace(char, '')
        clean_text = re.sub(' +', ' ', clean_text)
        return clean_text

    def data_in_link(self, session, url):
        self.list_url = []
        self.list_title = []
        self.list_content = []

        with session.get(url) as response:
            if not response.ok:
                return
            print('test url', url)
            
            domain = urlparse(url).netloc
            bs = BeautifulSoup(response.text, 'html.parser')
            bs = self.remove_unuse_tag(bs)
            # print('test bs inlink', bs)
            
            self.data['web'][url] = {}
            self.data['web'][url]['title'] = bs.find('h1').text

            self.content = ''
            section = bs.find('div', {'id' : 'mvp-content-main'})
            for p in section.find_all('p'):
                self.content += f'{self.clean_html(p.text)} ' #p.text
            self.data['web'][url]['content'] = self.content
            # print('test content inlink', self.content)



    def data_domain(self, session, url):
        with session.get(url) as response:
            if not response.ok:
                return
            domain = urlparse(url).netloc
            bs = BeautifulSoup(response.text, 'html.parser')
            bs = self.remove_unuse_tag(bs)
            # print('test bs domain', bs)

            news_link = []
            for li in bs.find_all('li', {'class' : 'mvp-blog-story-wrap left relative infinite-post'}):
                a = li.find('a')
                news_link.append(a.attrs['href'])
            # print('test news_link domain', news_link)

            n = len(news_link)
            # print('test n news_link domain', n)
            with ThreadPoolExecutor(max_workers=n) as executor:
                with requests.Session() as session:
                    executor.map(self.data_in_link, [session]*n, news_link)
                    executor.shutdown(wait=True)


    def scrap(self):
        pages_list = [f'https://thethaiger.com/th/entertainment/korean-entertainment/page/{i}' for i in range(1, 11)]
        n = len(pages_list)
        print('test page', pages_list)
        with ThreadPoolExecutor(max_workers=n) as executor:
            with requests.Session() as session:
                executor.map(self.data_domain, [session]*n, pages_list)
                executor.shutdown(wait=True)


    def save_to_json(self):
        with open(f'./WebScrab/Thaiger.json', 'w', encoding="UTF-8") as file:
            datafile = json.dumps(self.data, indent=4) 
            file.write(datafile)

        with open(f'./data/webdata.json', 'w', encoding="UTF-8") as file:
            metafile = json.dumps(self.webdata, indent=4)
            file.write(metafile)


if __name__ == '__main__':
    data = testThaiger()
    data.scrap()
    data.scrap_for_ref()
    data.save_to_json()
