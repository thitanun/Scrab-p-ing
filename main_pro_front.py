from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_twitter import Ui_main_twit
from main_web import Ui_main_web


class Ui_pro_front(object):
    def setupUi(self, pro_front):
        pro_front.setObjectName("pro_front")
        pro_front.resize(660, 575)

        self.wb_bttn = QtWidgets.QPushButton(pro_front)
        self.wb_bttn.setGeometry(QtCore.QRect(160, 200, 341, 81))
        self.wb_bttn.setObjectName("wb_bttn")
        self.wb_bttn.clicked.connect(self.con_web)

        self.tw_bttn = QtWidgets.QPushButton(pro_front)
        self.tw_bttn.setGeometry(QtCore.QRect(160, 330, 341, 81))
        self.tw_bttn.setObjectName("tw_bttn")
        self.tw_bttn.clicked.connect(self.con_twitter)

        self.retranslateUi(pro_front)
        QtCore.QMetaObject.connectSlotsByName(pro_front)

        self.TwitterPage = QtWidgets.QMainWindow()
        self.ui = Ui_main_twit()
        self.ui.setupUi(self.TwitterPage)

        self.WebsitePage = QtWidgets.QMainWindow()
        self.ui2 = Ui_main_web()
        self.ui2.setupUi(self.WebsitePage)

    def retranslateUi(self, pro_front):
        _translate = QtCore.QCoreApplication.translate
        pro_front.setWindowTitle(_translate("pro_front", "SCRAB(P)ing"))
        self.wb_bttn.setText(_translate("pro_front", "WEB"))
        self.tw_bttn.setText(_translate("pro_front", "TWITTER"))

    def con_twitter(self):
        self.TwitterPage.show()
        # sys.withdraw()
        # open_tw.exec()

    def con_web(self):
        self.WebsitePage.show()


app = QtWidgets.QApplication(sys.argv)
pro_front = QtWidgets.QWidget()
ui = Ui_pro_front()
ui.setupUi(pro_front)
pro_front.show()
sys.exit(app.exec_())
