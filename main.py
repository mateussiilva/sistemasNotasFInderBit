import sqlite3
import sys
from PySide6 import QtWidgets
# from model import cadastrar_dados
# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'CadastroCliente.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QStatusBar, QTableWidget, QTableWidgetItem, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1015, 772)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 60, 811, 231))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 49, 21))
        self.input_name_client = QLineEdit(self.frame)
        self.input_name_client.setObjectName(u"input_name_client")
        self.input_name_client.setGeometry(QRect(70, 10, 531, 26))
        self.input_adress_client = QLineEdit(self.frame)
        self.input_adress_client.setObjectName(u"input_adress_client")
        self.input_adress_client.setGeometry(QRect(90, 60, 521, 26))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 70, 18))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(620, 10, 31, 21))
        self.input_CPF_client = QLineEdit(self.frame)
        self.input_CPF_client.setObjectName(u"input_CPF_client")
        self.input_CPF_client.setGeometry(QRect(660, 10, 125, 26))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(620, 60, 32, 18))
        self.input_CEP_client = QLineEdit(self.frame)
        self.input_CEP_client.setObjectName(u"input_CEP_client")
        self.input_CEP_client.setGeometry(QRect(660, 60, 125, 26))
        self.label.raise_()
        self.input_name_client.raise_()
        self.input_adress_client.raise_()
        self.label_3.raise_()
        self.input_CPF_client.raise_()
        self.label_4.raise_()
        self.input_CEP_client.raise_()
        self.label_2.raise_()
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 40, 141, 18))
        self.btn_save_client = QPushButton(self.centralwidget)
        self.btn_save_client.setObjectName(u"btn_save_client")
        self.btn_save_client.setGeometry(QRect(870, 60, 121, 41))
        self.btn_save_client.setStyleSheet(
            u"background-color: rgb(38, 162, 105);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 310, 991, 431))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
# if QT_CONFIG(tooltip)
        self.frame.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Nome :", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Endere\u00e7o :", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"CPF:", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"CEP:", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Cadastro de Cliente", None))
        self.btn_save_client.setText(
            QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"Nome", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"CPF ", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"CEP", None))
    # retranslateUi


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.__btn_cadastro = self.btn_save_client.clicked.connect(
            self.save_client)

    def save_client(self):
        name = self.input_name_client.text()
        cpf = self.input_CPF_client.text()
        cep = self.input_CEP_client.text()
        adress = self.input_adress_client.text()
        data = (name, cpf, cep, adress)
        if len(name) > 0 and len(cpf) > 0 and \
                len(cep) > 0 and len(name) > 0:
            cadastrar_dados(data)
        else:
            print("Insira dados validas")
        


NAME_DATABASE = "dev_base.db"
conn = sqlite3.connect(NAME_DATABASE)
cursor = conn.cursor()


def close_connect():
    conn.commit()
    cursor.close()
    conn.commit()


def init_base():
    try:
        cursor.execute("""CREATE TABLE clientes(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name varchar(255), 
                        cpf varchar(255),
                        cep varchar(255),
                        adress varchar(255));""")
    except:
        pass
    close_connect()


def cadastrar_dados(data):
    cursor.execute("""
                   insert into clientes (name,cpf,cep,adress)
                   values(?,?,?,?)
                   """, data)
    close_connect()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
