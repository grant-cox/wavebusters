# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TouchInput = QtWidgets.QPushButton(self.centralwidget)
        self.TouchInput.setGeometry(QtCore.QRect(170, 310, 161, 161))
        self.TouchInput.setObjectName("TouchInput")
        self.WelcomeText = QtWidgets.QLabel(self.centralwidget)
        self.WelcomeText.setGeometry(QtCore.QRect(360, 190, 251, 21))
        self.WelcomeText.setTextFormat(QtCore.Qt.LogText)
        self.WelcomeText.setScaledContents(False)
        self.WelcomeText.setObjectName("WelcomeText")
        self.KeyboardInput = QtWidgets.QPushButton(self.centralwidget)
        self.KeyboardInput.setGeometry(QtCore.QRect(640, 310, 161, 161))
        self.KeyboardInput.setObjectName("KeyboardInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A.R.E.S"))
        self.TouchInput.setText(_translate("MainWindow", "Touch Input"))
        self.WelcomeText.setText(_translate("MainWindow", "Welcome! Please choose a GUI Layout"))
        self.KeyboardInput.setText(_translate("MainWindow", "Keyboard Input"))

