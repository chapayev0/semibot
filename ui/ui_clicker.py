# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clickerQfRUlj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import os
import sys
THIS_DIR = os.path.dirname(__file__)
CODE_DIR = os.path.abspath(os.path.join(THIS_DIR, '..', 'ui'))
sys.path.append(CODE_DIR)
import ui.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1158, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.action_name_edit = QLineEdit(self.frame_13)
        self.action_name_edit.setObjectName(u"action_name_edit")

        self.horizontalLayout_8.addWidget(self.action_name_edit)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_17)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_17)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 0))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_41)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_9)


        self.verticalLayout_17.addWidget(self.frame_41)

        self.frame_40 = QFrame(self.frame_17)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.type_key = QPushButton(self.frame_40)
        self.type_key.setObjectName(u"type_key")

        self.horizontalLayout_27.addWidget(self.type_key)

        self.type_click = QPushButton(self.frame_40)
        self.type_click.setObjectName(u"type_click")

        self.horizontalLayout_27.addWidget(self.type_click)

        self.type_double_click = QPushButton(self.frame_40)
        self.type_double_click.setObjectName(u"type_double_click")

        self.horizontalLayout_27.addWidget(self.type_double_click)

        self.type_delay = QPushButton(self.frame_40)
        self.type_delay.setObjectName(u"type_delay")

        self.horizontalLayout_27.addWidget(self.type_delay)

        self.copy_action = QPushButton(self.frame_40)
        self.copy_action.setObjectName(u"copy_action")

        self.horizontalLayout_27.addWidget(self.copy_action)


        self.verticalLayout_17.addWidget(self.frame_40)

        self.frame_42 = QFrame(self.frame_17)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 30))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, -1)
        self.label_16 = QLabel(self.frame_42)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.delay_time = QLineEdit(self.frame_42)
        self.delay_time.setObjectName(u"delay_time")

        self.horizontalLayout_11.addWidget(self.delay_time)


        self.verticalLayout_17.addWidget(self.frame_42)


        self.verticalLayout_6.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.x_pos_edit = QLineEdit(self.frame_16)
        self.x_pos_edit.setObjectName(u"x_pos_edit")

        self.horizontalLayout_7.addWidget(self.x_pos_edit)

        self.y_pos_edit = QLineEdit(self.frame_16)
        self.y_pos_edit.setObjectName(u"y_pos_edit")

        self.horizontalLayout_7.addWidget(self.y_pos_edit)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_23 = QFrame(self.frame_12)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.action_type_cp = QLabel(self.frame_23)
        self.action_type_cp.setObjectName(u"action_type_cp")
        self.action_type_cp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.action_type_cp)


        self.verticalLayout_6.addWidget(self.frame_23)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.key_content_edit = QLineEdit(self.frame_14)
        self.key_content_edit.setObjectName(u"key_content_edit")

        self.horizontalLayout_9.addWidget(self.key_content_edit)


        self.verticalLayout_5.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.clear_btn = QPushButton(self.frame_15)
        self.clear_btn.setObjectName(u"clear_btn")

        self.horizontalLayout_10.addWidget(self.clear_btn)

        self.number = QLineEdit(self.frame_15)
        self.number.setObjectName(u"number")

        self.horizontalLayout_10.addWidget(self.number)

        self.add_btn = QPushButton(self.frame_15)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout_10.addWidget(self.add_btn)


        self.verticalLayout_5.addWidget(self.frame_15)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(200, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.frame_20)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.selected_action = QLineEdit(self.frame_20)
        self.selected_action.setObjectName(u"selected_action")

        self.horizontalLayout_13.addWidget(self.selected_action)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.frame_11)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_11 = QLabel(self.frame_22)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.times = QLineEdit(self.frame_22)
        self.times.setObjectName(u"times")
        self.times.setClearButtonEnabled(False)

        self.horizontalLayout_14.addWidget(self.times)


        self.verticalLayout_7.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.frame_11)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.stop = QPushButton(self.frame_21)
        self.stop.setObjectName(u"stop")

        self.horizontalLayout_15.addWidget(self.stop)

        self.start = QPushButton(self.frame_21)
        self.start.setObjectName(u"start")

        self.horizontalLayout_15.addWidget(self.start)


        self.verticalLayout_7.addWidget(self.frame_21)


        self.horizontalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 300))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.action_list = QListWidget(self.frame_6)
        self.action_list.setObjectName(u"action_list")

        self.verticalLayout_3.addWidget(self.action_list)

        self.del_row = QPushButton(self.frame_6)
        self.del_row.setObjectName(u"del_row")

        self.verticalLayout_3.addWidget(self.del_row)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.action_list_name = QLabel(self.frame_5)
        self.action_list_name.setObjectName(u"action_list_name")

        self.horizontalLayout_5.addWidget(self.action_list_name)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.action_content_list = QListWidget(self.frame_7)
        self.action_content_list.setObjectName(u"action_content_list")

        self.verticalLayout_4.addWidget(self.action_content_list)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 30))
        self.frame_19.setMaximumSize(QSize(16777215, 30))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_19)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.mouse_pos_lbl = QLabel(self.frame_19)
        self.mouse_pos_lbl.setObjectName(u"mouse_pos_lbl")

        self.horizontalLayout_12.addWidget(self.mouse_pos_lbl)


        self.verticalLayout.addWidget(self.frame_19)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_25 = QFrame(self.frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.link_mailbtn = QPushButton(self.frame_25)
        self.link_mailbtn.setObjectName(u"link_mailbtn")

        self.horizontalLayout_17.addWidget(self.link_mailbtn)

        self.new_mail_btn = QPushButton(self.frame_25)
        self.new_mail_btn.setObjectName(u"new_mail_btn")

        self.horizontalLayout_17.addWidget(self.new_mail_btn)

        self.usr_name_btn = QPushButton(self.frame_25)
        self.usr_name_btn.setObjectName(u"usr_name_btn")

        self.horizontalLayout_17.addWidget(self.usr_name_btn)

        self.cmnt_page = QPushButton(self.frame_25)
        self.cmnt_page.setObjectName(u"cmnt_page")

        self.horizontalLayout_17.addWidget(self.cmnt_page)

        self.setting_btn = QPushButton(self.frame_25)
        self.setting_btn.setObjectName(u"setting_btn")

        self.horizontalLayout_17.addWidget(self.setting_btn)

        self.file_auto_btn = QPushButton(self.frame_25)
        self.file_auto_btn.setObjectName(u"file_auto_btn")

        self.horizontalLayout_17.addWidget(self.file_auto_btn)


        self.verticalLayout_8.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.frame_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_24)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.link_mail = QWidget()
        self.link_mail.setObjectName(u"link_mail")
        self.verticalLayout_9 = QVBoxLayout(self.link_mail)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.link_mail)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 50))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.add_link_mail = QLineEdit(self.frame_26)
        self.add_link_mail.setObjectName(u"add_link_mail")
        self.add_link_mail.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.add_link_mail)

        self.add_link_mail_btn = QPushButton(self.frame_26)
        self.add_link_mail_btn.setObjectName(u"add_link_mail_btn")

        self.horizontalLayout_19.addWidget(self.add_link_mail_btn)


        self.verticalLayout_9.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.link_mail)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 50))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lineEdit_2 = QLineEdit(self.frame_27)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setClearButtonEnabled(True)

        self.horizontalLayout_20.addWidget(self.lineEdit_2)

        self.add_bulk_mail = QPushButton(self.frame_27)
        self.add_bulk_mail.setObjectName(u"add_bulk_mail")

        self.horizontalLayout_20.addWidget(self.add_bulk_mail)


        self.verticalLayout_9.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.link_mail)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.link_mai_list = QListWidget(self.frame_28)
        self.link_mai_list.setObjectName(u"link_mai_list")

        self.horizontalLayout_21.addWidget(self.link_mai_list)


        self.verticalLayout_9.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.link_mail)
        self.new_gmail = QWidget()
        self.new_gmail.setObjectName(u"new_gmail")
        self.verticalLayout_10 = QVBoxLayout(self.new_gmail)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_44 = QFrame(self.new_gmail)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_44)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gmail_edit = QLineEdit(self.frame_44)
        self.gmail_edit.setObjectName(u"gmail_edit")
        self.gmail_edit.setClearButtonEnabled(True)

        self.verticalLayout_18.addWidget(self.gmail_edit)

        self.password_edit = QLineEdit(self.frame_44)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setClearButtonEnabled(True)

        self.verticalLayout_18.addWidget(self.password_edit)

        self.link_mail_2 = QLineEdit(self.frame_44)
        self.link_mail_2.setObjectName(u"link_mail_2")
        self.link_mail_2.setClearButtonEnabled(True)

        self.verticalLayout_18.addWidget(self.link_mail_2)

        self.link_poone = QLineEdit(self.frame_44)
        self.link_poone.setObjectName(u"link_poone")
        self.link_poone.setClearButtonEnabled(True)

        self.verticalLayout_18.addWidget(self.link_poone)

        self.addd_mail_btn = QPushButton(self.frame_44)
        self.addd_mail_btn.setObjectName(u"addd_mail_btn")

        self.verticalLayout_18.addWidget(self.addd_mail_btn)


        self.verticalLayout_10.addWidget(self.frame_44)

        self.frame_29 = QFrame(self.new_gmail)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 300))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.new_mail_list = QListWidget(self.frame_29)
        self.new_mail_list.setObjectName(u"new_mail_list")

        self.horizontalLayout_22.addWidget(self.new_mail_list)


        self.verticalLayout_10.addWidget(self.frame_29)

        self.frame_46 = QFrame(self.new_gmail)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_18 = QLabel(self.frame_46)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_31.addWidget(self.label_18)

        self.gmail_count = QLabel(self.frame_46)
        self.gmail_count.setObjectName(u"gmail_count")

        self.horizontalLayout_31.addWidget(self.gmail_count)


        self.verticalLayout_10.addWidget(self.frame_46)

        self.frame_30 = QFrame(self.new_gmail)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 50))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_30)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_12 = QLabel(self.frame_31)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_23.addWidget(self.label_12)

        self.gmail_det = QLineEdit(self.frame_31)
        self.gmail_det.setObjectName(u"gmail_det")

        self.horizontalLayout_23.addWidget(self.gmail_det)


        self.verticalLayout_11.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_13 = QLabel(self.frame_32)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_24.addWidget(self.label_13)

        self.password_det = QLineEdit(self.frame_32)
        self.password_det.setObjectName(u"password_det")

        self.horizontalLayout_24.addWidget(self.password_det)


        self.verticalLayout_11.addWidget(self.frame_32)

        self.frame_45 = QFrame(self.frame_30)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_17 = QLabel(self.frame_45)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_30.addWidget(self.label_17)

        self.link_mobile_det = QLineEdit(self.frame_45)
        self.link_mobile_det.setObjectName(u"link_mobile_det")

        self.horizontalLayout_30.addWidget(self.link_mobile_det)


        self.verticalLayout_11.addWidget(self.frame_45)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_14 = QLabel(self.frame_33)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_25.addWidget(self.label_14)

        self.link_mail_det = QLineEdit(self.frame_33)
        self.link_mail_det.setObjectName(u"link_mail_det")

        self.horizontalLayout_25.addWidget(self.link_mail_det)


        self.verticalLayout_11.addWidget(self.frame_33)


        self.verticalLayout_10.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.new_gmail)
        self.user_name = QWidget()
        self.user_name.setObjectName(u"user_name")
        self.verticalLayout_14 = QVBoxLayout(self.user_name)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_38 = QFrame(self.user_name)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_38)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.f_name = QLineEdit(self.frame_38)
        self.f_name.setObjectName(u"f_name")
        self.f_name.setClearButtonEnabled(True)

        self.verticalLayout_15.addWidget(self.f_name)

        self.l_name = QLineEdit(self.frame_38)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setClearButtonEnabled(True)

        self.verticalLayout_15.addWidget(self.l_name)

        self.add_usr_btn = QPushButton(self.frame_38)
        self.add_usr_btn.setObjectName(u"add_usr_btn")

        self.verticalLayout_15.addWidget(self.add_usr_btn)


        self.verticalLayout_14.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.user_name)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_39)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.user_list = QListWidget(self.frame_39)
        self.user_list.setObjectName(u"user_list")

        self.verticalLayout_16.addWidget(self.user_list)


        self.verticalLayout_14.addWidget(self.frame_39)

        self.stackedWidget.addWidget(self.user_name)
        self.comment_page = QWidget()
        self.comment_page.setObjectName(u"comment_page")
        self.verticalLayout_21 = QVBoxLayout(self.comment_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.inp_comment = QLineEdit(self.comment_page)
        self.inp_comment.setObjectName(u"inp_comment")
        self.inp_comment.setClearButtonEnabled(True)

        self.verticalLayout_21.addWidget(self.inp_comment)

        self.add_comment_btn = QPushButton(self.comment_page)
        self.add_comment_btn.setObjectName(u"add_comment_btn")

        self.verticalLayout_21.addWidget(self.add_comment_btn)

        self.comment_list = QListWidget(self.comment_page)
        self.comment_list.setObjectName(u"comment_list")

        self.verticalLayout_21.addWidget(self.comment_list)

        self.stackedWidget.addWidget(self.comment_page)
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.verticalLayout_12 = QVBoxLayout(self.setting)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_34 = QFrame(self.setting)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_34)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_15 = QLabel(self.frame_37)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_26.addWidget(self.label_15)

        self.password_inp = QLineEdit(self.frame_37)
        self.password_inp.setObjectName(u"password_inp")

        self.horizontalLayout_26.addWidget(self.password_inp)


        self.verticalLayout_13.addWidget(self.frame_37)

        self.frame_18 = QFrame(self.frame_34)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_18)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.date_inp = QLineEdit(self.frame_18)
        self.date_inp.setObjectName(u"date_inp")

        self.horizontalLayout_2.addWidget(self.date_inp)


        self.verticalLayout_13.addWidget(self.frame_18)

        self.frame_43 = QFrame(self.frame_34)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_2 = QLabel(self.frame_43)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_29.addWidget(self.label_2)

        self.year_inp = QLineEdit(self.frame_43)
        self.year_inp.setObjectName(u"year_inp")

        self.horizontalLayout_29.addWidget(self.year_inp)


        self.verticalLayout_13.addWidget(self.frame_43)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_35 = QLabel(self.frame_36)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_32.addWidget(self.label_35)

        self.mail_count_from = QLineEdit(self.frame_36)
        self.mail_count_from.setObjectName(u"mail_count_from")

        self.horizontalLayout_32.addWidget(self.mail_count_from)


        self.verticalLayout_13.addWidget(self.frame_36)

        self.scrollArea = QScrollArea(self.frame_34)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 397, 400))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.frame_35 = QFrame(self.scrollAreaWidgetContents)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 400))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_35)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_19 = QLabel(self.frame_35)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_35)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_19.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_35)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_19.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_35)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_19.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_35)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_19.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_35)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_19.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_35)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_19.addWidget(self.label_25)

        self.label_27 = QLabel(self.frame_35)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_19.addWidget(self.label_27)

        self.label_26 = QLabel(self.frame_35)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_19.addWidget(self.label_26)

        self.label_28 = QLabel(self.frame_35)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_19.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_35)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_19.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_35)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_19.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_35)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_19.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_35)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_19.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_35)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_19.addWidget(self.label_33)

        self.label_36 = QLabel(self.frame_35)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_19.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_35)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_19.addWidget(self.label_37)

        self.label_34 = QLabel(self.frame_35)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_19.addWidget(self.label_34)


        self.verticalLayout_20.addWidget(self.frame_35)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_12.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.setting)
        self.file_automate = QWidget()
        self.file_automate.setObjectName(u"file_automate")
        self.verticalLayout_22 = QVBoxLayout(self.file_automate)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_47 = QFrame(self.file_automate)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.file_path = QLineEdit(self.frame_47)
        self.file_path.setObjectName(u"file_path")

        self.horizontalLayout_33.addWidget(self.file_path)

        self.separator = QLineEdit(self.frame_47)
        self.separator.setObjectName(u"separator")

        self.horizontalLayout_33.addWidget(self.separator)


        self.verticalLayout_22.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.file_automate)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.from_left = QRadioButton(self.frame_48)
        self.from_left.setObjectName(u"from_left")
        self.from_left.setChecked(True)

        self.horizontalLayout_34.addWidget(self.from_left)

        self.from_right = QRadioButton(self.frame_48)
        self.from_right.setObjectName(u"from_right")

        self.horizontalLayout_34.addWidget(self.from_right)

        self.colum_ids = QLineEdit(self.frame_48)
        self.colum_ids.setObjectName(u"colum_ids")

        self.horizontalLayout_34.addWidget(self.colum_ids)


        self.verticalLayout_22.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.file_automate)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.beginning_prefix_line_edit = QLineEdit(self.frame_49)
        self.beginning_prefix_line_edit.setObjectName(u"beginning_prefix_line_edit")

        self.horizontalLayout_35.addWidget(self.beginning_prefix_line_edit)

        self.center_prefix_line_edit = QLineEdit(self.frame_49)
        self.center_prefix_line_edit.setObjectName(u"center_prefix_line_edit")

        self.horizontalLayout_35.addWidget(self.center_prefix_line_edit)

        self.end_prefix_line_edit = QLineEdit(self.frame_49)
        self.end_prefix_line_edit.setObjectName(u"end_prefix_line_edit")

        self.horizontalLayout_35.addWidget(self.end_prefix_line_edit)


        self.verticalLayout_22.addWidget(self.frame_49)

        self.file_read_btn = QPushButton(self.file_automate)
        self.file_read_btn.setObjectName(u"file_read_btn")

        self.verticalLayout_22.addWidget(self.file_read_btn)

        self.speci_text_fix = QPlainTextEdit(self.file_automate)
        self.speci_text_fix.setObjectName(u"speci_text_fix")

        self.verticalLayout_22.addWidget(self.speci_text_fix)

        self.file_text_list = QListWidget(self.file_automate)
        self.file_text_list.setObjectName(u"file_text_list")

        self.verticalLayout_22.addWidget(self.file_text_list)

        self.stackedWidget.addWidget(self.file_automate)

        self.horizontalLayout_18.addWidget(self.stackedWidget)


        self.verticalLayout_8.addWidget(self.frame_24)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Action Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Action Type:", None))
        self.type_key.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.type_click.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.type_double_click.setText(QCoreApplication.translate("MainWindow", u"Double click", None))
        self.type_delay.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.copy_action.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Delay Time", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Click Action", None))
        self.x_pos_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X Position", None))
        self.y_pos_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y Position", None))
        self.action_type_cp.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Keyword Action", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Select Action", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Action run times:", None))
        self.times.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Action List", None))
        self.del_row.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Actions content List:", None))
        self.action_list_name.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mouse Pos: X,Y", None))
        self.mouse_pos_lbl.setText("")
        self.link_mailbtn.setText(QCoreApplication.translate("MainWindow", u"Link Gmail", None))
        self.new_mail_btn.setText(QCoreApplication.translate("MainWindow", u"New Gmail", None))
        self.usr_name_btn.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.cmnt_page.setText(QCoreApplication.translate("MainWindow", u"Comment", None))
        self.setting_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.file_auto_btn.setText(QCoreApplication.translate("MainWindow", u"File Auto", None))
        self.add_link_mail_btn.setText(QCoreApplication.translate("MainWindow", u"Add Gmail", None))
        self.add_bulk_mail.setText(QCoreApplication.translate("MainWindow", u"Add Bulk Gmail", None))
        self.gmail_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gmail", None))
        self.password_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.link_mail_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link mail", None))
        self.link_poone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Linked mobile", None))
        self.addd_mail_btn.setText(QCoreApplication.translate("MainWindow", u"Add New Gmail", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Gmail Count:", None))
        self.gmail_count.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gmail", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Passowrd", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Linked Mobile", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Linked Gmail", None))
        self.add_usr_btn.setText(QCoreApplication.translate("MainWindow", u"Add User Name", None))
        self.add_comment_btn.setText(QCoreApplication.translate("MainWindow", u"Add Comment", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.password_inp.setText(QCoreApplication.translate("MainWindow", u"Shashika@1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.date_inp.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.year_inp.setText(QCoreApplication.translate("MainWindow", u"1998", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Login Gmail Count from ", None))
        self.mail_count_from.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Key Words", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"f_name : Type first name automaticly", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"l_name : Type last name automaticly", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"password : Type password automaticly", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"date : Type date automaticly", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"year : Type Year automaticly", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"space : Type space or scroll down automaticly", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"write_out : Save created gmail to database automaticly", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"reco_mail : Type recover mail automaticly", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"login_mail : Type gmail automaticly", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"login_pass: Type previously enterd gmail password automaticly", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"comment: Type a random comment from list automaticly", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"up_arw: Press Up Arrow key", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"down_arw: Press Down arrow key", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"page_up: Press Page up Key", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"enter:press enter", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"file_list:gate data from file list one by one", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"page_down: Press page down key", None))
        self.file_path.setText("")
        self.file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"file path", None))
        self.separator.setPlaceholderText(QCoreApplication.translate("MainWindow", u"data separator prefix", None))
        self.from_left.setText(QCoreApplication.translate("MainWindow", u"Left>", None))
        self.from_right.setText(QCoreApplication.translate("MainWindow", u"<Right", None))
        self.colum_ids.setPlaceholderText(QCoreApplication.translate("MainWindow", u"add column numbers to scrap", None))
        self.beginning_prefix_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"beginning prefix charactor", None))
        self.center_prefix_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"middle prefix charactor", None))
        self.end_prefix_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"end prefix charactor", None))
        self.file_read_btn.setText(QCoreApplication.translate("MainWindow", u"Read File", None))
        self.speci_text_fix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"add specila text to add on", None))
    # retranslateUi

