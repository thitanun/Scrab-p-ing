import os
import tweepy as tw
import pandas as pd
import re
import nltk
import json
import numpy as np
from wordcloud import WordCloud,STOPWORDS
nltk.download('punkt')   
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as nltk_wt
from nltk.stem import PorterStemmer
from textblob import TextBlob
from datetime import datetime,timedelta ,date
from pythainlp.corpus import thai_stopwords
from pythainlp import word_tokenize as pyt_wt
import requests
from sklearn.feature_extraction.text import CountVectorizer
from langdetect import detect


class ClawTwitter:
    def __init__(self): 
        # self.listdata = []
        # self.data = self.get_datatweet()
        self.metadata = {}
        self.setup_dir()
        self.load_meta_data()

    def setup_dir(self):
        if not os.path.exists(f"./data/"): 
            os.mkdir(f"./data/")
        if not os.path.exists(f"./data/tweets/"): 
            os.mkdir(f"./data/tweets/")
            # print("crete folder Successed")
        if not os.path.exists('./data/metadata.json'):
            data = {'keyword' : {}}
            with open('./data/metadata.json', 'w', encoding="UTF-8") as file: #utf-16
                metafile = json.dumps(data, indent=4)
                file.write(metafile)
        
        
    def load_meta_data(self):
        metadata_json = open('./data/metadata.json',encoding="UTF-8")
        self.metadata = json.load(metadata_json)


    def save_meta_data(self):
        with open('./data/metadata.json', 'w', encoding="UTF-8") as file:
            metafile = json.dumps(self.metadata, indent=4)
            file.write(metafile)


    def connect(self):

        consumer_key = 'xxxx'
        consumer_secret = 'xxxx'
        access_token = 'xxxx'
        access_token_secret = 'xxxx'
        

        try:
            auth = tw.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tw.API(auth)
            return api
        except:
            print("Error")
            exit(1)

    def remove_url(txt):
        """Replace URLs found in a text string with nothing 
        (i.e. it will remove the URL from the string).

        Parameters
        ----------
        txt : string
            A text string that you want to parse and remove urls.

        Returns
        ----------
        The same txt string with url's removed.
        """

        return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

    def remove_url_th(txt):
        """Replace URLs found in a text string with nothing 
        (i.e. it will remove the URL from the string).

        Parameters
        ----------
        txt : string
            A text string that you want to parse and remove urls.

        Returns
        ----------
        The same txt string with url's removed.
        """

        return " ".join(re.sub("([^\u0E00-\u0E7Fa-zA-Z' ]|^'|'$|''|(\w+:\/\/\S+))", "", txt).split())

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'(@[A-Za-z0-9_]+)', '', text)
        text = re.sub('http://\S+|https://\S+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text_tokens = nltk_wt(text)
        text = [word for word in text_tokens if not word in stopwords.words()]
        text = ' '.join(text)
        return text


    def clean_text_th(self, text):
        text = re.sub('http://\S+|https://\S+', '', text)
        url = "https://api.aiforthai.in.th/textcleansing"
        params = {f'text':{text}}
        headers = {
            'Apikey': "xxxx",
            }
        res = requests.request("GET", url, headers=headers, params=params)
        # print('test sen', res.json())
        return res.json()['cleansing_text']

    # def clean_text_th(self, text):
    #     url ='https://api.aiforthai.in.th/lextoplus'
    #     headers = {'Apikey':"xxxx"}
        
    #     params = {'text':text,'norm':'1'}
    #     response = requests.get(url, params=params, headers=headers)
    #     return response.json()['tokens']


    def stemmer(self, text):
        porter_text = PorterStemmer()
        token_words = nltk_wt(text)
        stem_word = []
        for word in token_words:
            stem_word.append(porter_text.stem(word))
        return " ".join(stem_word)


    def sentiment(self, text_en):
        sentiment_text = text_en.sentiment.polarity
        if  sentiment_text > 0:
            return 'positive'
        elif sentiment_text < 0:
            return 'negative'
        else:
            return 'neutral'


    def sentiment_th(self, text_th):
        url = "https://api.aiforthai.in.th/ssense"
        params = {'text':text_th}
        headers = {
            'Apikey': "xxxx"
            }
        res = requests.get(url, headers=headers, params=params)
        if res.json()['sentiment']['polarity'] == '':
            polarity = "neutral"
        else:
            polarity = res.json()['sentiment']['polarity']
        # print('hey', res.json())
        return polarity


    def get_datatweet(self, keyword,today):
        if not os.path.exists(f"./data/tweets/{keyword}"):
            os.makedirs(f"./data/tweets/{keyword}")
        api = self.connect()
        # today = datetime.utcnow().date()
        today_str = today.strftime("%Y-%m-%d")
        check_date = today.strftime("%d/%m/%Y")
        tweets= tw.Cursor(api.search_tweets, q = keyword + " -filter:retweets" ,until = today_str).items(100)
                    # since= today_str).items(10)
        tweet_frame = self.dataframe_tweets(tweets,keyword,check_date)
        self.twitter_to_xlsx(keyword,today,tweet_frame)

    def dataframe_tweets(self,tweets,keyword,check_date):
                     
        tweet_list = []    
        for tweet in tweets:
            tweet_list.append(tweet)
        tweets = tweet_list

        data_tweet = [[keyword,
                        self.data_hashtagcount(tweet).upper().count(keyword.upper()) if self.data_hashtagcount(tweet).upper().count(keyword.upper()) > 0 else 1,
                        tweet.user.screen_name,
                        # tweet.lang,
                        tweet.user.location if tweet.user.location != '' else 'unknown',
                        datetime.strftime(tweet.created_at.replace(tzinfo = None) + timedelta(hours = 7),"%d/%m/%Y"),
                        ClawTwitter.remove_url(tweet.text) if tweet.lang == "en" else ClawTwitter.remove_url_th(tweet.text),
                        tweet.retweet_count,
                        tweet.favorite_count,     
                        self.sentiment_th(self.clean_text_th(tweet.text)) 
                        if tweet.lang == "th" else self.sentiment(TextBlob(self.stemmer(self.clean_text(ClawTwitter.remove_url(tweet.text))))),
                        f"https://twitter.com/twitter/statuses/{tweet.id}"] for tweet in tweets if str(datetime.strftime(tweet.created_at.replace(tzinfo = None) + timedelta(hours = 7),"%d/%m/%Y")) == check_date]

        tweet_frame = pd.DataFrame(data=data_tweet,
                            columns=['topic', 'count topic', 'user','location','post date',
                                    'tweet','retweet','likes', 'sentiment','tweet link'])
        return tweet_frame
        

    def twitter_to_xlsx(self,keyword,today,tweet_frame):

        set_today_str = today.strftime("%d%m%Y")
    
        if keyword not in self.metadata['keyword'].keys():
            self.metadata['keyword'][keyword] = {'date' : []}
        
        tweet_frame.to_excel(f"./data/tweets/{keyword}/{keyword}_{set_today_str}.xlsx", engine="openpyxl", index=False)
        if set_today_str not in self.metadata['keyword'][keyword]['date']:
            self.metadata['keyword'][keyword]['date'].append(set_today_str)
            self.save_meta_data()

    def data_hashtagcount(self,tweet):
        entity_ht = tweet.entities.get('hashtags')
        hashtag = ""
        for i in range(0, len(entity_ht)):
            hashtag = hashtag + ",#" + entity_ht[i]['text']
        return hashtag
    

    def tokenize_th(self,d):
        # print('hey', d)
        d = re.sub('[a-z]', '', d)
        d = re.sub('[A-Z]', '', d)
        d = re.sub('[0-9]', '', d)
        # print('test d', d)
        result = d.split(" ")
        result = list(filter(None, result))
        return result
    
    def tokenize_en(self, d):
        # print('hey', d)
        d = re.sub('[ก-๙]', '', d)
        d = re.sub('[0-9]', '', d)
        # print('test d', d)
        result = d.split(" ")
        result = list(filter(None, result))
        return result


    def count_word_en(self,new_text):
    # def count_word_en(dfr):
        # new_text = []
        # for txt in dfr["tweet"]:
        #     new_text.append(test.clean_text(txt))
        
        vectorizer = CountVectorizer(tokenizer=self.tokenize_en)
        transformed_data = vectorizer.fit_transform(new_text)
        # keyword_df_en = pd.DataFrame(columns = ['word', 'count'])
        # keyword_df_en['word'] = vectorizer.get_feature_names_out()
        # keyword_df_en['count'] = np.ravel(transformed_data.sum(axis=0))
        keyword_word = vectorizer.get_feature_names_out()
        keyword_count = np.ravel(transformed_data.sum(axis=0))
        list_countword_en = [[keyword_word[i],keyword_count[i]] for i in range(len(keyword_word))]
        keyword_df_en = pd.DataFrame(data = list_countword_en,columns = ['word', 'count'])
        # topword_en = keyword_df_en.sort_values(by=['count'], ascending=False).head(20)

        return keyword_df_en

    def count_word_th(self,new_text):
        # new_text = []
        # for txt in dfr["tweet"]:
        #     new_text.append(test.clean_text(txt))
        stop_words = thai_stopwords()
        vectorizer = CountVectorizer(tokenizer = self.tokenize_th)
        transformed_data = vectorizer.fit_transform(new_text)
        # keyword_df_th = pd.DataFrame(columns = ['word', 'count'])
        # keyword_df_th['word'] = vectorizer.get_feature_names_out()
        # keyword_df_th['count'] = np.ravel(transformed_data.sum(axis=0))
        keyword_word = vectorizer.get_feature_names_out()
        keyword_count = np.ravel(transformed_data.sum(axis=0))
        list_countword_th = [[keyword_word[i],keyword_count[i]] for i in range(len(keyword_word)) if keyword_word[i] not in stop_words]
        keyword_df_th = pd.DataFrame(data = list_countword_th,columns = ['word', 'count'])
        # topword_en = keyword_df_en.sort_values(by=['count'], ascending=False).head(20)

        return keyword_df_th
    
    def showcount_twitter(self,tweets_data):
        dfr = tweets_data
        new_text_th = []
        new_text_en = []

        for txt in dfr["tweet"]:
            # if type(txt) == str:
            #     new_text_en.append(self.clean_text(txt))
            # for txt_cut in pyt_wt(txt, keep_whitespace=False,engine="multi_cut"):
            # for txt_cut in pyt_wt(txt, keep_whitespace=False,engine="multi_cut"):
            # for txt_cut in clean_text_th(txt):
            #     if txt_cut == '':
            #         pass
            #     else:
                    # new_text_th.append(txt_cut)
            if type(txt) == str:
                if detect(txt) == 'th':
                    new_text_th.append(self.clean_text_th((txt)))
                else:
                    new_text_en.append(self.clean_text(txt))

            # new_text.append(clean_text_th((txt))) 


        # keyword_df_en = self.count_word_en(new_text_en)
        # keyword_df_th = self.count_word_th(new_text_th)
        # frames = [keyword_df_en, keyword_df_th]
        frames = []

        if len(new_text_en) > 0 and len(new_text_th) > 0:
            keyword_df_en = self.count_word_en(new_text_en)
            frames.append(keyword_df_en)
            keyword_df_th = self.count_word_th(new_text_th)
            frames.append(keyword_df_th)
        elif len(new_text_en) > 0 and len(new_text_th) == 0:
            keyword_df_en = self.count_word_en(new_text_en)
            frames.append(keyword_df_en)
        elif len(new_text_th) > 0 and len(new_text_en) == 0:
            keyword_df_th = self.count_word_th(new_text_th)
            frames.append(keyword_df_th)

        result = pd.concat(frames)

        topword = result.sort_values(by=['count'], ascending=False).head(20)
        return topword