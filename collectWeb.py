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
from pythainlp import word_tokenize as pyt_wt
from WebScrab import testThaiger,testYouZap,testNME,testSudsapda,testKoreaboo,testHelloKpop,\
                        testKorism ,testSeoulme ,testBrighttv ,testKoreajoongangdaily ,testKorseries , \
                        testKpopchannel , testMetro ,testPinkvilla ,testTheguardian , \
                        testTwentyfour ,testHallyukstar ,testKpopmap , testHungerplus ,testThematternews 

class ClawWeb:

    def sentiment(self, text_en): #check sentiment
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

    
    def get_data(self, keyword): #get data from database
        key_sc = keyword
        list_filedata = ['./WebScrab/Thaiger.json','./WebScrab/YouZap.json','./WebScrab/NME.json',
                        './WebScrab/Sudsapda.json','./WebScrab/Koreaboo.json','./WebScrab/HelloKpop.json',
                        './WebScrab/Korism.json','./WebScrab/Seoulme.json','./WebScrab/Brighttv.json',
                        './WebScrab/Koreajoongangdaily.json','./WebScrab/Korseries.json','./WebScrab/Kpopchannel.json',
                        './WebScrab/Metro.json','./WebScrab/Pinkvilla.json','./WebScrab/Theguardian.json',
                        './WebScrab/Twentyfour.json','./WebScrab/Hallyukstar.json','./WebScrab/Kpopmap.json',
                        './WebScrab/Hungerplus.json','./WebScrab/Thematternews.json']
        list_dataframe = []  
        for i in list_filedata:
            file = open(i, "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    if key_sc.upper() in datafile['web'][data]['content'].upper():
                        data_web.append([data,
                                datafile['web'][data]['title'],
                                key_sc,
                                datafile['web'][data]['content'].upper().count(key_sc.upper()),
                                self.sentiment_th((datafile['web'][data]['title']))
                                if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                                ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','word', 'count','sentiment']).sort_values(by=['count'], ascending=False)
            list_dataframe.append(web_frame)
        all_web_frame = pd.concat(list_dataframe)
        return all_web_frame


    def update_get_data(self, keyword): #update data -> new scrap
        key_sc = keyword
        list_dataframe = []

        if key_sc == 'testThaiger':
            for i in [testThaiger]:
                data = i.testThaiger()

            file = open('./WebScrab/Thaiger.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testYouZap':
            for i in [testYouZap]:
                data = i.testYouZap()

            file = open('./WebScrab/YouZap.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testNME':
            for i in [testNME]:
                data = i.testNME()

            file = open('./WebScrab/NME.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)
    
        elif key_sc == 'testSudsapda':
            for i in [testSudsapda]:
                data = i.testSudsapda()

            file = open('./WebScrab/Sudsapda.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testKoreaboor':
            for i in [testKoreaboo]:
                data = i.testKoreaboo()

            file = open('./WebScrab/Koreaboo.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testHelloKpop':
            for i in [testHelloKpop]:
                data = i.testHelloKpop()

            file = open('./WebScrab/HelloKpop.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testKorism':
            for i in [testKorism]:
                data = i.testKorism()

            file = open('./WebScrab/Korism.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testSeoulme':
            for i in [testSeoulme]:
                data = i.testSeoulme()

            file = open('./WebScrab/Seoulme.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testBrighttv':
            for i in [testBrighttv]:
                data = i.testBrighttv()

            file = open('./WebScrab/Brighttv.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testKoreajoongangdaily':
            for i in [testKoreajoongangdaily]:
                data = i.testKoreajoongangdaily()

            file = open('./WebScrab/Koreajoongangdaily.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testKorseries':
            for i in [testKorseries]:
                data = i.testKorseries()

            file = open('./WebScrab/Korseries.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testKpopchannel':
            for i in [testKpopchannel]:
                data = i.testKpopchannel()

            file = open('./WebScrab/Kpopchannel.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testMetro':
            for i in [testMetro]:
                data = i.testMetro()

            file = open('./WebScrab/Metro.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testPinkvilla':
            for i in [testPinkvilla]:
                data = i.testPinkvilla()

            file = open('./WebScrab/Pinkvilla.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)
    
        elif key_sc == 'testTheguardian':
            for i in [testTheguardian]:
                data = i.testTheguardian()

            file = open('./WebScrab/Theguardian.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testTwentyfour':
            for i in [testTwentyfour]:
                data = i.testTwentyfour()

            file = open('./WebScrab/Twentyfour.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testHallyukstar':
            for i in [testHallyukstar]:
                data = i.testHallyukstar()

            file = open('./WebScrab/Hallyukstar.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testKpopmap':
            for i in [testKpopmap]:
                data = i.testKpopmap()

            file = open('./WebScrab/Kpopmap.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        elif key_sc == 'testThematternews':
            for i in [testThematternews]:
                data = i.testThematternews()

            file = open('./WebScrab/Thematternews.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)


        elif key_sc == 'testHungerplus':
            for i in [testHungerplus]:
                data = i.testHungerplus()

            file = open('./WebScrab/Hungerplus.json', "r")
            datafile = json.loads(file.read())
            file.close()

            data_web = []
            for data in datafile['web']:
                try:
                    data_web.append([data,
                            datafile['web'][data]['title'],
                            self.sentiment_th((datafile['web'][data]['title']))
                            if datafile['web'][data]['content'] == "th" else self.sentiment(TextBlob(datafile['web'][data]['title']))
                            ] )
                except:
                    pass

            web_frame = pd.DataFrame(data=data_web,
                            columns=['link','title','sentiment'])
            list_dataframe.append(web_frame)

        all_web_frame = pd.concat(list_dataframe)
        return all_web_frame