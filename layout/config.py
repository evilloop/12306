# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui/config.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigUi(object):
    def setupUi(self, ConfigUi):
        ConfigUi.setObjectName("ConfigUi")
        ConfigUi.resize(637, 458)
        self.layoutWidget = QtWidgets.QWidget(ConfigUi)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 561, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.station_dates_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.station_dates_box.setObjectName("station_dates_box")
        self.station_date_input = QtWidgets.QDateEdit(self.station_dates_box)
        self.station_date_input.setGeometry(QtCore.QRect(10, 20, 111, 24))
        self.station_date_input.setObjectName("station_date_input")
        self.station_dates_label = QtWidgets.QLabel(self.station_dates_box)
        self.station_dates_label.setGeometry(QtCore.QRect(10, 50, 60, 16))
        self.station_dates_label.setObjectName("station_dates_label")
        self.gridLayout.addWidget(self.station_dates_box, 0, 0, 1, 1)
        self.ticke_peoples_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.ticke_peoples_box.setObjectName("ticke_peoples_box")
        self.ticke_peoples_box_2 = QtWidgets.QGroupBox(self.ticke_peoples_box)
        self.ticke_peoples_box_2.setGeometry(QtCore.QRect(10, 120, 211, 81))
        self.ticke_peoples_box_2.setObjectName("ticke_peoples_box_2")
        self.gridLayout.addWidget(self.ticke_peoples_box, 0, 1, 1, 1)
        self.station_trains_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.station_trains_box.setObjectName("station_trains_box")
        self.gridLayout.addWidget(self.station_trains_box, 1, 0, 1, 1)
        self.accounts_of_12306_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.accounts_of_12306_box.setObjectName("accounts_of_12306_box")
        self.gridLayout.addWidget(self.accounts_of_12306_box, 1, 1, 1, 1)
        self.station_names_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.station_names_box.setObjectName("station_names_box")
        self.gridLayout.addWidget(self.station_names_box, 2, 0, 1, 1)
        self.set_types_box = QtWidgets.QGroupBox(self.layoutWidget)
        self.set_types_box.setObjectName("set_types_box")
        self.gridLayout.addWidget(self.set_types_box, 3, 0, 1, 1)

        self.retranslateUi(ConfigUi)
        QtCore.QMetaObject.connectSlotsByName(ConfigUi)

    def retranslateUi(self, ConfigUi):
        _translate = QtCore.QCoreApplication.translate
        ConfigUi.setWindowTitle(_translate("ConfigUi", "Form"))
        self.station_dates_box.setTitle(_translate("ConfigUi", "Station Dates"))
        self.station_dates_label.setText(_translate("ConfigUi", "TextLabel"))
        self.ticke_peoples_box.setTitle(_translate("ConfigUi", "Ticke Peoples"))
        self.ticke_peoples_box_2.setTitle(_translate("ConfigUi", "Ticke Peoples"))
        self.station_trains_box.setTitle(_translate("ConfigUi", "Station Trains"))
        self.accounts_of_12306_box.setTitle(_translate("ConfigUi", "12306 Accounts"))
        self.station_names_box.setTitle(_translate("ConfigUi", "Station Names"))
        self.set_types_box.setTitle(_translate("ConfigUi", "Set Type"))

