# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.login_user = QtWidgets.QLineEdit(self.centralwidget)
        self.login_user.setObjectName("login_user")
        self.horizontalLayout.addWidget(self.login_user)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.login_passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.login_passwd.setObjectName("login_passwd")
        self.horizontalLayout_2.addWidget(self.login_passwd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout.addWidget(self.btn_login)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_go_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go_register.setStyleSheet("border: none;\n"
"color: blue;\n"
"margin-right: 10px")
        self.btn_go_register.setObjectName("btn_go_register")
        self.horizontalLayout_3.addWidget(self.btn_go_register)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆"))
        self.label.setText(_translate("MainWindow", "账号："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.btn_login.setText(_translate("MainWindow", "登陆"))
        self.btn_go_register.setText(_translate("MainWindow", "注册"))
