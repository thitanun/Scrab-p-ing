from PyQt5 import QtCore, QtGui, QtWidgets
import collectWeb
from datetime import datetime,timedelta ,date
from PyQt5.QtWidgets import QTableWidgetItem
import pandas as pd


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
        self.search_bttn_ht.setGeometry(QtCore.QRect(90, 170, 75, 23))
        self.search_bttn_ht.setObjectName("search_bttn_ht")
        self.search_bttn_ht.clicked.connect(self.search_keyword)

        self.keyword_data = QtWidgets.QListWidget(main_webb)
        self.keyword_data.setGeometry(QtCore.QRect(30, 260, 191, 261))
        self.keyword_data.setObjectName("keyword_data")

        self.ht_label_2 = QtWidgets.QLabel(main_webb)
        self.ht_label_2.setGeometry(QtCore.QRect(30, 220, 191, 31))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.ht_label_2.setFont(font)
        self.ht_label_2.setObjectName("ht_label_2")

        self.start_date = QtWidgets.QDateEdit(main_webb)
        self.start_date.setGeometry(QtCore.QRect(30, 130, 81, 22))
        self.start_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QtCore.QDate.currentDate())
        self.start_date.setDisplayFormat("dd/MM/yyyy")
        self.start_date.setObjectName("start_date")


        self.stop_date = QtWidgets.QDateEdit(main_webb)
        self.stop_date.setGeometry(QtCore.QRect(140, 130, 81, 22))
        self.stop_date.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.stop_date.setCalendarPopup(True)
        self.stop_date.setDate(QtCore.QDate.currentDate())
        self.stop_date.setDisplayFormat("dd/MM/yyyy")
        self.stop_date.setObjectName("start_date")


        self.label = QtWidgets.QLabel(main_webb)
        self.label.setGeometry(QtCore.QRect(120, 120, 47, 41))
        self.label.setObjectName("label")

        # self.progress_bar = QtWidgets.QProgressBar(main_webb)
        # self.progress_bar.setGeometry(QtCore.QRect(30, 540, 191, 23))
        # self.progress_bar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        # self.progress_bar.setProperty("value", 24)
        # self.progress_bar.setObjectName("progress_bar")

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

        self.data_box = QtWidgets.QTableWidget(main_webb)
        self.data_box.setGeometry(QtCore.QRect(250, 10, 611, 561))
        self.data_box.setObjectName("data_box")
        self.data_box.setColumnCount(0)
        self.data_box.setRowCount(0)

        self.retranslateUi(main_webb)
        QtCore.QMetaObject.connectSlotsByName(main_webb)

        self.check_date()
        self.update_keyword_data()
        # self.search_keyword()

        self.colWeb = collectWeb.ClawWeb()

    def retranslateUi(self, main_webb):
        _translate = QtCore.QCoreApplication.translate
        main_webb.setWindowTitle(_translate("main_webb", "SCRAB(P)ing WEBSITE"))
        self.ht_label.setText(_translate("main_webb", "KEYWORD"))
        self.search_bttn_ht.setText(_translate("main_webb", "SEARCH"))
        self.ht_label_2.setText(_translate("main_webb", "DATABASE"))
        self.start_date.setDisplayFormat(_translate("main_webb", "dd/MM/yyyy"))
        self.stop_date.setDisplayFormat(_translate("main_webb", "dd/MM/yyyy"))
        self.label.setText(_translate("main_webb", "to"))
        self.today_lb.setText(_translate("main_webb", "TODAY"))
        self.current_date_lb.setText(_translate("main_webb","TODAY"))

    def update_keyword_data(self):
        self.keyword_data.addItem("Bright TV")
        self.keyword_data.addItem("Hello Kpop") 
        self.keyword_data.addItem("KBS")
        self.keyword_data.addItem("Koreaboo")
        self.keyword_data.addItem("Korism")
        self.keyword_data.addItem("Nineentertain")
        self.keyword_data.addItem("NME")
        self.keyword_data.addItem("Seoul2me")
        self.keyword_data.addItem("Sudsapda")
        self.keyword_data.addItem("Thaiger")
        self.keyword_data.addItem("Youzap")

    def check_date(self):
        today = datetime.utcnow().date()
        today_str = today.strftime("%d-%m-%Y")
        self.current_date_lb.setText(today_str)

    
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


    def search_keyword(self):
        keyword = self.ent_ht.text()
        print('test keyword', keyword)

        if keyword == "": #if user doesn't enter anything
            self.no_text_in_ent_ht()

        else:
            print("okay")


        if keyword != "":
            print('yes')
            self.get_data_web()
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

    
    def get_data_web(self):
        keyword = self.ent_ht.text().upper()
        dataframe = []
        # self.colWeb.get_data(keyword)
        # df = pd.read_excel(f"./data/tweets/{keyword}/{keyword}.xlsx", engine="openpyxl")
        df = self.colWeb.get_data(keyword)
        dataframe.append(df)
        result = pd.concat(dataframe)
        self.show_data_table(result)
        # return result 