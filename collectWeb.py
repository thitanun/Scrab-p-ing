import pandas as pd
import re
import nltk
import json
from wordcloud import WordCloud,STOPWORDS
nltk.download('punkt')   
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as nltk_wt
from nltk.stem import PorterStemmer
from textblob import TextBlob
# from pythainlp.corpus import thai_stopwords
from pythainlp import word_tokenize as pyt_wt


class ClawWeb:

    def sentiment(self, text_en):
        sentiment_text = text_en.sentiment.polarity
        if  sentiment_text > 0:
            return 'positive'
        elif sentiment_text < 0:
            return 'negative'
        else:
            return 'neutral'

    def stemmer(self, text):
        porter_text = PorterStemmer()
        token_words = nltk_wt(text)
        stem_word = []
        for word in token_words:
            stem_word.append(porter_text.stem(word))
        return " ".join(stem_word)

    
    def get_data(self, keyword):

        key_sc = keyword
        list_filedata = ['./testWeb/Thaiger.json','./testWeb/YouZap.json','./testWeb/NME.json',
                        './testWeb/Sudsapda.json','./testWeb/KBS.json','./testWeb/Koreaboo.json',
                        './testWeb/HelloKpop.json','./testWeb/Korism.json','./testWeb/Seoulme.json',
                        './testWeb/Brighttv.json']
                        # './testWeb/Brighttv.json','./testWeb/Nineentertain.json']
        list_dataframe = []
        for i in list_filedata:
            file = open(i, "r")
            datafile = json.loads(file.read())
            file.close()
            data_web = [[data,
                    datafile['web'][data]['title'],
                    key_sc,
                    datafile['web'][data]['content'].upper().count(key_sc.upper()),
                    self.sentiment(TextBlob(self.stemmer(datafile['web'][data]['content']))),
                    # sentiment(TextBlob(datafile['web'][data]['content']))),
                    # if tweet.lang == "en" else self.sentiment_th(self.clean_text_th(tweet.text)
                    ] for data in datafile['web'] if key_sc.upper() in datafile['web'][data]['content'].upper()]
            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','word', 'count','sentiment']).sort_values(by=['count'], ascending=False)
            list_dataframe.append(web_frame)
        all_web_frame = pd.concat(list_dataframe)
        return all_web_frame


    # def webtwitter_to_xlsx(self, all_web_framekeyword):  
        
    #     tweet_frame.to_excel(f"./data/tweets/{keyword}/{keyword}_{set_today_str}.xlsx", engine="openpyxl", index=False)