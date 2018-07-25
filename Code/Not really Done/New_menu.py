# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Nouveau_Menu(object):
    def setupUi(self, Nouveau_Menu):
        Nouveau_Menu.setObjectName("Nouveau_Menu")
        Nouveau_Menu.resize(693, 583)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../202d56b81c1417ce88b2c0e4a957e9be.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Nouveau_Menu.setWindowIcon(icon)
        Nouveau_Menu.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(255, 222, 57);\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Nouveau_Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.btnRetour = QtWidgets.QPushButton(self.centralwidget)
        self.btnRetour.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnRetour.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("H:/PROGRAMMATION/LANGUAGE PYTHON/Projet_dietetiq/Actions-blue-arrow-undo-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRetour.setIcon(icon1)
        self.btnRetour.setObjectName("btnRetour")
        self.btnSauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.btnSauvegarder.setGeometry(QtCore.QRect(120, 20, 75, 23))
        self.btnSauvegarder.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("H:/PROGRAMMATION/LANGUAGE PYTHON/Projet_dietetiq/icon_checkmark-69825e34cc01215e760dfbd28842923c.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSauvegarder.setIcon(icon2)
        self.btnSauvegarder.setObjectName("btnSauvegarder")
        self.vider = QtWidgets.QPushButton(self.centralwidget)
        self.vider.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.vider.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("H:/PROGRAMMATION/LANGUAGE PYTHON/Projet_dietetiq/7095.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vider.setIcon(icon3)
        self.vider.setObjectName("vider")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 110, 421, 431))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.btn_pd = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pd.setGeometry(QtCore.QRect(10, 90, 91, 23))
        self.btn_pd.setObjectName("btn_pd")
        self.btn_d = QtWidgets.QPushButton(self.centralwidget)
        self.btn_d.setGeometry(QtCore.QRect(90, 90, 81, 23))
        self.btn_d.setObjectName("btn_d")
        self.btn_din = QtWidgets.QPushButton(self.centralwidget)
        self.btn_din.setGeometry(QtCore.QRect(160, 90, 91, 23))
        self.btn_din.setObjectName("btn_din")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(510, 330, 161, 201))
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(510, 150, 161, 171))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 159, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(140, 0, 20, 171))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.nat_alim = QtWidgets.QComboBox(self.centralwidget)
        self.nat_alim.setGeometry(QtCore.QRect(510, 110, 161, 22))
        self.nat_alim.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nat_alim.setObjectName("nat_alim")
        self.nat_alim.addItem("")
        self.nat_alim.addItem("")
        self.nat_alim.addItem("")
        self.nat_alim.addItem("")
        Nouveau_Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Nouveau_Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 21))
        self.menubar.setObjectName("menubar")
        Nouveau_Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Nouveau_Menu)
        self.statusbar.setObjectName("statusbar")
        Nouveau_Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Nouveau_Menu)
        QtCore.QMetaObject.connectSlotsByName(Nouveau_Menu)

    def retranslateUi(self, Nouveau_Menu):
        _translate = QtCore.QCoreApplication.translate
        Nouveau_Menu.setWindowTitle(_translate("Nouveau_Menu", "Nouveau_Menu"))
        self.btn_pd.setText(_translate("Nouveau_Menu", "Petit dejeuner"))
        self.btn_d.setText(_translate("Nouveau_Menu", "Dejeuner"))
        self.btn_din.setText(_translate("Nouveau_Menu", "Diner"))
        self.label.setText(_translate("Nouveau_Menu", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">ELABORATION DU MENU</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Nouveau_Menu", "TOTAL"))
        self.nat_alim.setItemText(0, _translate("Nouveau_Menu", "Céreale"))
        self.nat_alim.setItemText(1, _translate("Nouveau_Menu", "Boisson gazeuse"))
        self.nat_alim.setItemText(2, _translate("Nouveau_Menu", "Boisson energetique"))
        self.nat_alim.setItemText(3, _translate("Nouveau_Menu", "Sauce"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Nouveau_Menu = QtWidgets.QMainWindow()
    ui = Ui_Nouveau_Menu()
    ui.setupUi(Nouveau_Menu)
    Nouveau_Menu.show()
    sys.exit(app.exec_())

