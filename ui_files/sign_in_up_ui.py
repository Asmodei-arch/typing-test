# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_designer_files/sign_in_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.loginInput = QtWidgets.QLineEdit(Form)
        self.loginInput.setObjectName("loginInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginInput)
        self.passwordInput = QtWidgets.QLineEdit(Form)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.verticalLayout.addLayout(self.formLayout)
        self.errorField = QtWidgets.QLineEdit(Form)
        self.errorField.setReadOnly(True)
        self.errorField.setObjectName("errorField")
        self.verticalLayout.addWidget(self.errorField)
        self.signButton = QtWidgets.QPushButton(Form)
        self.signButton.setText("")
        self.signButton.setObjectName("signButton")
        self.verticalLayout.addWidget(self.signButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "Логин"))
        self.label_2.setText(_translate("Form", "Пароль"))
