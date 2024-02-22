# -*- coding: utf-8 -*-
import sys
import pyautogui
import pyperclip
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sqlite3
import time
import ctypes
import threading  # Import threading module

import os
import ui.resource_rc
from ui.ui_clicker import Ui_MainWindow
from ui.ui_login import Ui_login

action_type = 0
new_gmail = ""
new_gmail_password = ""
new_gmail_link = ""
mail_count_from = 0
login_mail = ""
file_auto_item_count = 0
file_auto_current_item_count_number = 0

writing_done = False
x_position1 = 100  # Update with desired x-coordinate for position 1
y_position1 = 100  # Update with desired y-coordinate for position 1
x_position2 = 200  # Update with desired x-coordinate for position 2
y_position2 = 200  # Update with desired y-coordinate for position 2
class WorkerThread(QtCore.QThread):
    action_completed = QtCore.Signal()

    def __init__(self, function, *args, **kwargs):
        super(WorkerThread, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.function(*self.args, **self.kwargs)
        self.action_completed.emit()


class login_ui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.root_back.setCurrentWidget(self.ui.page)
        self.dashboard = Main_ui()
        icon = QIcon(":/image/styles/logo.png")
        self.task_icon()
        self.setWindowIcon(icon)
        self.setWindowTitle("SemiBot Login")
        self.ui.login_btn.clicked.connect(self.load_dashboard)
        self.ui.exit_btn.clicked.connect(self.terminate)
        self.ui.pwd.returnPressed.connect(self.load_dashboard)

    def task_icon(self):
        AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(AppUserModelID)

    def terminate(self):
        self.close()

    def load_dashboard(self):
        global teacher_statu
        usr_name = self.ui.user.text()
        usr_pass = self.ui.pwd.text()
        db = sqlite3.connect("data/local.db")
        db.text_factory
        data = db.execute(""" SELECT * FROM login_data""")
        if usr_name == "" and usr_pass == "":
            self.ui.status_lbl.setText("Please enter username and password")
        else:
            for line in data:
                usr = line[0]
                pwd = line[1]
                print(usr)
                print(pwd)
                if usr_name == usr and usr_pass == pwd:
                    self.dashboard.show()
                    self.close()
                else:
                    self.ui.status_lbl.setText("Check your credentials and try again!")


class Main_ui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pyautogui.position()
        self.time = QTimer()
        icon = QIcon(":/image/styles/logo.png")
        self.task_icon()
        self.setWindowIcon(icon)
        self.setWindowTitle("SemiBot Dashboard")
        self.mouse_capture_sortcut = QShortcut(QKeySequence(Qt.ALT + Qt.Key_C), self)
        self.sortcut_copy = QShortcut(QKeySequence(Qt.ALT + Qt.Key_Z), self)
        self.sortcut_copy1 = QShortcut(QKeySequence(Qt.ALT + Qt.Key_V), self)
        self.mouse_capture_sortcut.activated.connect(self.static_c_pos_capture)
        self.time.setInterval(5)
        self.time.timeout.connect(self.dynamic_c_pos)
        self.time.start()
        self.update_action_list()
        self.ui.action_list.itemClicked.connect(self.update_action_content_list)
        self.ui.frame_16.hide()
        self.ui.frame_14.hide()
        self.ui.frame_23.hide()
        self.ui.frame_42.hide()
        self.ui.type_key.clicked.connect(self.type_key)
        self.ui.type_click.clicked.connect(self.type_click)
        self.ui.type_delay.clicked.connect(self.type_delay)
        self.ui.add_btn.clicked.connect(self.update_data_base)
        self.ui.start.clicked.connect(self.loop_run_start)
        self.ui.type_double_click.clicked.connect(self.type_double_click)
        self.ui.copy_action.clicked.connect(self.type_copy)
        self.sortcut_copy.activated.connect(self.hid)
        self.sortcut_copy1.activated.connect(self.hid1)
        self.ui.link_mailbtn.clicked.connect(self.link_mail_page)
        self.ui.new_mail_btn.clicked.connect(self.new_mail_page)
        self.ui.usr_name_btn.clicked.connect(self.usr_name_page)
        self.ui.setting_btn.clicked.connect(self.setting_page)
        self.ui.file_auto_btn.clicked.connect(self.file_auto_page)
        self.ui.del_row.clicked.connect(self.delete_row)
        self.ui.cmnt_page.clicked.connect(self.comment_page)
        self.ui.add_comment_btn.clicked.connect(self.add_comment)
        self.ui.add_usr_btn.clicked.connect(self.add_user_name_single)
        self.ui.addd_mail_btn.clicked.connect(self.add_new_gmail)
        self.ui.new_mail_list.itemClicked.connect(self.new_gmail_clicked)
        self.ui.add_link_mail_btn.clicked.connect(self.add_link_mail_single)
        self.ui.file_read_btn.clicked.connect(self.process_file)

    def task_icon(self):
        AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(AppUserModelID)

    def process_file(self):
        thread = WorkerThread(self.process_file_worker)
        thread.start()

    def process_file(self):


        self.ui.file_text_list.clear()
        file_path = self.ui.file_path.text()
        separator = self.ui.separator.text()
        alignment = "left" if self.ui.from_left.isChecked() else "right"
        column_ids = [int(id) for id in self.ui.colum_ids.text().split(',')]
        beginning_prefix = self.ui.beginning_prefix_line_edit.text()
        center_prefix = self.ui.center_prefix_line_edit.text()
        end_prefix = self.ui.end_prefix_line_edit.text()

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                result = []
                for line in lines:
                    parts = line.strip().split(separator)
                    selected_columns = [parts[i] for i in column_ids if i < len(parts)]
                    formatted_line = ""
                    if beginning_prefix:
                        formatted_line += beginning_prefix
                    for i, col in enumerate(selected_columns):
                        if i > 0 and center_prefix:
                            formatted_line += center_prefix
                        formatted_line += col
                    if end_prefix:
                        formatted_line += end_prefix
                    if alignment == "right":
                        formatted_line = formatted_line[::-1]
                    # result.append(formatted_line)
                    self.ui.file_text_list.addItem(formatted_line)
        except FileNotFoundError:
            self.ui.label_4.setText("File not found.")
        except Exception as e:
            self.ui.label_4.setText(f"An error occurred: {str(e)}")

        # print(self.ui.file_text_list.item(5).text())
        # print(self.ui.file_text_list.count())

    def task_icon(self):

        AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(AppUserModelID)

    def hid(self):
        self.hide()

    def hid1(self):
        self.show()

    def mouseMoveEvent(self, QMouseEvent):

        pass

    def dynamic_c_pos(self):
        self.time.start()
        self.ui.mouse_pos_lbl.setText(str(QCursor.pos().x()) + "," + str(QCursor.pos().y()))

    def static_c_pos_capture(self):
        self.ui.x_pos_edit.setText(str(QCursor.pos().x()))
        self.ui.y_pos_edit.setText(str(QCursor.pos().y()))

    def update_action_list(self):
        self.ui.action_list.clear()
        db = sqlite3.connect("data/local.db")
        db.text_factory

        data = db.execute(""" SELECT * FROM action_list""")

        lst = []

        for info in data:

            act = info[0]

            if act not in lst:
                lst.append(act)
                self.ui.action_list.addItem(act)

    def update_action_content_list(self):
        db = sqlite3.connect("data/local.db")
        db.text_factory
        self.ui.action_content_list.clear()

        word = str(self.ui.action_list.currentItem().text())
        self.ui.action_list_name.setText(word)
        self.ui.selected_action.setText(word)

        data = db.execute(""" SELECT * FROM action_list WHERE place='%s'""" % (word))

        for info in data:
            type = info[1]
            x_pos = info[2]
            y_pos = info[3]
            content = info[4]
            sub_place = info[5]
            delay_time = info[6]

            self.ui.action_content_list.addItem(
                "Type:" + type + "| X_Pos:" + x_pos + "| Y_Pos:" + y_pos + "| Content:" + content + "|Delay: " + delay_time + "||" + sub_place)

    def update_data_base(self):
        global action_type

        db = sqlite3.connect("data/local.db")
        cursor = db.cursor()

        place = self.ui.action_name_edit.text()
        xpos = self.ui.x_pos_edit.text()
        ypos = self.ui.y_pos_edit.text()
        action_type_edit = ""
        a_content = self.ui.key_content_edit.text()
        number = self.ui.number.text()
        delay_time = self.ui.delay_time.text()

        if action_type == 1:

            action_type_edit = "key"
            xpos = "-"
            ypos = "-"
            delay_time = "-"

        elif action_type == 2:

            action_type_edit = "click"
            a_content = "-"
            delay_time = "-"

        elif action_type == 3:

            action_type_edit = "double_click"
            a_content = "-"
            delay_time = "-"

        elif action_type == 4:

            action_type_edit = "copy"
            xpos = "-"
            ypos = "-"
            delay_time = "-"

        elif action_type == 5:

            action_type_edit = "delay"
            xpos = "-"
            ypos = "-"
            a_content = "-"

        data_tup = (place, action_type_edit, xpos, ypos, a_content, number, delay_time)

        sqlite_insert = """ INSERT INTO 'action_list'
                                                         ('place', 'type', 'x_pos', 'y_pos', 'content', 'sub_place', 'delay_time') VALUES (?, ?, ?, ?, ?, ?, ?)"""

        cursor.execute(sqlite_insert, data_tup)
        db.commit()
        self.update_action_list()

    def type_key(self):

        global action_type

        action_type = 1
        self.ui.frame_14.show()
        self.ui.frame_16.hide()
        self.ui.frame_42.hide()
        self.ui.frame_23.hide()

    def type_click(self):

        global action_type

        action_type = 2
        self.ui.frame_16.show()
        self.ui.label_7.setText("click action")
        self.ui.frame_14.hide()
        self.ui.frame_42.hide()
        self.ui.frame_23.hide()

    def type_double_click(self):

        global action_type

        action_type = 3
        self.ui.frame_16.show()
        self.ui.label_7.setText("Double click action")
        self.ui.frame_14.hide()
        self.ui.frame_23.hide()
        self.ui.frame_42.hide()

    def type_copy(self):

        global action_type

        action_type = 4
        self.ui.frame_23.show()
        self.ui.action_type_cp.setText("Action: Copy")
        self.ui.frame_14.show()
        self.ui.frame_16.hide()
        self.ui.frame_42.hide()

    def random_mouse_move(self):

        global  writing_done, x_position1, y_position1, x_position2, y_position2


        alternate = False
        while not writing_done:
            if alternate:
                pyautogui.moveTo(x_position2, y_position2)
            else:
                pyautogui.moveTo(x_position1, y_position1)
            alternate = not alternate
            time.sleep(0.5)




    def type_delay(self):

        global action_type

        action_type = 5
        self.ui.frame_42.show()
        self.ui.frame_23.hide()
        self.ui.action_type_cp.setText("Action: Copy")
        self.ui.frame_14.hide()
        self.ui.frame_16.hide()

    def file_lit_action(self):
        global file_auto_item_count, file_auto_current_item_count_number, writing_done, x_position, y_position

        file_auto_item_count = self.ui.file_text_list.count()

        list_text = self.ui.file_text_list.item(file_auto_current_item_count_number).text()
        fix_text = self.ui.speci_text_fix.toPlainText()

        final_text = list_text #+ fix_text

        pyautogui.write(final_text)

        file_auto_current_item_count_number += 1


    def start_actions(self):

        global new_gmail, new_gmail_link, new_gmail_password
        global mail_count_from, login_mail, file_auto_item_count, file_auto_current_item_count_number

        db = sqlite3.connect("data/local.db")
        db.text_factory

        word = str(self.ui.selected_action.text())

        data = db.execute(""" SELECT * FROM action_list where place = '%s'""" % (word))

        for info in data:
            a_type = info[1]
            cont = info[4]

            if a_type == "click":
                xpos = info[2]
                ypos = info[3]

                pyautogui.leftClick(int(xpos), int(ypos))

            elif a_type == "key" and cont == "f_name":

                db = sqlite3.connect("data/local.db")
                db.text_factory

                data = db.execute(""" SELECT * FROM user_name  ORDER BY RANDOM() LIMIT 1""")

                for data1 in data:
                    fname = data1[0]

                pyautogui.write(fname)

            elif a_type == "key" and cont == "l_name":

                db = sqlite3.connect("data/local.db")
                db.text_factory

                data = db.execute(""" SELECT * FROM user_name  ORDER BY RANDOM() LIMIT 1""")

                for data1 in data:
                    lname = data1[0]

                pyautogui.write(lname)

            elif a_type == "key" and cont == "password":

                pasw = self.ui.password_inp.text()

                pyautogui.write(pasw)
                new_gmail_password = pasw

            elif a_type == "key" and cont == "comment":

                db = sqlite3.connect("data/local.db")
                db.text_factory

                data = db.execute(""" SELECT * FROM comment  ORDER BY RANDOM() LIMIT 1""")

                for data1 in data:
                    comnt = data1[0]

                pyautogui.write(comnt)


            elif a_type == "key" and cont == "date":

                date = self.ui.date_inp.text()

                pyautogui.write(date)

            elif a_type == "key" and cont == "year":

                year = self.ui.year_inp.text()

                pyautogui.write(year)

            elif a_type == "key" and cont == "space":

                content = " "

                pyautogui.write(content)


            elif a_type == "key" and cont == "up_arw":

                pyautogui.press("up")

            elif a_type == "key" and cont == "down_arw":

                pyautogui.press("down")

            elif a_type == "key" and cont == "page_up":

                pyautogui.press("pgup")

            elif a_type == "key" and cont == "page_down":

                pyautogui.press("pgdn")

            elif a_type == "key" and cont == "enter":

                pyautogui.press("enter")

            elif a_type == "key" and cont == "file_list":


                self.file_lit_action()


            elif a_type == "key" and cont == "login_mail":

                db = sqlite3.connect("data/local.db")
                db.text_factory

                mail_count_from = int(self.ui.mail_count_from.text())

                data = db.execute(""" SELECT * FROM new_gmail  WHERE count_from >= '%s' LIMIT 1""" % (mail_count_from))

                for data1 in data:
                    lnk_mail = data1[0]
                    login_mail = lnk_mail

                pyautogui.write(login_mail)
                mail_count_from += 1


            elif a_type == "key" and cont == "login_pass":

                db = sqlite3.connect("data/local.db")
                db.text_factory

                # mail_count_from = int(self.ui.mail_count_from.text())

                data = db.execute(""" SELECT * FROM new_gmail  WHERE user_name = '%s' LIMIT 1""" % (login_mail))

                for data1 in data:
                    passd = data1[1]

                pyautogui.write(passd)



            elif a_type == "double_click":

                xpos = info[2]
                ypos = info[3]

                pyautogui.doubleClick(int(xpos), int(ypos))

            elif a_type == "copy" and cont == "gmail":

                pyautogui.hotkey('ctrl', 'c')
                x = pyperclip.paste()
                new_gmail = x + "@gmail.com"
                print(new_gmail)

            elif a_type == "delay":

                delay = int(info[6])

                time.sleep(delay)

            elif a_type == "key" and cont == "reco_mail":

                db = sqlite3.connect("data/local.db")
                db.text_factory

                data = db.execute(""" SELECT * FROM link_gmail  ORDER BY RANDOM() LIMIT 1""")

                for data1 in data:
                    lnk_mail = data1[0]

                pyautogui.write(lnk_mail)
                new_gmail_link = lnk_mail


            elif a_type == "key" and cont == "write_out":

                db = sqlite3.connect("data/local.db")
                cursor = db.cursor()
                new_mo = self.ui.link_poone.text()

                data_tup = (new_gmail, new_gmail_password, new_gmail_link, new_mo)

                sqlite_insert = """ INSERT INTO 'new_gmail'
                                                                 ('user_name', 'password', 'linked_email', 'link_phone') VALUES (?, ?, ?, ?)"""

                cursor.execute(sqlite_insert, data_tup)
                db.commit()
                self.update_new_mail_list()

    def link_mail_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.link_mail)
        self.update_link_list()

    def new_mail_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.new_gmail)
        self.update_new_mail_list()

    def usr_name_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.user_name)
        self.update_usr_name_list()

    def comment_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.comment_page)
        self.update_comment_list()

    def setting_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.setting)

    def file_auto_page(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.file_automate)

    def add_link_mail_single(self):

        db = sqlite3.connect("data/local.db")
        cursor = db.cursor()

        link_mail = self.ui.add_link_mail.text()

        data_tup = (link_mail,)

        sqlite_insert = """ INSERT INTO 'link_gmail'
                                                         ('gmail_link') VALUES (?)"""

        cursor.execute(sqlite_insert, data_tup)
        db.commit()
        self.update_link_list()

    def update_link_list(self):

        self.ui.link_mai_list.clear()
        db = sqlite3.connect("data/local.db")
        db.text_factory

        data = db.execute(""" SELECT * FROM link_gmail""")

        for info in data:
            self.ui.link_mai_list.addItem(info[0])

    def update_new_mail_list(self):

        self.ui.new_mail_list.clear()
        db = sqlite3.connect("data/local.db")
        db.text_factory
        cont = 0

        data = db.execute(""" SELECT * FROM new_gmail""")

        for info in data:
            cont += 1

            self.ui.new_mail_list.addItem(info[0])

        self.ui.gmail_count.setText(str(cont))

    def update_usr_name_list(self):

        self.ui.user_list.clear()
        db = sqlite3.connect("data/local.db")
        db.text_factory

        data = db.execute(""" SELECT * FROM user_name""")

        for info in data:
            fname = info[0]

            self.ui.user_list.addItem(fname)

    def add_user_name_single(self):

        db = sqlite3.connect("data/local.db")
        cursor = db.cursor()

        f_name = self.ui.f_name.text()
        l_name = self.ui.l_name.text()

        data_tup = (f_name, l_name,)

        sqlite_insert = """ INSERT INTO 'user_name'
                                                         ('f_name', 'l_name') VALUES (?, ?)"""

        cursor.execute(sqlite_insert, data_tup)
        db.commit()
        self.update_usr_name_list()

    def add_new_gmail(self):

        new_g = self.ui.gmail_edit.text()
        new_gp = self.ui.password_edit.text()
        new_gl = self.ui.link_mail_2.text()
        new_mo = self.ui.link_poone.text()

        db = sqlite3.connect("data/local.db")
        cursor = db.cursor()

        data_tup = (new_g, new_gp, new_gl, new_mo)

        sqlite_insert = """ INSERT INTO 'new_gmail'
                                                         ('user_name', 'password', 'linked_email', 'link_phone') VALUES (?, ?, ?, ?)"""

        cursor.execute(sqlite_insert, data_tup)
        db.commit()
        self.update_new_mail_list()

    def new_gmail_clicked(self):

        db = sqlite3.connect("data/local.db")
        db.text_factory

        word = str(self.ui.new_mail_list.currentItem().text())

        data = db.execute(""" SELECT * FROM new_gmail WHERE user_name='%s'""" % (word))

        for info in data:
            new_m = info[0]
            m_pas = info[1]
            m_link = info[2]
            m_link_m = info[3]

            self.ui.gmail_det.setText(new_m)
            self.ui.password_det.setText(m_pas)
            self.ui.link_mail_det.setText(m_link)
            self.ui.link_mobile_det.setText(m_link_m)

    def loop_run_start(self):

        cont = int(self.ui.times.text())

        for i in range(cont):
            self.start_actions()

    def delete_row(self):

        db = sqlite3.connect("data/local.db")
        cursor = db.cursor()

        word = str(self.ui.action_list.currentItem().text())

        delete_row = """ DELETE FROM action_list WHERE place = '%s'  """ % (word)

        cursor.execute(delete_row)
        db.commit()
        self.update_action_list()

    def update_comment_list(self):

        self.ui.comment_list.clear()
        db = sqlite3.connect("data/local.db")
        db.text_factory

        data = db.execute(""" SELECT * FROM comment""")

        for info in data:
            fname = info[0]

            self.ui.comment_list.addItem(fname)

    def add_comment(self):

        db = sqlite3.connect("data/local.db")
        cursor = db.cursor()

        cmnt = self.ui.inp_comment.text()

        data_tup = (cmnt,)

        sqlite_insert = """ INSERT INTO 'comment'
                                                           ('comnt') VALUES (?)"""

        cursor.execute(sqlite_insert, data_tup)
        db.commit()
        self.update_comment_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = login_ui()
    window.show()
    sys.exit(app.exec_())

