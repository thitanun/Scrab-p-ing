# from multiprocessing.connection import answer_challenge
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import os
import collectTwitter
import pandas as pd
from datetime import datetime,timedelta ,date


class Ui_main_twit(object):
    def setupUi(self, main_twit):

        main_twit.setObjectName("main_twit")
        main_twit.resize(890, 593)

        self.ht_label = QtWidgets.QLabel(main_twit)
        self.ht_label.setGeometry(QtCore.QRect(30, 20, 101, 31))
        
        font = QtGui.QFont()
        font.setFamily("Poplar Std")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.ht_label.setFont(font)
        self.ht_label.setObjectName("ht_label")

        self.ent_ht = QtWidgets.QLineEdit(main_twit)
        self.ent_ht.setGeometry(QtCore.QRect(30, 50, 191, 31))
        self.ent_ht.setObjectName("ent_ht")

        self.table_box = QtWidgets.QTableWidget(main_twit)
        self.table_box.setGeometry(QtCore.QRect(250, 20, 601, 551))
        self.table_box.setObjectName("table_box")
        self.table_box.setColumnCount(0)
        self.table_box.setRowCount(0)

        self.search_bttn_ht = QtWidgets.QPushButton(main_twit)
        self.search_bttn_ht.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.search_bttn_ht.setObjectName("search_bttn_ht")
        self.search_bttn_ht.clicked.connect(self.search_keyword)

        self.keyword_data = QtWidgets.QListWidget(main_twit)
        self.keyword_data.setGeometry(QtCore.QRect(30, 220, 191, 281))
        self.keyword_data.setObjectName("keyword_data")
        self.keyword_data.itemDoubleClicked.connect(self.show_data_in_database)

        self.ht_label_2 = QtWidgets.QLabel(main_twit)
        self.ht_label_2.setGeometry(QtCore.QRect(30, 180, 181, 31))
        
        font = QtGui.QFont()
        font.setFamily("Poplar Std")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.ht_label_2.setFont(font)
        self.ht_label_2.setObjectName("ht_label_2")

        self.start_date = QtWidgets.QDateEdit(main_twit)
        self.start_date.setGeometry(QtCore.QRect(30, 90, 81, 22))
        self.start_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 4, 1), QtCore.QTime(0, 0, 0)))
        self.start_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 30), QtCore.QTime(0, 0, 0)))
        self.start_date.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QtCore.QDate(2022, 4, 1))
        self.start_date.setObjectName("start_date")

        self.stop_date = QtWidgets.QDateEdit(main_twit)
        self.stop_date.setGeometry(QtCore.QRect(140, 90, 81, 22))
        self.stop_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.stop_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 4, 1), QtCore.QTime(0, 0, 0)))
        self.stop_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 30), QtCore.QTime(0, 0, 0)))
        self.stop_date.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.stop_date.setCalendarPopup(True)
        self.stop_date.setDate(QtCore.QDate(2022, 4, 1))
        self.stop_date.setObjectName("stop_date")

        self.label = QtWidgets.QLabel(main_twit)
        self.label.setGeometry(QtCore.QRect(120, 80, 47, 41))
        self.label.setObjectName("label")

        self.retranslateUi(main_twit)
        QtCore.QMetaObject.connectSlotsByName(main_twit)

        self.check_keyword()
        self.update_keyword()

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


    def no_text_in_ent_ht(self):
        # warn_ent = QMessageBox.warning(self, "Box is empty", 
        #                                              "Please enter text before you search",
        #                                              defaultButton = QMessageBox.Ok)
        warn_ent = QtWidgets.QMessageBox()
        warn_ent.setIcon(QtWidgets.QMessageBox.Warning)
        warn_ent.setWindowTitle("Box is empty!")
        warn_ent.setText("Please enter text before you search")
        warn_ent.setStandardButtons(QtWidgets.QMessageBox.Ok ) #| QtWidgets.QMessageBox.Cancel)
        warn_ent.buttonClicked.connect(lambda:warn_ent.close())

        a = warn_ent.exec_() 


    def check_keyword(self):
        self.al_search = os.listdir("./data/tweets")
        print('test update', self.al_search)


    def update_keyword(self):
        self.keyword_data.clear()
        for i in self.al_search:
            self.keyword_data.addItem(i)
        print('update success')


    def conf_to_search(self):
        sure_ent = QtWidgets.QMessageBox()
        sure_ent.setIcon(QtWidgets.QMessageBox.Critical)
        sure_ent.setWindowTitle("New Keyword")
        sure_ent.setText("This keyword is not in database\n Do you want to continue?")
        # sure_ent.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        sure_ent.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        # sure_ent.buttonClicked.connect(lambda:sure_ent.close())
        sure_ent.buttonClicked.connect(self.answer_bttn)

        a = sure_ent.exec_() 


    def answer_bttn(self, conf):
        if conf.text() == "OK":
            print('said yes')
            self.answer_confirm = True
        else:
            print('said no')
            self.answer_confirm = False


    def search_keyword(self):
        keyword = self.ent_ht.text()
        print('test keyword', keyword)

        if keyword == "": #if user doesn't enter anything
            self.no_text_in_ent_ht()

        elif keyword not in self.al_search and keyword != "": #if keyword is not in database
            print("not in")
            self.conf_to_search()

        else:
            print("okay")

        if self.answer_confirm:
            print('start')
            # collectTwitter.ClawTwitter.get_datatweet(keyword)
            self.colTwitter.get_datatweet(keyword)
            self.check_keyword()
            self.update_keyword()
            self.get_data_twitter()
        elif keyword in self.al_search and keyword != "":
            print('in database')
            self.get_data_twitter()
        else:
            print('no')


    def show_data_table(self, data):
        # print('show data here')
        head_col = list(data.head(0))
        # print('check head', head_col)
        len_file_col = len(head_col)
        # print('len col', len_file_col)
        len_file_row = len(data)
        # print('len row', len_file_row)

        self.table_box.clear()
        self.table_box.setRowCount(0)
        self.table_box.setColumnCount(len_file_col)
        self.table_box.setRowCount(len_file_row)
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


    def get_data_twitter(self):
        keyword = self.ent_ht.text()
        today = datetime.utcnow().date()
        today_str = today.strftime("%d%m%Y")
        all_file = os.listdir(f"./data/tweets/{keyword}")
        # print('test all file', all_file)
        dataframe = []
        if f"{keyword}_{today_str}.xlsx" in all_file:
            df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}_{today_str}.xlsx", engine="openpyxl")
            dataframe.append(df)
        tweets = pd.concat(dataframe, ignore_index=True)
        # print('test df', tweets)
        self.show_data_table(tweets)


    def show_data_in_database(self):
        self.ent_ht.setText(self.keyword_data.selectedItems()[0].text())
        self.get_data_twitter()
