from PyQt5 import QtCore, QtGui, QtWidgets
import collectWeb
from datetime import datetime,timedelta ,date
from PyQt5.QtWidgets import QTableWidgetItem
import pandas as pd
import json
import os


class Ui_main_web(object):
    def setupUi(self, main_webb):
        main_webb.setObjectName("main_webb")
        main_webb.resize(882, 593)

        self.ht_label = QtWidgets.QLabel(main_webb)
        self.ht_label.setGeometry(QtCore.QRect(30, 60, 191, 31))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.ht_label.setFont(font)
        self.ht_label.setObjectName("ht_label")

        self.ent_ht = QtWidgets.QLineEdit(main_webb)
        self.ent_ht.setGeometry(QtCore.QRect(30, 90, 191, 31))
        self.ent_ht.setObjectName("ent_ht")

        self.search_bttn_ht = QtWidgets.QPushButton(main_webb)
        self.search_bttn_ht.setGeometry(QtCore.QRect(80, 130, 75, 23))
        self.search_bttn_ht.setObjectName("search_bttn_ht")
        self.search_bttn_ht.clicked.connect(self.search_keyword)

        self.keyword_data = QtWidgets.QListWidget(main_webb)
        self.keyword_data.setGeometry(QtCore.QRect(30, 290, 191, 231))
        self.keyword_data.setObjectName("keyword_data")
        self.keyword_data.doubleClicked.connect(self.show_data_in_database)

        self.ht_label_2 = QtWidgets.QLabel(main_webb)
        self.ht_label_2.setGeometry(QtCore.QRect(30, 260, 191, 31))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.ht_label_2.setFont(font)
        self.ht_label_2.setObjectName("ht_label_2")

        self.progress_bar = QtWidgets.QProgressBar(main_webb)
        self.progress_bar.setGeometry(QtCore.QRect(30, 540, 191, 23))
        self.progress_bar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progress_bar.setProperty("value", 100)
        self.progress_bar.setObjectName("progress_bar")

        self.today_lb = QtWidgets.QLabel(main_webb)
        self.today_lb.setGeometry(QtCore.QRect(30, 10, 141, 16))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.today_lb.setFont(font)
        self.today_lb.setObjectName("today_lb")

        self.current_date_lb = QtWidgets.QLabel(main_webb)
        self.current_date_lb.setGeometry(QtCore.QRect(30, 30, 191, 16))

        font = QtGui.QFont()
        font.setPointSize(10)
        
        # self.current_date_lb.setText("")
        self.current_date_lb.setFont(font)
        self.current_date_lb.setObjectName("current_date_lb")

        self.tabWidget = QtWidgets.QTabWidget(main_webb)
        self.tabWidget.setGeometry(QtCore.QRect(250, 10, 611, 551))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.data_box = QtWidgets.QTableWidget(self.tab)
        self.data_box.setGeometry(QtCore.QRect(0, 0, 611, 531))
        self.data_box.setObjectName("data_box")
        self.data_box.setColumnCount(0)
        self.data_box.setRowCount(0)

        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.senti_box = QtWidgets.QTableWidget(self.tab_2)
        self.senti_box.setGeometry(QtCore.QRect(0, 0, 611, 531))
        self.senti_box.setObjectName("senti_box")
        self.senti_box.setColumnCount(0)
        self.senti_box.setRowCount(0)

        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.ref_box = QtWidgets.QTableWidget(self.tab_3)
        self.ref_box.setGeometry(QtCore.QRect(0, 0, 611, 531))
        self.ref_box.setObjectName("ref_box")
        self.ref_box.setColumnCount(0)
        self.ref_box.setRowCount(0)

        self.tabWidget.addTab(self.tab_3, "")

        self.ht_label_3 = QtWidgets.QLabel(main_webb)
        self.ht_label_3.setGeometry(QtCore.QRect(30, 160, 191, 31))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.ht_label_3.setFont(font)
        self.ht_label_3.setObjectName("ht_label_3")
        
        self.ent_ht_2 = QtWidgets.QLineEdit(main_webb)
        self.ent_ht_2.setGeometry(QtCore.QRect(30, 190, 191, 31))
        self.ent_ht_2.setObjectName("ent_ht_2")

        self.search_bttn_ht_2 = QtWidgets.QPushButton(main_webb)
        self.search_bttn_ht_2.setGeometry(QtCore.QRect(80, 230, 75, 23))
        self.search_bttn_ht_2.setObjectName("search_bttn_ht_2")
        self.search_bttn_ht_2.clicked.connect(self.update_data)


        self.retranslateUi(main_webb)
        QtCore.QMetaObject.connectSlotsByName(main_webb)

        self.check_date()
        self.update_keyword_data()


        self.progress_bar.hide()

        self.colWeb = collectWeb.ClawWeb()

    def retranslateUi(self, main_webb):
        _translate = QtCore.QCoreApplication.translate
        main_webb.setWindowTitle(_translate("main_webb", "SCRAB(P)ing WEBSITE"))
        self.ht_label.setText(_translate("main_webb", "KEYWORD"))
        self.search_bttn_ht.setText(_translate("main_webb", "SEARCH"))
        self.ht_label_2.setText(_translate("main_webb", "DATABASE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("main_twit", "Data Website"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("main_twit", "Sentiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("main_twit", "Reference"))
        self.today_lb.setText(_translate("main_webb", "TODAY"))
        self.current_date_lb.setText(_translate("main_webb","TODAY"))
        self.ht_label_3.setText(_translate("main_twit", "LINK"))
        self.search_bttn_ht_2.setText(_translate("main_twit", "UPDATE"))


    def update_keyword_data(self): #add web to database box
        self.keyword_data.addItem("Thaiger")
        self.keyword_data.addItem("YouZap") 
        self.keyword_data.addItem("NME")
        self.keyword_data.addItem("Sudsapda")
        self.keyword_data.addItem("Koreaboo")
        self.keyword_data.addItem("HelloKpop")
        self.keyword_data.addItem("Korism")
        self.keyword_data.addItem("Seoulme")
        self.keyword_data.addItem("Brighttv")
        self.keyword_data.addItem("Koreajoongangdaily")
        self.keyword_data.addItem("Korseries")
        self.keyword_data.addItem("Kpopchannel")
        self.keyword_data.addItem("Metro")
        self.keyword_data.addItem("Pinkvilla")
        self.keyword_data.addItem("Theguardian")
        self.keyword_data.addItem("Twentyfour")
        self.keyword_data.addItem("Hallyukstar")
        self.keyword_data.addItem("Kpopmap")
        self.keyword_data.addItem("Hungerplus")
        self.keyword_data.addItem("Thematternews")

    def show_data_in_database(self): #show selected website when double clicked at database
        self.ent_ht_2.setText(self.keyword_data.selectedItems()[0].text())

    def check_date(self):
        today = datetime.utcnow().date()
        today_str = today.strftime("%d-%m-%Y")
        self.current_date_lb.setText(today_str)

    
    def no_text_in_ent_ht(self): # Warning if entry have no text
        warn_ent = QtWidgets.QMessageBox()
        warn_ent.setIcon(QtWidgets.QMessageBox.Warning)
        warn_ent.setWindowTitle("Box is empty!")
        warn_ent.setText("Please enter text before you search")
        warn_ent.setStandardButtons(QtWidgets.QMessageBox.Ok ) #| QtWidgets.QMessageBox.Cancel)
        warn_ent.buttonClicked.connect(lambda:warn_ent.close())

        a = warn_ent.exec_() 

    def conf_to_search(self): #ask for confirm to search data
        sure_ent = QtWidgets.QMessageBox()
        sure_ent.setIcon(QtWidgets.QMessageBox.Warning)
        sure_ent.setWindowTitle("Not in database")
        sure_ent.setText("Keyword not in database")
        sure_ent.setStandardButtons(QtWidgets.QMessageBox.Ok)
        sure_ent.buttonClicked.connect(lambda:sure_ent.close())

        a = sure_ent.exec_() 

    
    def update_data(self): #update data from database
        keyword = self.ent_ht_2.text()
        list_web = ["Thaiger", "YouZap","NME","Sudsapda","Koreaboo","HelloKpop","Korism","Seoulme",
                    "Brighttv","Koreajoongangdaily","Korseries","Kpopchannel","Metro","Pinkvilla",
                    "Theguardian","Twentyfour","Hallyukstar","Kpopmap","Hungerplus","Thematternews"]

        if keyword == "": #if user doesn't enter anything
            self.no_text_in_ent_ht()

        elif keyword not in list_web and keyword != "": #if keyword is not in database
            self.conf_to_search()

        elif keyword in list_web and keyword != "":
            self.progress_bar.show()
            self.progress_bar.setValue(int(25)) 
            self.data_name = "test" + keyword
            self.update_data_web()
            self.progress_bar.setValue(int(100)) 



    def search_keyword(self):
        keyword = self.ent_ht.text()
        print('test keyword', keyword)

        if keyword == "": #if user doesn't enter anything
            self.no_text_in_ent_ht()

        else:
            print("okay")


        if keyword != "":
            print('yes')
            self.progress_bar.show()
            self.progress_bar.setValue(int(25)) 
            self.get_data_web()
            self.progress_bar.setValue(int(70)) 
            self.ref_checkframe()
        else:
            print('no')

    def show_update_data_table(self, data): #show update data on table
        self.progress_bar.setValue(int(70)) 
        head_col = list(data.head(0))
        len_file_col = len(head_col)
        len_file_row = len(data)

        self.data_box.clear()
        self.data_box.setRowCount(0)
        self.data_box.setColumnCount(len_file_col)
        self.data_box.setRowCount(len_file_row)
        for n, key in enumerate(data.keys()): # add item
            for m, item in enumerate(data[key]):
                if type(item) == float:
                    float_item = round(item,3)
                    newitem = QTableWidgetItem(str(float_item))
                else:
                    newitem = QTableWidgetItem(str(item))
                self.data_box.setItem(m, n, newitem)
        self.data_box.setHorizontalHeaderLabels(head_col)
        self.data_box.verticalHeader().hide()   
        self.data_box.show()

    

    def update_data_web(self):
        dataframe = []
        df = self.colWeb.update_get_data(self.data_name)
        dataframe.append(df)
        result = pd.concat(dataframe)
        self.show_update_data_table(result)



    def show_data_table(self, data):
        self.progress_bar.setValue(int(50)) 
        head_col = list(data.head(0))
        len_file_col = len(head_col)
        len_file_row = len(data)

        self.data_box.clear()
        self.data_box.setRowCount(0)
        self.data_box.setColumnCount(len_file_col)
        self.data_box.setRowCount(len_file_row)
        for n, key in enumerate(data.keys()): # add item
            for m, item in enumerate(data[key]):
                if type(item) == float:
                    float_item = round(item,3)
                    newitem = QTableWidgetItem(str(float_item))
                else:
                    newitem = QTableWidgetItem(str(item))
                self.data_box.setItem(m, n, newitem)
        self.data_box.setHorizontalHeaderLabels(head_col)
        self.data_box.verticalHeader().hide()   
        self.data_box.show()

    
    def get_data_web(self): #get data from scrap
        keyword = self.ent_ht.text().upper()
        dataframe = []
        df = self.colWeb.get_data(keyword)
        dataframe.append(df)
        result = pd.concat(dataframe)
        self.show_data_table(result.sort_values(by=['count'], ascending=False))
        self.show_sentiment_table(result)
        self.web_to_xlsx(keyword,result.sort_values(by=['count'], ascending=False))


    def web_to_xlsx(self,keyword,data_frame):
        if not os.path.exists(f"./data/"): 
            os.mkdir(f"./data/")
        if not os.path.exists(f"./data/search/"): 
            os.mkdir(f"./data/search/")
        set_today_str = date.today().strftime("%d%m%Y")
        data_frame.to_excel(f"./data/search/{keyword}_search_{set_today_str}.xlsx", engine="openpyxl", index=False)
    

    def show_sentiment_table(self,data): #sentiment table
        ne_count,pos_count,neg_count,per_ne,per_pos,per_neg = self.sentiment_cal_count(data)
        datasentiment_count = self.sentiment_count_frame(ne_count,pos_count,neg_count,per_ne,per_pos,per_neg)
        head_col = list(datasentiment_count.head(0))
        len_file_col = len(head_col)
        len_file_row = len(datasentiment_count)
        self.senti_box.clear()
        self.senti_box.setRowCount(0)
        self.senti_box.setColumnCount(len_file_col)
        self.senti_box.setRowCount(len_file_row)
        for n, key in enumerate(datasentiment_count.keys()): # add item
            for m, item in enumerate(datasentiment_count[key]):
                if type(item) == float:
                    float_item = round(item,3)
                    newitem = QTableWidgetItem(str(float_item))
                else:
                    newitem = QTableWidgetItem(str(item))
                self.senti_box.setItem(m, n, newitem)
        self.senti_box.setHorizontalHeaderLabels(head_col)
        self.senti_box.verticalHeader().hide()    
        self.senti_box.show()


    def sentiment_cal_count(self,data): #calculate sentiment

        sentiment_data = list(data['sentiment'])
        neutral_count = 0
        positive_count = 0
        negative_count = 0

        try:
            for sen in sentiment_data: #check polarity
                if sen == 'neutral':
                    neutral_count += 1
                elif sen == 'positive':
                    positive_count += 1
                elif sen == 'negative':
                    negative_count += 1
            all_percent = neutral_count+positive_count+negative_count
            percent_neutral = neutral_count/all_percent * 100
            percent_positive = positive_count/all_percent * 100
            percent_negative = negative_count/all_percent * 100
        except:
            percent_neutral = 0
            percent_positive = 0
            percent_negative = 0
        return neutral_count,positive_count,negative_count,percent_neutral,percent_positive,percent_negative

    def sentiment_count_frame(self,ne_count,pos_count,neg_count,per_ne,per_pos,per_neg):
        list_dataframe = [['neutral',ne_count,per_ne],['positive',pos_count,per_pos],['negative',neg_count,per_neg]]
        data_frame = pd.DataFrame(data=list_dataframe,columns=['sentiment','total','percent'])

        return data_frame 

    def ref_checkframe(self): #check reference link
        file = open('./data/webdata.json',"r")
        datafile = json.loads(file.read())
        file.close()
        list_countweb = {}
        for name in list(datafile['website'].keys()): 
            count_web = 0
            for check_web in list(datafile['website'].keys()):
                print(name,check_web)
                if name != check_web:
                    for ref_link in datafile['website'][name]:
                        if check_web in ref_link:
                            if check_web in list_countweb.keys():
                                list_countweb[check_web] = list_countweb[check_web] + 1    
                            else:
                                list_countweb[check_web] = 1
                else:
                    if check_web in list_countweb.keys():
                        pass
                    else:
                        list_countweb[check_web] = count_web
        name_data_countweb = list(list_countweb.keys()) 
        data_countweb = list(list_countweb.values())         
        data_frame = [[name_data_countweb[i],data_countweb[i]] for i in range(len(name_data_countweb))]
        countweb_frame = pd.DataFrame(data=data_frame,columns=['web','count web']).sort_values(by=['count web'], ascending=False)
        self.show_ref_table(countweb_frame)


    def show_ref_table(self, data): #show referenc table
        self.progress_bar.setValue(int(90)) 
        head_col = list(data.head(0))
        len_file_col = len(head_col)
        len_file_row = len(data)

        self.ref_box.clear()
        self.ref_box.setRowCount(0)
        self.ref_box.setColumnCount(len_file_col)
        self.ref_box.setRowCount(len_file_row)
        for n, key in enumerate(data.keys()): # add item
            for m, item in enumerate(data[key]):
                if type(item) == float:
                    float_item = round(item,3)
                    newitem = QTableWidgetItem(str(float_item))
                else:
                    newitem = QTableWidgetItem(str(item))
                self.ref_box.setItem(m, n, newitem)
        self.ref_box.setHorizontalHeaderLabels(head_col)
        self.ref_box.verticalHeader().hide()   
        self.ref_box.show()
        self.progress_bar.setValue(int(100)) 