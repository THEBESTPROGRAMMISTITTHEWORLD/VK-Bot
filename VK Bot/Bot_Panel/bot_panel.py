# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bot_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Window = QtWidgets.QFrame(self.centralwidget)
        self.Window.setGeometry(QtCore.QRect(10, 10, 411, 321))
        self.Window.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}")
        self.Window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Window.setObjectName("Window")
        self.WindowFrame = QtWidgets.QFrame(self.Window)
        self.WindowFrame.setGeometry(QtCore.QRect(0, 0, 411, 31))
        self.WindowFrame.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.WindowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WindowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WindowFrame.setObjectName("WindowFrame")
        self.CloseWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.CloseWindowButton.setGeometry(QtCore.QRect(370, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CloseWindowButton.setFont(font)
        self.CloseWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.CloseWindowButton.setObjectName("CloseWindowButton")
        self.MinimizeWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.MinimizeWindowButton.setGeometry(QtCore.QRect(329, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MinimizeWindowButton.setFont(font)
        self.MinimizeWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MinimizeWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.MinimizeWindowButton.setDefault(False)
        self.MinimizeWindowButton.setObjectName("MinimizeWindowButton")
        self.StartBotButton = QtWidgets.QPushButton(self.Window)
        self.StartBotButton.setGeometry(QtCore.QRect(210, 260, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.StartBotButton.setFont(font)
        self.StartBotButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartBotButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8px;\n"
"    background-color: #02d609;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #02c709;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #04b309;\n"
"}")
        self.StartBotButton.setObjectName("StartBotButton")
        self.BotSettingsButton = QtWidgets.QPushButton(self.Window)
        self.BotSettingsButton.setGeometry(QtCore.QRect(20, 260, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BotSettingsButton.setFont(font)
        self.BotSettingsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotSettingsButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.BotSettingsButton.setObjectName("BotSettingsButton")
        self.LogListWidget = QtWidgets.QListWidget(self.Window)
        self.LogListWidget.setGeometry(QtCore.QRect(20, 50, 371, 151))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.LogListWidget.setFont(font)
        self.LogListWidget.setTabletTracking(False)
        self.LogListWidget.setAutoFillBackground(False)
        self.LogListWidget.setStyleSheet("color: white;\n"
"border-radius: 7px;\n"
"background-color: #2C313C;\n"
"")
        self.LogListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LogListWidget.setLineWidth(1)
        self.LogListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.LogListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.LogListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.LogListWidget.setAutoScroll(True)
        self.LogListWidget.setTabKeyNavigation(False)
        self.LogListWidget.setProperty("showDropIndicator", True)
        self.LogListWidget.setDragDropOverwriteMode(False)
        self.LogListWidget.setAlternatingRowColors(False)
        self.LogListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.LogListWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.LogListWidget.setMovement(QtWidgets.QListView.Static)
        self.LogListWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.LogListWidget.setProperty("isWrapping", False)
        self.LogListWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.LogListWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.LogListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.LogListWidget.setUniformItemSizes(False)
        self.LogListWidget.setWordWrap(False)
        self.LogListWidget.setSelectionRectVisible(False)
        self.LogListWidget.setObjectName("LogListWidget")
        self.SaveLogButton = QtWidgets.QPushButton(self.Window)
        self.SaveLogButton.setGeometry(QtCore.QRect(20, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SaveLogButton.setFont(font)
        self.SaveLogButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveLogButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.SaveLogButton.setObjectName("SaveLogButton")
        self.ClearLogButton = QtWidgets.QPushButton(self.Window)
        self.ClearLogButton.setGeometry(QtCore.QRect(210, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ClearLogButton.setFont(font)
        self.ClearLogButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ClearLogButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.ClearLogButton.setObjectName("ClearLogButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CloseWindowButton.setText(_translate("MainWindow", "X"))
        self.MinimizeWindowButton.setText(_translate("MainWindow", "_"))
        self.StartBotButton.setText(_translate("MainWindow", "Запустить бота"))
        self.BotSettingsButton.setText(_translate("MainWindow", "Настройки"))
        self.LogListWidget.setSortingEnabled(False)
        self.SaveLogButton.setText(_translate("MainWindow", "Сохранить логи"))
        self.ClearLogButton.setText(_translate("MainWindow", "Очистить логи"))
