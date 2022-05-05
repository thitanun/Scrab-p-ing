from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import os
import collectTwitter
import pandas as pd
from datetime import datetime,timedelta ,date
import json

class Ui_main_twit(object):
    def setupUi(self, main_twit):

        main_twit.setObjectName("main_twit")
        main_twit.resize(882, 593)

        self.ht_label = QtWidgets.QLabel(main_twit)
        self.ht_label.setGeometry(QtCore.QRect(30, 60, 191, 31))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.ht_label.setFont(font)
        self.ht_label.setObjectName("ht_label")

        self.ent_ht = QtWidgets.QLineEdit(main_twit)
        self.ent_ht.setGeometry(QtCore.QRect(30, 90, 191, 31))
        self.ent_ht.setObjectName("ent_ht")

        self.search_bttn_ht = QtWidgets.QPushButton(main_twit)
        self.search_bttn_ht.setGeometry(QtCore.QRect(90, 170, 75, 23))
        self.search_bttn_ht.setObjectName("search_bttn_ht")
        self.search_bttn_ht.clicked.connect(self.search_keyword)

        self.keyword_data = QtWidgets.QListWidget(main_twit)
        self.keyword_data.setGeometry(QtCore.QRect(30, 260, 191, 261))
        self.keyword_data.setObjectName("keyword_data")
        self.keyword_data.doubleClicked.connect(self.show_data_in_database)


        self.ht_label_2 = QtWidgets.QLabel(main_twit)
        self.ht_label_2.setGeometry(QtCore.QRect(30, 220, 191, 31))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.ht_label_2.setFont(font)
        self.ht_label_2.setObjectName("ht_label_2")

        self.start_date = QtWidgets.QDateEdit(main_twit)
        self.start_date.setGeometry(QtCore.QRect(30, 130, 81, 22))
        self.start_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QtCore.QDate.currentDate())
        self.start_date.setDisplayFormat("dd/MM/yyyy")
        self.start_date.setObjectName("start_date")


        self.stop_date = QtWidgets.QDateEdit(main_twit)
        self.stop_date.setGeometry(QtCore.QRect(140, 130, 81, 22))
        self.stop_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.stop_date.setCalendarPopup(True)
        self.stop_date.setDate(QtCore.QDate.currentDate())
        self.stop_date.setDisplayFormat("dd/MM/yyyy")
        self.stop_date.setObjectName("start_date")


        self.label = QtWidgets.QLabel(main_twit)
        self.label.setGeometry(QtCore.QRect(120, 120, 47, 41))
        self.label.setObjectName("label")

        self.tabWidget = QtWidgets.QTabWidget(main_twit)
        self.tabWidget.setGeometry(QtCore.QRect(250, 20, 611, 551))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.table_box = QtWidgets.QTableWidget(self.tab)
        self.table_box = QtWidgets.QTableWidget(self.tab)
        self.table_box.setGeometry(QtCore.QRect(0, 0, 611, 531))
        self.table_box.setObjectName("table_box")
        self.table_box.setColumnCount(0)
        self.table_box.setRowCount(0)

        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.count_box = QtWidgets.QTableWidget(self.tab_2)
        self.count_box.setGeometry(QtCore.QRect(0, 0, 611, 531))
        self.count_box.setObjectName("count_box")
        self.count_box.setColumnCount(0)
        self.count_box.setRowCount(0)

        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.table_box_3 = QtWidgets.QTableWidget(self.tab_3)
        self.table_box_3.setGeometry(QtCore.QRect(0, 0, 611, 531))
        self.table_box_3.setObjectName("table_box_3")
        self.table_box_3.setColumnCount(0)
        self.table_box_3.setRowCount(0)

        self.tabWidget.addTab(self.tab_3, "")

        self.progress_bar = QtWidgets.QProgressBar(main_twit)
        self.progress_bar.setGeometry(QtCore.QRect(30, 540, 191, 23))
        self.progress_bar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progress_bar.setProperty("value", 100)
        self.progress_bar.setObjectName("progress_bar")

        self.today_lb = QtWidgets.QLabel(main_twit)
        self.today_lb.setGeometry(QtCore.QRect(30, 10, 141, 16))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.today_lb.setFont(font)
        self.today_lb.setObjectName("today_lb")

        self.current_date_lb = QtWidgets.QLabel(main_twit)
        self.current_date_lb.setGeometry(QtCore.QRect(30, 30, 191, 16))

        font = QtGui.QFont()
        font.setPointSize(10)


        self.current_date_lb.setFont(font)
        self.current_date_lb.setObjectName("current_date_lb")

        self.retranslateUi(main_twit)
        QtCore.QMetaObject.connectSlotsByName(main_twit)

        self.check_date()
        self.check_keyword()
        self.update_keyword()
        self.progress_bar.hide()

        self.colTwitter = collectTwitter.ClawTwitter()

        self.answer_confirm = False

    def retranslateUi(self, main_twit):
        _translate = QtCore.QCoreApplication.translate
        main_twit.setWindowTitle(_translate("main_twit", "SCRAB(P)ing TWITTER"))
        self.ht_label.setText(_translate("main_twit", "HASHTAG"))
        self.search_bttn_ht.setText(_translate("main_twit", "SEARCH"))
        self.ht_label_2.setText(_translate("main_twit", "DATABASE"))
        self.start_date.setDisplayFormat(_translate("main_twit", "dd/MM/yyyy"))
        self.stop_date.setDisplayFormat(_translate("main_twit", "dd/MM/yyyy"))
        self.label.setText(_translate("main_twit", "to"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("main_twit", "Data Twitter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("main_twit", "Data Count"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("main_twit", "Sentiment"))
        self.today_lb.setText(_translate("main_twit", "TODAY"))
        self.current_date_lb.setText(_translate("main_twit","TODAY"))



    def no_text_in_ent_ht(self): # Warning if entry have no text
        warn_ent = QtWidgets.QMessageBox()
        warn_ent.setIcon(QtWidgets.QMessageBox.Warning)
        warn_ent.setWindowTitle("Box is empty!")
        warn_ent.setText("Please enter text before you search")
        warn_ent.setStandardButtons(QtWidgets.QMessageBox.Ok )
        warn_ent.buttonClicked.connect(lambda:warn_ent.close())

        a = warn_ent.exec_() 
    
    def no_data_in_dataframe(self): # Warning if dataframe is empty
        warn_data_ent = QtWidgets.QMessageBox()
        warn_data_ent.setIcon(QtWidgets.QMessageBox.Warning)
        warn_data_ent.setWindowTitle("Empty")
        warn_data_ent.setText("Data is empty!")
        warn_data_ent.setStandardButtons(QtWidgets.QMessageBox.Ok )
        warn_data_ent.buttonClicked.connect(lambda:warn_data_ent.close())

        w = warn_data_ent.exec_() 


    def check_date(self): #check date 
        today = datetime.utcnow().date() 
        today_str = today.strftime("%d-%m-%Y")
        self.current_date_lb.setText(today_str)


    def check_keyword(self): #check keysword
        self.al_search = os.listdir("./data/tweets")


    def update_keyword(self): #update_keyword
        self.keyword_data.clear()
        for i in self.al_search:
            self.keyword_data.addItem(i)


    def conf_to_search(self): #ask for confirm to search data
        sure_ent = QtWidgets.QMessageBox()
        sure_ent.setIcon(QtWidgets.QMessageBox.Critical)
        sure_ent.setWindowTitle("New Keyword")
        sure_ent.setText("This keyword is not in database\n Do you want to continue?")
        sure_ent.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        sure_ent.buttonClicked.connect(self.answer_bttn)

        a = sure_ent.exec_() 

    
    def conf_to_search_date(self, date_start, date_stop): #ask for confirm to search date
        sure_date_ent = QtWidgets.QMessageBox()
        sure_date_ent.setIcon(QtWidgets.QMessageBox.Critical)
        sure_date_ent.setWindowTitle("New Date")
        sure_date_ent.setText(f"This keyword have no data between {date_start} - {date_stop}\n Do you want to continue?")
        sure_date_ent.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        sure_date_ent.buttonClicked.connect(self.answer_bttn)

        a = sure_date_ent.exec_() 



    def answer_bttn(self, conf): #button when program ask to continue
        if conf.text() == "OK":
            self.answer_confirm = True
        else:
            self.answer_confirm = False


    def search_keyword(self):
        keyword = self.ent_ht.text()
        date_start = self.start_date.date().toPyDate()
        date_stop = self.stop_date.date().toPyDate()

        if keyword == "": #if user doesn't enter anything
            self.no_text_in_ent_ht()

        elif keyword not in self.al_search and keyword != "": #if keyword is not in database
            self.conf_to_search()

        elif date_start.strftime('%d%m%Y') not in self.colTwitter.metadata['keyword'][keyword]['date'] or date_stop.strftime('%d%m%Y') not in self.colTwitter.metadata['keyword'][keyword]['date']: #if keyword have no data at that date

            self.conf_to_search_date(date_start, date_stop)

        if self.answer_confirm:
            self.progress_bar.show()
            self.progress_bar.setValue(int(25)) 
            self.check_keyword()
            self.update_keyword()
            self.get_data_twitter()
        elif keyword in self.al_search and keyword != "" and date_start.strftime('%d%m%Y') in self.colTwitter.metadata['keyword'][keyword]['date'] and date_stop.strftime('%d%m%Y') in self.colTwitter.metadata['keyword'][keyword]['date']:
            self.progress_bar.show()
            self.progress_bar.setValue(int(25)) 
            self.get_data_twitter()
        else:
            pass
    
    def show_data_in_database(self): #show selected word when double clicked at database
        self.ent_ht.setText(self.keyword_data.selectedItems()[0].text())


    def show_data_table(self, data): #show data on table
        head_col = list(data.head(0))
        len_file_col = len(head_col)
        len_file_row = len(data)

        self.table_box.clear()
        self.table_box.setRowCount(0)
        self.table_box.setColumnCount(len_file_col)
        self.table_box.setRowCount(len_file_row)
        self.progress_bar.setValue(int(65)) 
        for n, key in enumerate(data.keys()): # add item
            for m, item in enumerate(data[key]):
                if type(item) == float:
                    float_item = round(item,3)
                    newitem = QTableWidgetItem(str(float_item))
                else:
                    newitem = QTableWidgetItem(str(item))
                self.table_box.setItem(m, n, newitem)
        self.table_box.setHorizontalHeaderLabels(head_col)
        self.table_box.verticalHeader().hide()     
        self.table_box.show()



    def formdate(self,date_start,date_stop):# form date

        diff_deltadays = date_stop - date_start 
        diff_days = diff_deltadays.days #int
        return diff_days


    def get_data_twitter(self):
        keyword = self.ent_ht.text().upper()
        date_start = self.start_date.date().toPyDate()
        date_stop = self.stop_date.date().toPyDate()
        diff_days = self.formdate(date_start,date_stop)
        dataframe = []

        for i in range(diff_days+1):
            date_add = date_start + timedelta(days = int(i))
            date_addstr = date_add.strftime("%Y-%m-%d")
            date_filestr = date_add.strftime("%d%m%Y")
            try: #read file in folder
                df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}_{date_filestr}.xlsx", engine="openpyxl")
                dataframe.append(df)

            except:
                self.progress_bar.setValue(int(25))
                try:
                    self.colTwitter.get_datatweet(keyword,date_add) #add file in folder
                    self.check_keyword()
                    self.update_keyword()
                    df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}_{date_filestr}.xlsx", engine="openpyxl")#read file in folder
                    dataframe.append(df)
                except:
                    data_tweet = [] # data frame empty
                    df = pd.DataFrame(data=data_tweet,columns=['topic', 'count topic', 'user','location','post date',
                                'tweet','retweet','likes', 'sentiment','tweet link'])
                    dataframe.append(df)
                    self.save_metadata(keyword)
        self.progress_bar.setValue(int(50))
        result = pd.concat(dataframe)
        self.show_data_table(result )#show table 
        count_frame = self.colTwitter.showcount_twitter(result) # dataframe count
        self.show_count_table(count_frame) #show dataframe count
        self.show_sentiment_table(result) #show dataframe sentiment
        self.check_keyword() #check keyword
        self.update_keyword()  #update keyword

    def save_metadata(self,keyword): #save metadata when dataframe empty and new keys
        metadata_json = open('./data/twitterdata.json',encoding="UTF-8")
        metadata = json.load(metadata_json)
        with open('./data/twitterdata.json', 'w', encoding="UTF-8") as file:
            if keyword not in metadata.keys():
                metadata["keyword"][keyword] = {}
                metadata["keyword"][keyword]['date'] = []
                metafile = json.dumps(metadata, indent=4)
            file.write(metafile)

    def show_count_table(self, data):
        self.progress_bar.setValue(int(70))  
        head_col = list(data.head(0))
        len_file_col = len(head_col)
        len_file_row = len(data)

        self.count_box.clear()
        self.count_box.setRowCount(0)
        self.count_box.setColumnCount(len_file_col)
        self.count_box.setRowCount(len_file_row)
        for n, key in enumerate(data.keys()): # add item
            for m, item in enumerate(data[key]):
                if type(item) == float:
                    float_item = round(item,3)
                    newitem = QTableWidgetItem(str(float_item))
                else:
                    newitem = QTableWidgetItem(str(item))
                self.count_box.setItem(m, n, newitem)
        self.count_box.setHorizontalHeaderLabels(head_col)
        self.count_box.verticalHeader().hide()    
        self.count_box.show()
        self.progress_bar.setValue(int(90))  

        
    def show_sentiment_table(self,data):
        ne_count,pos_count,neg_count,per_ne,per_pos,per_neg = self.sentiment_cal_count(data)
        datasentiment_count = self.sentiment_count_frame(ne_count,pos_count,neg_count,per_ne,per_pos,per_neg)
        head_col = list(datasentiment_count.head(0))
        len_file_col = len(head_col)
        len_file_row = len(datasentiment_count)
        self.table_box_3.clear()
        self.table_box_3.setRowCount(0)
        self.table_box_3.setColumnCount(len_file_col)
        self.table_box_3.setRowCount(len_file_row)
        for n, key in enumerate(datasentiment_count.keys()): # add item
            for m, item in enumerate(datasentiment_count[key]):
                if type(item) == float:
                    float_item = round(item,3)
                    newitem = QTableWidgetItem(str(float_item))
                else:
                    newitem = QTableWidgetItem(str(item))
                self.table_box_3.setItem(m, n, newitem)
        self.table_box_3.setHorizontalHeaderLabels(head_col)
        self.table_box_3.verticalHeader().hide()    
        self.table_box_3.show()
        self.progress_bar.setValue(int(100))  


    def sentiment_cal_count(self,data): #calculate sentiment

        sentiment_data = list(data['sentiment'])
        neutral_count = 0
        positive_count = 0
        negative_count = 0

        try:
            for sen in sentiment_data:# check polarity
                if sen == 'neutral':
                    neutral_count += 1
                elif sen == 'positive':
                    positive_count += 1
                elif sen == 'negative':
                    negative_count += 1
            all_percent = neutral_count+positive_count+negative_count
            percent_neutral = neutral_count/all_percent * 100     # percent polarity
            percent_positive = positive_count/all_percent * 100
            percent_negative = negative_count/all_percent * 100
        except:
            percent_neutral = 0
            percent_positive = 0
            percent_negative = 0
        return neutral_count,positive_count,negative_count,percent_neutral,percent_positive,percent_negative

    def sentiment_count_frame(self,ne_count,pos_count,neg_count,per_ne,per_pos,per_neg): #dataframe
        list_dataframe = [['neutral',ne_count,per_ne],['positive',pos_count,per_pos],['negative',neg_count,per_neg]]
        data_frame = pd.DataFrame(data=list_dataframe,columns=['sentiment','total','percent'])

        return data_frame