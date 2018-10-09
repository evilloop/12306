# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui/entry.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EntryUi(object):
    def setupUi(self, EntryUi):
        EntryUi.setObjectName("EntryUi")
        EntryUi.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(EntryUi)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 587, 442))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.oper_sizer = QtWidgets.QHBoxLayout()
        self.oper_sizer.setObjectName("oper_sizer")
        self.query_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.query_btn.setObjectName("query_btn")
        self.oper_sizer.addWidget(self.query_btn)
        self.info_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.info_lbl.setObjectName("info_lbl")
        self.oper_sizer.addWidget(self.info_lbl)
        self.open_config_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.open_config_btn.setObjectName("open_config_btn")
        self.oper_sizer.addWidget(self.open_config_btn)
        self.verticalLayout_2.addLayout(self.oper_sizer)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tickit_list = QtWidgets.QListWidget(self.layoutWidget)
        self.tickit_list.setObjectName("tickit_list")
        self.verticalLayout.addWidget(self.tickit_list)
        self.contact_list = QtWidgets.QListWidget(self.layoutWidget)
        self.contact_list.setObjectName("contact_list")
        self.verticalLayout.addWidget(self.contact_list)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.log_list = QtWidgets.QListView(self.layoutWidget)
        self.log_list.setObjectName("log_list")
        self.horizontalLayout.addWidget(self.log_list)
        EntryUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EntryUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        EntryUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EntryUi)
        self.statusbar.setObjectName("statusbar")
        EntryUi.setStatusBar(self.statusbar)

        self.retranslateUi(EntryUi)
        QtCore.QMetaObject.connectSlotsByName(EntryUi)

    def retranslateUi(self, EntryUi):
        _translate = QtCore.QCoreApplication.translate
        EntryUi.setWindowTitle(_translate("EntryUi", "MainWindow"))
        self.query_btn.setText(_translate("EntryUi", "Query"))
        self.info_lbl.setText(_translate("EntryUi", "Some Infomation"))
        self.open_config_btn.setText(_translate("EntryUi", "Open Config"))

