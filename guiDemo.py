# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiDemo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 1065)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label01 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label01.setFont(font)
        self.label01.setAlignment(QtCore.Qt.AlignCenter)
        self.label01.setObjectName("label01")
        self.horizontalLayout.addWidget(self.label01)
        self.slideSwitch01 = SlideSwitch(self.centralwidget)
        self.slideSwitch01.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch01.sizePolicy().hasHeightForWidth())
        self.slideSwitch01.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch01.setFont(font)
        self.slideSwitch01.setObjectName("slideSwitch01")
        self.horizontalLayout.addWidget(self.slideSwitch01)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label02 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label02.setFont(font)
        self.label02.setAlignment(QtCore.Qt.AlignCenter)
        self.label02.setObjectName("label02")
        self.horizontalLayout_2.addWidget(self.label02)
        self.slideSwitch02 = SlideSwitch(self.centralwidget)
        self.slideSwitch02.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch02.sizePolicy().hasHeightForWidth())
        self.slideSwitch02.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch02.setFont(font)
        self.slideSwitch02.setObjectName("slideSwitch02")
        self.horizontalLayout_2.addWidget(self.slideSwitch02)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label03 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label03.setFont(font)
        self.label03.setAlignment(QtCore.Qt.AlignCenter)
        self.label03.setObjectName("label03")
        self.horizontalLayout_3.addWidget(self.label03)
        self.slideSwitch03 = SlideSwitch(self.centralwidget)
        self.slideSwitch03.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch03.sizePolicy().hasHeightForWidth())
        self.slideSwitch03.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch03.setFont(font)
        self.slideSwitch03.setObjectName("slideSwitch03")
        self.horizontalLayout_3.addWidget(self.slideSwitch03)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label04 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label04.setFont(font)
        self.label04.setAlignment(QtCore.Qt.AlignCenter)
        self.label04.setObjectName("label04")
        self.horizontalLayout_4.addWidget(self.label04)
        self.slideSwitch04 = SlideSwitch(self.centralwidget)
        self.slideSwitch04.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch04.sizePolicy().hasHeightForWidth())
        self.slideSwitch04.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch04.setFont(font)
        self.slideSwitch04.setObjectName("slideSwitch04")
        self.horizontalLayout_4.addWidget(self.slideSwitch04)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.slideSwitch05 = SlideSwitch(self.centralwidget)
        self.slideSwitch05.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch05.sizePolicy().hasHeightForWidth())
        self.slideSwitch05.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch05.setFont(font)
        self.slideSwitch05.setObjectName("slideSwitch05")
        self.horizontalLayout_5.addWidget(self.slideSwitch05)
        self.slideSwitch06 = SlideSwitch(self.centralwidget)
        self.slideSwitch06.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch06.sizePolicy().hasHeightForWidth())
        self.slideSwitch06.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch06.setFont(font)
        self.slideSwitch06.setObjectName("slideSwitch06")
        self.horizontalLayout_5.addWidget(self.slideSwitch06)
        self.slideSwitch07 = SlideSwitch(self.centralwidget)
        self.slideSwitch07.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch07.sizePolicy().hasHeightForWidth())
        self.slideSwitch07.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch07.setFont(font)
        self.slideSwitch07.setObjectName("slideSwitch07")
        self.horizontalLayout_5.addWidget(self.slideSwitch07)
        self.slideSwitch08 = SlideSwitch(self.centralwidget)
        self.slideSwitch08.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slideSwitch08.sizePolicy().hasHeightForWidth())
        self.slideSwitch08.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(6)
        self.slideSwitch08.setFont(font)
        self.slideSwitch08.setObjectName("slideSwitch08")
        self.horizontalLayout_5.addWidget(self.slideSwitch08)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnShuffle = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShuffle.sizePolicy().hasHeightForWidth())
        self.btnShuffle.setSizePolicy(sizePolicy)
        self.btnShuffle.setObjectName("btnShuffle")
        self.gridLayout_3.addWidget(self.btnShuffle, 0, 3, 1, 1)
        self.btnDefault = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDefault.sizePolicy().hasHeightForWidth())
        self.btnDefault.setSizePolicy(sizePolicy)
        self.btnDefault.setObjectName("btnDefault")
        self.gridLayout_3.addWidget(self.btnDefault, 0, 1, 1, 1)
        self.btnAllOff = QtWidgets.QPushButton(self.centralwidget)
        self.btnAllOff.setObjectName("btnAllOff")
        self.gridLayout_3.addWidget(self.btnAllOff, 1, 1, 1, 1)
        self.btnAllOn = QtWidgets.QPushButton(self.centralwidget)
        self.btnAllOn.setObjectName("btnAllOn")
        self.gridLayout_3.addWidget(self.btnAllOn, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1293, 31))
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
        self.label01.setText(_translate("MainWindow", "Slide Switch 1"))
        self.label02.setText(_translate("MainWindow", "Slide Switch 2"))
        self.label03.setText(_translate("MainWindow", "Slide Switch 3"))
        self.label04.setText(_translate("MainWindow", "Slide Switch 4"))
        self.btnShuffle.setText(_translate("MainWindow", "Shuffle Colours"))
        self.btnDefault.setText(_translate("MainWindow", "Default Colours"))
        self.btnAllOff.setText(_translate("MainWindow", "All Off"))
        self.btnAllOn.setText(_translate("MainWindow", "All On"))

from slideSwitch import SlideSwitch

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

