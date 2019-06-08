# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Documents_DD\SCOLAIRE\INFORMATIQUE\Application_ASSOBI\ui\InterfaceV1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def Application_loop():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1850, 950)
        MainWindow.setMinimumSize(QtCore.QSize(1850, 950)) #Fixe la taille
        MainWindow.setMaximumSize(QtCore.QSize(1850, 950))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        
    ## BackGround
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(
"QWidget{\n"
"    background-image: url(BackGroundV1.png)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        
    ## ProgressBar
        self.progressBar_Sith = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_Sith.setGeometry(QtCore.QRect(100, 490, 825, 100))
        self.progressBar_Sith.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar_Sith.setAutoFillBackground(False)
        self.progressBar_Sith.setStyleSheet(
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ffffff, stop: 0.5 #ff3f3f, stop: 1 #ffffff);\n"
"    width: 2px;\n"
"}")
        self.progressBar_Sith.setProperty("value", 78)
        self.progressBar_Sith.setObjectName("progressBar_Sith")
        self.progressBar_Sith.setTextVisible(False)
        
        
        self.progressBar_Jedi = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_Jedi.setGeometry(QtCore.QRect(920, 490, 825, 100))
        self.progressBar_Jedi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_Jedi.setAutoFillBackground(False)
        self.progressBar_Jedi.setStyleSheet(
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 2px;\n"
"    background-color: black;"
"    background-image: url(PB_BG_Jedi.png)"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ffffff, stop: 0.5 #239fdd, stop: 1 #ffffff);\n"
"    width: 2px;\n"
"}")
        self.progressBar_Jedi.setProperty("value", 25)
        self.progressBar_Jedi.setObjectName("progressBar_Jedi")
        self.progressBar_Jedi.setTextVisible(False)
        
    ## Button
        self.JediButton = QtWidgets.QPushButton(self.centralwidget)
        self.JediButton.setGeometry(QtCore.QRect(1530, 770, 311, 131))
        self.JediButton.setStyleSheet("background-image: url(logo.png)")
        self.JediButton.setObjectName("JediButton")
        
        self.SithButton = QtWidgets.QPushButton(self.centralwidget)
        self.SithButton.setGeometry(QtCore.QRect(10, 770, 311, 131))
        self.SithButton.setStyleSheet("background-image: url(logo.png)")
        self.SithButton.setObjectName("SithButton")
        
    ## Scores
        self.ScoreSiths = QtWidgets.QLCDNumber(self.centralwidget)
        self.ScoreSiths.setGeometry(QtCore.QRect(100, 300, 351, 181))
        self.ScoreSiths.setAutoFillBackground(False)
        self.ScoreSiths.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.ScoreSiths.setSmallDecimalPoint(False)
        self.ScoreSiths.setDigitCount(5)
        self.ScoreSiths.setMode(QtWidgets.QLCDNumber.Dec)
        self.ScoreSiths.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ScoreSiths.setProperty("value", 0.85)
        self.ScoreSiths.setObjectName("ScoreSiths")
        
    ## Appli
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1850, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SithButton.setText(_translate("MainWindow", "+1 pour les Siths"))
        self.JediButton.setText(_translate("MainWindow", "+1 pour les Jedis"))


if __name__ == "__main__":
    Application_loop()

