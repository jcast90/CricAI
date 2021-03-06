# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CricAI_Basic.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonRunMLP = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRunMLP.setGeometry(QtCore.QRect(330, 430, 151, 41))
        self.buttonRunMLP.setObjectName("buttonRunMLP")
        self.dbInnings = QtWidgets.QGroupBox(self.centralwidget)
        self.dbInnings.setGeometry(QtCore.QRect(250, 230, 311, 80))
        self.dbInnings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dbInnings.setTitle("")
        self.dbInnings.setObjectName("dbInnings")
        self.labelInnings = QtWidgets.QLabel(self.dbInnings)
        self.labelInnings.setGeometry(QtCore.QRect(90, 10, 121, 20))
        self.labelInnings.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInnings.setObjectName("labelInnings")
        self.rbTeam1_Innings = QtWidgets.QRadioButton(self.dbInnings)
        self.rbTeam1_Innings.setGeometry(QtCore.QRect(30, 40, 101, 21))
        self.rbTeam1_Innings.setObjectName("rbTeam1_Innings")
        self.rbTeam2_Innings = QtWidgets.QRadioButton(self.dbInnings)
        self.rbTeam2_Innings.setGeometry(QtCore.QRect(200, 40, 91, 21))
        self.rbTeam2_Innings.setObjectName("rbTeam2_Innings")
        self.dbVenue = QtWidgets.QGroupBox(self.centralwidget)
        self.dbVenue.setGeometry(QtCore.QRect(180, 320, 431, 80))
        self.dbVenue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dbVenue.setTitle("")
        self.dbVenue.setAlignment(QtCore.Qt.AlignCenter)
        self.dbVenue.setObjectName("dbVenue")
        self.labelVenue = QtWidgets.QLabel(self.dbVenue)
        self.labelVenue.setGeometry(QtCore.QRect(160, 10, 111, 20))
        self.labelVenue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVenue.setObjectName("labelVenue")
        self.rbTeam1_Home = QtWidgets.QRadioButton(self.dbVenue)
        self.rbTeam1_Home.setGeometry(QtCore.QRect(20, 40, 92, 21))
        self.rbTeam1_Home.setObjectName("rbTeam1_Home")
        self.rbTeam2_Home = QtWidgets.QRadioButton(self.dbVenue)
        self.rbTeam2_Home.setGeometry(QtCore.QRect(170, 40, 111, 21))
        self.rbTeam2_Home.setObjectName("rbTeam2_Home")
        self.rb_Neutral = QtWidgets.QRadioButton(self.dbVenue)
        self.rb_Neutral.setGeometry(QtCore.QRect(330, 40, 92, 21))
        self.rb_Neutral.setObjectName("rb_Neutral")
        self.buttonRunDT = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRunDT.setGeometry(QtCore.QRect(330, 490, 151, 41))
        self.buttonRunDT.setObjectName("buttonRunDT")
        self.labelFlagT1 = QtWidgets.QLabel(self.centralwidget)
        self.labelFlagT1.setGeometry(QtCore.QRect(140, 40, 151, 101))
        self.labelFlagT1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelFlagT1.setObjectName("labelFlagT1")
        self.labelFlagT2 = QtWidgets.QLabel(self.centralwidget)
        self.labelFlagT2.setGeometry(QtCore.QRect(500, 40, 151, 101))
        self.labelFlagT2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelFlagT2.setObjectName("labelFlagT2")
        self.labelVersus = QtWidgets.QLabel(self.centralwidget)
        self.labelVersus.setGeometry(QtCore.QRect(370, 60, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.labelVersus.setFont(font)
        self.labelVersus.setObjectName("labelVersus")
        self.comboBoxTeam1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTeam1.setGeometry(QtCore.QRect(10, 70, 101, 24))
        self.comboBoxTeam1.setObjectName("comboBoxTeam1")
        self.comboBoxTeam2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTeam2.setGeometry(QtCore.QRect(680, 70, 101, 24))
        self.comboBoxTeam2.setObjectName("comboBoxTeam2")
        self.comboBoxGround = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxGround.setGeometry(QtCore.QRect(360, 180, 181, 24))
        self.comboBoxGround.setObjectName("comboBoxGround")
        self.labelGround = QtWidgets.QLabel(self.centralwidget)
        self.labelGround.setGeometry(QtCore.QRect(270, 180, 49, 20))
        self.labelGround.setObjectName("labelGround")
        self.frameWarning = QtWidgets.QFrame(self.centralwidget)
        self.frameWarning.setGeometry(QtCore.QRect(190, 30, 411, 151))
        self.frameWarning.setAutoFillBackground(True)
        self.frameWarning.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWarning.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWarning.setObjectName("frameWarning")
        self.labelMessage = QtWidgets.QLabel(self.frameWarning)
        self.labelMessage.setGeometry(QtCore.QRect(130, 80, 161, 20))
        self.labelMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMessage.setObjectName("labelMessage")
        self.labelLogo = QtWidgets.QLabel(self.frameWarning)
        self.labelLogo.setGeometry(QtCore.QRect(180, 10, 61, 61))
        self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.pushButtonOK = QtWidgets.QPushButton(self.frameWarning)
        self.pushButtonOK.setGeometry(QtCore.QRect(164, 110, 91, 27))
        self.pushButtonOK.setObjectName("pushButtonOK")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CricAI_Basic"))
        self.buttonRunMLP.setText(_translate("MainWindow", "RUN : MLPClassifier"))
        self.labelInnings.setText(_translate("MainWindow", "First Innings"))
        self.rbTeam1_Innings.setText(_translate("MainWindow", "India"))
        self.rbTeam2_Innings.setText(_translate("MainWindow", "Australia"))
        self.labelVenue.setText(_translate("MainWindow", "Venue"))
        self.rbTeam1_Home.setText(_translate("MainWindow", "India"))
        self.rbTeam2_Home.setText(_translate("MainWindow", "Australia"))
        self.rb_Neutral.setText(_translate("MainWindow", "Neutral"))
        self.buttonRunDT.setText(_translate("MainWindow", "RUN : DTClassifier"))
        self.labelFlagT1.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/flags/images/flags/India.jpg\"/></p></body></html>"))
        self.labelFlagT2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/flags/images/flags/Australia.jpg\"/></p></body></html>"))
        self.labelVersus.setText(_translate("MainWindow", "V/S"))
        self.labelGround.setText(_translate("MainWindow", "Ground"))
        self.labelMessage.setText(_translate("MainWindow", "Kindly Select Different Teams"))
        self.labelLogo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/projectImages/images/warning.jpg\"/></p></body></html>"))
        self.pushButtonOK.setText(_translate("MainWindow", "OK"))

import CricAI_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

