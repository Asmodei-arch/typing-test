# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_designer_files/choose_mode.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 488)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.boringMode = QtWidgets.QPushButton(Form)
        self.boringMode.setObjectName("boringMode")
        self.verticalLayout.addWidget(self.boringMode)
        self.oneErrorMode = QtWidgets.QPushButton(Form)
        self.oneErrorMode.setObjectName("oneErrorMode")
        self.verticalLayout.addWidget(self.oneErrorMode)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выбор режима"))
        self.boringMode.setText(_translate("Form", "Просто набор текста"))
        self.oneErrorMode.setText(_translate("Form", "Без права на ошибку"))
