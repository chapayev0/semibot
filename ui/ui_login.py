# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginbwOyFX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(500, 550)
        login.setMinimumSize(QSize(500, 550))
        login.setStyleSheet(u"")
        self.root = QWidget(login)
        self.root.setObjectName(u"root")
        self.verticalLayout = QVBoxLayout(self.root)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.root_back = QStackedWidget(self.root)
        self.root_back.setObjectName(u"root_back")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)

        self.lg_lbl = QLabel(self.page)
        self.lg_lbl.setObjectName(u"lg_lbl")
        self.lg_lbl.setMinimumSize(QSize(100, 50))
        font = QFont()
        font.setFamily(u"Adobe Fan Heiti Std B")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lg_lbl.setFont(font)
        self.lg_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lg_lbl)

        self.lin_frm = QFrame(self.page)
        self.lin_frm.setObjectName(u"lin_frm")
        self.lin_frm.setMaximumSize(QSize(16777215, 93))
        self.lin_frm.setFrameShape(QFrame.StyledPanel)
        self.lin_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.lin_frm)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user = QLineEdit(self.lin_frm)
        self.user.setObjectName(u"user")
        self.user.setMinimumSize(QSize(300, 35))
        self.user.setMaximumSize(QSize(300, 16777215))
        self.user.setStyleSheet(u"QLineEdit{\n"
"\n"
"}")
        self.user.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.user)

        self.pwd = QLineEdit(self.lin_frm)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setMinimumSize(QSize(300, 35))
        self.pwd.setMaximumSize(QSize(300, 16777215))
        self.pwd.setEchoMode(QLineEdit.Password)
        self.pwd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.pwd)


        self.verticalLayout_3.addWidget(self.lin_frm, 0, Qt.AlignHCenter)

        self.btn_frm = QFrame(self.page)
        self.btn_frm.setObjectName(u"btn_frm")
        self.btn_frm.setMaximumSize(QSize(16777215, 100))
        self.btn_frm.setFrameShape(QFrame.StyledPanel)
        self.btn_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.btn_frm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_btn = QPushButton(self.btn_frm)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 50))
        self.login_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.login_btn)

        self.sign_btn = QPushButton(self.btn_frm)
        self.sign_btn.setObjectName(u"sign_btn")
        self.sign_btn.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.sign_btn)


        self.verticalLayout_3.addWidget(self.btn_frm)

        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status_lbl = QLabel(self.frame_2)
        self.status_lbl.setObjectName(u"status_lbl")

        self.horizontalLayout_2.addWidget(self.status_lbl)

        self.exit_btn = QPushButton(self.frame_2)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(0, 30))
        self.exit_btn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.exit_btn)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.root_back.addWidget(self.page)
        self.sign_page = QWidget()
        self.sign_page.setObjectName(u"sign_page")
        self.verticalLayout_4 = QVBoxLayout(self.sign_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.f_name = QLineEdit(self.sign_page)
        self.f_name.setObjectName(u"f_name")
        self.f_name.setMinimumSize(QSize(0, 40))
        self.f_name.setStyleSheet(u"QLineEdit{\n"
"\n"
"color:black;\n"
"                       border: 0px solid;\n"
"                       padding: 0.5px 20px;\n"
"                       margin: 2px 2px;\n"
"                       margin-right:0px;\n"
"	\n"
"                       border: 1px solid;\n"
"	border-color: rgb(185, 185, 185);\n"
"background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"                       border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"\n"
"                       border: 1px solid;\n"
"	border-color: rgb(225, 225, 225);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.f_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.f_name)

        self.l_name = QLineEdit(self.sign_page)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setMinimumSize(QSize(0, 40))
        self.l_name.setStyleSheet(u"QLineEdit{\n"
"\n"
"color:black;\n"
"                       border: 0px solid;\n"
"                       padding: 0.5px 20px;\n"
"                       margin: 2px 2px;\n"
"                       margin-right:0px;\n"
"	\n"
"                       border: 1px solid;\n"
"	border-color: rgb(185, 185, 185);\n"
"background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"                       border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"\n"
"                       border: 1px solid;\n"
"	border-color: rgb(225, 225, 225);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.l_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_name)

        self.mail = QLineEdit(self.sign_page)
        self.mail.setObjectName(u"mail")
        self.mail.setMinimumSize(QSize(0, 40))
        self.mail.setStyleSheet(u"QLineEdit{\n"
"\n"
"color:black;\n"
"                       border: 0px solid;\n"
"                       padding: 0.5px 20px;\n"
"                       margin: 2px 2px;\n"
"                       margin-right:0px;\n"
"	\n"
"                       border: 1px solid;\n"
"	border-color: rgb(185, 185, 185);\n"
"background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"                       border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"\n"
"                       border: 1px solid;\n"
"	border-color: rgb(225, 225, 225);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.mail.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.mail.setEchoMode(QLineEdit.Normal)
        self.mail.setCursorPosition(0)
        self.mail.setAlignment(Qt.AlignCenter)
        self.mail.setClearButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.mail)

        self.addr = QLineEdit(self.sign_page)
        self.addr.setObjectName(u"addr")
        self.addr.setMinimumSize(QSize(0, 40))
        self.addr.setStyleSheet(u"QLineEdit{\n"
"\n"
"color:black;\n"
"                       border: 0px solid;\n"
"                       padding: 0.5px 20px;\n"
"                       margin: 2px 2px;\n"
"                       margin-right:0px;\n"
"	\n"
"                       border: 1px solid;\n"
"	border-color: rgb(185, 185, 185);\n"
"background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"                       border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"\n"
"                       border: 1px solid;\n"
"	border-color: rgb(225, 225, 225);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.addr.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.addr)

        self.contact = QLineEdit(self.sign_page)
        self.contact.setObjectName(u"contact")
        self.contact.setMinimumSize(QSize(0, 40))
        self.contact.setStyleSheet(u"QLineEdit{\n"
"\n"
"color:black;\n"
"                       border: 0px solid;\n"
"                       padding: 0.5px 20px;\n"
"                       margin: 2px 2px;\n"
"                       margin-right:0px;\n"
"	\n"
"                       border: 1px solid;\n"
"	border-color: rgb(185, 185, 185);\n"
"background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"                       border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"\n"
"                       border: 1px solid;\n"
"	border-color: rgb(225, 225, 225);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.contact.setInputMethodHints(Qt.ImhDigitsOnly)
        self.contact.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.contact)

        self.passw = QLineEdit(self.sign_page)
        self.passw.setObjectName(u"passw")
        self.passw.setMinimumSize(QSize(0, 40))
        self.passw.setStyleSheet(u"QLineEdit{\n"
"\n"
"color:black;\n"
"                       border: 0px solid;\n"
"                       padding: 0.5px 20px;\n"
"                       margin: 2px 2px;\n"
"                       margin-right:0px;\n"
"	\n"
"                       border: 1px solid;\n"
"	border-color: rgb(185, 185, 185);\n"
"background-color: rgb(248, 248, 248);\n"
"\n"
"\n"
"                       border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"\n"
"                       border: 1px solid;\n"
"	border-color: rgb(225, 225, 225);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.passw.setEchoMode(QLineEdit.Password)
        self.passw.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.passw)

        self.register_btn = QPushButton(self.sign_page)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.register_btn)

        self.root_back.addWidget(self.sign_page)
        self.confirm_page = QWidget()
        self.confirm_page.setObjectName(u"confirm_page")
        self.verticalLayout_5 = QVBoxLayout(self.confirm_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.confirm_page)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.back_login = QPushButton(self.confirm_page)
        self.back_login.setObjectName(u"back_login")
        self.back_login.setMinimumSize(QSize(0, 40))

        self.verticalLayout_5.addWidget(self.back_login)

        self.root_back.addWidget(self.confirm_page)

        self.verticalLayout.addWidget(self.root_back)

        self.sign_lbl = QLabel(self.root)
        self.sign_lbl.setObjectName(u"sign_lbl")
        self.sign_lbl.setMinimumSize(QSize(0, 20))
        self.sign_lbl.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.sign_lbl)

        login.setCentralWidget(self.root)

        self.retranslateUi(login)

        self.root_back.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
        self.lg_lbl.setText(QCoreApplication.translate("login", u"SAT TEAM", None))
        self.user.setPlaceholderText(QCoreApplication.translate("login", u"Enter your user name", None))
        self.pwd.setPlaceholderText(QCoreApplication.translate("login", u"Enter your password", None))
        self.login_btn.setText(QCoreApplication.translate("login", u"Login", None))
        self.sign_btn.setText(QCoreApplication.translate("login", u"SignUP", None))
        self.status_lbl.setText("")
        self.exit_btn.setText(QCoreApplication.translate("login", u"Exit", None))
        self.f_name.setPlaceholderText(QCoreApplication.translate("login", u"Enter first name", None))
        self.l_name.setPlaceholderText(QCoreApplication.translate("login", u"Enter last name", None))
        self.mail.setPlaceholderText(QCoreApplication.translate("login", u"Enter your  E Mail", None))
        self.addr.setPlaceholderText(QCoreApplication.translate("login", u"Enter your address", None))
        self.contact.setPlaceholderText(QCoreApplication.translate("login", u"Enter contact number", None))
        self.passw.setPlaceholderText(QCoreApplication.translate("login", u"Enter password", None))
        self.register_btn.setText(QCoreApplication.translate("login", u"Register", None))
        self.label.setText(QCoreApplication.translate("login", u"You will recive your acount details via E mail after admins aproval.\n"
" Thank you!", None))
        self.back_login.setText(QCoreApplication.translate("login", u"Back to login", None))
        self.sign_lbl.setText("")
    # retranslateUi

