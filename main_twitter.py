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
        # self.keyword_data.itemDoubleClicked.connect(self.show_data_in_database)
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
        # self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 4, 16), QtCore.QTime(0, 0, 0)))
        # self.start_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 30), QtCore.QTime(0, 0, 0)))
        # self.start_date.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.start_date.setCalendarPopup(True)
        # self.start_date.setDate(date.today())
        self.start_date.setDate(QtCore.QDate.currentDate())
        # self.start_date.setDate(QtCore.QDate(2020, 12, 30))
        self.start_date.setDisplayFormat("dd/MM/yyyy")
        self.start_date.setObjectName("start_date")


        self.stop_date = QtWidgets.QDateEdit(main_twit)
        self.stop_date.setGeometry(QtCore.QRect(140, 130, 81, 22))
        self.stop_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        # self.stop_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 4, 16), QtCore.QTime(0, 0, 0)))
        # self.stop_date.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 30), QtCore.QTime(0, 0, 0)))
        # self.stop_date.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.stop_date.setCalendarPopup(True)
        # self.stop_date.setDate(date.today())
        self.stop_date.setDate(QtCore.QDate.currentDate())
        # self.stop_date.setDate(QtCore.QDate(2020, 12, 30))
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
        # self.table_box = QtWidgets.QTableWidget(main_twit)
        self.table_box = QtWidgets.QTableWidget(self.tab)
        # self.table_box.setGeometry(QtCore.QRect(250, 20, 611, 531))
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

        # self.current_date_lb.setText("")
        self.current_date_lb.setFont(font)
        self.current_date_lb.setObjectName("current_date_lb")

        self.retranslateUi(main_twit)
        # self.tabWidget.setCurrentIndex(1)
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
        self.today_lb.setText(_translate("main_twit", "TODAY"))
        # self.current_date_lb.setText(_translate("main_twit", f"{self.today_str}"))
        self.current_date_lb.setText(_translate("main_twit","TODAY"))



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


    def check_date(self):
        today = datetime.utcnow().date()
        today_str = today.strftime("%d-%m-%Y")
        self.current_date_lb.setText(today_str)


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

    
    def conf_to_search_date(self, date_start, date_stop):
        sure_date_ent = QtWidgets.QMessageBox()
        sure_date_ent.setIcon(QtWidgets.QMessageBox.Critical)
        sure_date_ent.setWindowTitle("New Date")
        sure_date_ent.setText(f"This keyword have no data between {date_start} - {date_stop}\n Do you want to continue?")
        sure_date_ent.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        sure_date_ent.buttonClicked.connect(self.answer_bttn)

        a = sure_date_ent.exec_() 



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
        date_start = self.start_date.date().toPyDate()
        date_stop = self.stop_date.date().toPyDate()

        if keyword == "": #if user doesn't enter anything
            self.no_text_in_ent_ht()

        elif keyword not in self.al_search and keyword != "": #if keyword is not in database
            print("not in")
            self.conf_to_search()

        elif date_start.strftime('%d%m%Y') not in self.colTwitter.metadata['keyword'][keyword]['date']: #if keyword have no data at that date
            print("date not in")
            print('start', date_start)
            print('stop', date_stop)
            self.conf_to_search_date(date_start, date_stop)
            # print('test ans', self.answer_confirm)

        elif date_stop.strftime('%d%m%Y') not in self.colTwitter.metadata['keyword'][keyword]['date']: #if keyword have no data at that date
            print("date not in")
            self.conf_to_search_date(date_start, date_stop)

        else:
            print("okay")

        if self.answer_confirm:
            print('start')
            # collectTwitter.ClawTwitter.get_datatweet(keyword)
            self.progress_bar.show()
            # self.progress_bar.setValue(int(0)) 
            # self.colTwitter.get_datatweet(keyword)
            self.progress_bar.setValue(int(25)) 
            self.check_keyword()
            self.update_keyword()
            self.get_data_twitter()
        elif keyword in self.al_search and keyword != "" and date_start.strftime('%d%m%Y') in self.colTwitter.metadata['keyword'][keyword]['date'] and date_stop.strftime('%d%m%Y') in self.colTwitter.metadata['keyword'][keyword]['date']:
            print('in database')
            self.progress_bar.show()
            # self.progress_bar.setValue(int(0))
            self.progress_bar.setValue(int(25)) 
            self.get_data_twitter()
        else:
            print('no')
    
    def show_data_in_database(self):
        self.ent_ht.setText(self.keyword_data.selectedItems()[0].text())
        # self.get_data_twitter()


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
        self.progress_bar.setValue(int(70)) 
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
        # self.progress_bar.setValue(int(100))    
        self.table_box.show()
        # self.progress_bar.hide()


    def formdate(self,date_start,date_stop):
        # form_date = "%Y-%m-%d"
        # format_star = datetime.strptime(date_start,form_date)
        # format_stop = datetime.strptime(date_stop,form_date)
        diff_deltadays = date_stop - date_start 
        # diff_deltadays = format_stop - format_star #timedelta
        diff_days = diff_deltadays.days #int
        return diff_days
        # return format_star,format_stop,diff_days
    
    # def get_data_twitter(self):
    #     keyword = self.ent_ht.text().upper()
    #     date_start = self.start_date.date().toPyDate()
    #     date_stop = self.stop_date.date().toPyDate()
    #     # format_star,format_stop,diff_days = self.formdate(date_start,date_stop)
    #     diff_days = self.formdate(date_start,date_stop)
    #     dataframe = []
    #     for i in range(diff_days+1):
    #         # date_add = format_star + timedelta(days = int(i))
    #         date_add = date_start + timedelta(days = int(i))
    #         date_addstr = date_add.strftime("%Y-%m-%d")
    #         date_filestr = date_add.strftime("%d%m%Y")
    #         try:
    #             df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}_{date_filestr}.xlsx", engine="openpyxl")
    #         except:
    #             self.colTwitter.get_datatweet(keyword,date_add)
    #             self.check_keyword()
    #             self.update_keyword()
    #             df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}_{date_filestr}.xlsx", engine="openpyxl")
    #         dataframe.append(df)
    #     result = pd.concat(dataframe)
    #     self.show_data_table(result)
    #     # return result 

    def get_data_twitter(self):
        keyword = self.ent_ht.text().upper()
        date_start = self.start_date.date().toPyDate()
        date_stop = self.stop_date.date().toPyDate()
        # format_star,format_stop,diff_days = self.formdate(date_start,date_stop)
        diff_days = self.formdate(date_start,date_stop)
        dataframe = []
        for i in range(diff_days+1):
            # date_add = format_star + timedelta(days = int(i))
            date_add = date_start + timedelta(days = int(i))
            date_addstr = date_add.strftime("%Y-%m-%d")
            date_filestr = date_add.strftime("%d%m%Y")
            try:
                df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}_{date_filestr}.xlsx", engine="openpyxl")
            except:
                self.progress_bar.setValue(int(25)) 
                self.colTwitter.get_datatweet(keyword,date_add)
                self.progress_bar.setValue(int(50)) 
                self.check_keyword()
                self.update_keyword()
                df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}_{date_filestr}.xlsx", engine="openpyxl")
            self.progress_bar.setValue(int(50)) 
            dataframe.append(df)
        result = pd.concat(dataframe)
        self.show_data_table(result)
        count_frame = self.colTwitter.showcount_twitter(result)
        # print(count_frame)
        self.show_count_table(count_frame)
        # return result 


    def show_count_table(self, data):
        self.progress_bar.setValue(int(90))  
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
        self.progress_bar.hide()