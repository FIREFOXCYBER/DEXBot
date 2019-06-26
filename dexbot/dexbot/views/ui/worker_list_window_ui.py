# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jacko/Desktop/DEXBot/dexbot/dexbot/views/ui/worker_list_window.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 513)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("* {\n"
"    background-color: #152B2A;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContent = QtWidgets.QWidget()
        self.scrollAreaContent.setGeometry(QtCore.QRect(0, 0, 1023, 319))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaContent.sizePolicy().hasHeightForWidth())
        self.scrollAreaContent.setSizePolicy(sizePolicy)
        self.scrollAreaContent.setToolTipDuration(-7)
        self.scrollAreaContent.setStyleSheet("color: white;")
        self.scrollAreaContent.setObjectName("scrollAreaContent")
        self.scrollArea.setWidget(self.scrollAreaContent)
        self.gridLayout_2.addWidget(self.scrollArea, 3, 0, 1, 1)
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(0, 100))
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_wrap = QtWidgets.QWidget(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_wrap.sizePolicy().hasHeightForWidth())
        self.logo_wrap.setSizePolicy(sizePolicy)
        self.logo_wrap.setMinimumSize(QtCore.QSize(120, 50))
        self.logo_wrap.setMaximumSize(QtCore.QSize(120, 16777215))
        self.logo_wrap.setObjectName("logo_wrap")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.logo_wrap)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dexbot_logo = QtWidgets.QLabel(self.logo_wrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dexbot_logo.sizePolicy().hasHeightForWidth())
        self.dexbot_logo.setSizePolicy(sizePolicy)
        self.dexbot_logo.setMinimumSize(QtCore.QSize(0, 60))
        self.dexbot_logo.setMaximumSize(QtCore.QSize(100, 60))
        self.dexbot_logo.setText("")
        self.dexbot_logo.setPixmap(QtGui.QPixmap(":/general/img/dexbot.png"))
        self.dexbot_logo.setScaledContents(True)
        self.dexbot_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.dexbot_logo.setObjectName("dexbot_logo")
        self.verticalLayout_2.addWidget(self.dexbot_logo)
        self.horizontalLayout.addWidget(self.logo_wrap)
        self.actions_wrap = QtWidgets.QWidget(self.header)
        self.actions_wrap.setObjectName("actions_wrap")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.actions_wrap)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.actions_wrap)
        self.widget_5.setMaximumSize(QtCore.QSize(250, 80))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_worker_button_2 = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_worker_button_2.sizePolicy().hasHeightForWidth())
        self.add_worker_button_2.setSizePolicy(sizePolicy)
        self.add_worker_button_2.setMinimumSize(QtCore.QSize(100, 0))
        self.add_worker_button_2.setMaximumSize(QtCore.QSize(250, 25))
        self.add_worker_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_worker_button_2.setToolTipDuration(-1)
        self.add_worker_button_2.setStyleSheet("border: 0px; background-color: #3A6257; width: 250px; height: 20px; border-radius: 10px; color: #ffffff;")
        self.add_worker_button_2.setObjectName("add_worker_button_2")
        self.verticalLayout_3.addWidget(self.add_worker_button_2)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.add_worker_button = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_worker_button.sizePolicy().hasHeightForWidth())
        self.add_worker_button.setSizePolicy(sizePolicy)
        self.add_worker_button.setMinimumSize(QtCore.QSize(100, 0))
        self.add_worker_button.setMaximumSize(QtCore.QSize(250, 25))
        self.add_worker_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_worker_button.setToolTipDuration(-1)
        self.add_worker_button.setStyleSheet("border: 0px; background-color: #3A6257; width: 250px; height: 20px; border-radius: 10px; color: #ffffff;")
        self.add_worker_button.setObjectName("add_worker_button")
        self.verticalLayout_3.addWidget(self.add_worker_button)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.actions_wrap)
        self.settings_wrap = QtWidgets.QWidget(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_wrap.sizePolicy().hasHeightForWidth())
        self.settings_wrap.setSizePolicy(sizePolicy)
        self.settings_wrap.setMinimumSize(QtCore.QSize(120, 100))
        self.settings_wrap.setMaximumSize(QtCore.QSize(120, 100))
        self.settings_wrap.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.settings_wrap.setObjectName("settings_wrap")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settings_wrap)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings_button = QtWidgets.QPushButton(self.settings_wrap)
        self.settings_button.setMinimumSize(QtCore.QSize(80, 0))
        self.settings_button.setMaximumSize(QtCore.QSize(80, 25))
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_button.setStyleSheet("border: 0px; background-color: #3A6257; width: 250px; height: 30px; border-radius: 10px; color: #ffffff;")
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout.addWidget(self.settings_button)
        self.help_button = QtWidgets.QPushButton(self.settings_wrap)
        self.help_button.setMinimumSize(QtCore.QSize(80, 0))
        self.help_button.setMaximumSize(QtCore.QSize(80, 25))
        self.help_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help_button.setStyleSheet("border: 0px; background-color: #3A6257; width: 250px; height: 30px; border-radius: 10px; color: #ffffff;")
        self.help_button.setObjectName("help_button")
        self.verticalLayout.addWidget(self.help_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.settings_wrap)
        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.status_bar.setStyleSheet("color: #fff;")
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DEXBot"))
        self.add_worker_button_2.setText(_translate("MainWindow", "Visualisation"))
        self.add_worker_button.setText(_translate("MainWindow", "Add worker"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.help_button.setText(_translate("MainWindow", "Help"))

from dexbot.resources import icons_rc