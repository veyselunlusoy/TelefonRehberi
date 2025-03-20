# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 80, 25))
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 80, 25))
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 80, 25))
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.TxtTelefon = QtWidgets.QLineEdit(self.centralwidget)
        self.TxtTelefon.setGeometry(QtCore.QRect(110, 80, 300, 25))
        self.TxtTelefon.setObjectName("TxtTelefon")
        self.TextEposta = QtWidgets.QLineEdit(self.centralwidget)
        self.TextEposta.setGeometry(QtCore.QRect(110, 110, 300, 25))
        self.TextEposta.setObjectName("TextEposta")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.TblListe = QtWidgets.QTableWidget(self.centralwidget)
        self.TblListe.setGeometry(QtCore.QRect(20, 230, 401, 192))
        self.TblListe.setObjectName("TblListe")
        self.TblListe.setColumnCount(0)
        self.TblListe.setRowCount(0)
        self.BtnKaydet = QtWidgets.QPushButton(self.centralwidget)
        self.BtnKaydet.setGeometry(QtCore.QRect(30, 450, 80, 27))
        self.BtnKaydet.setObjectName("BtnKaydet")
        self.BtnListele = QtWidgets.QPushButton(self.centralwidget)
        self.BtnListele.setGeometry(QtCore.QRect(180, 450, 80, 27))
        self.BtnListele.setObjectName("BtnListele")
        self.BtnCikis = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCikis.setGeometry(QtCore.QRect(330, 450, 80, 27))
        self.BtnCikis.setObjectName("BtnCikis")
        self.TxtAdiSoyadi = QtWidgets.QLineEdit(self.centralwidget)
        self.TxtAdiSoyadi.setGeometry(QtCore.QRect(110, 50, 300, 25))
        self.TxtAdiSoyadi.setObjectName("TxtAdiSoyadi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 24))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuKapat = QtWidgets.QMenu(self.menuDosya)
        self.menuKapat.setObjectName("menuKapat")
        self.menuD_zen = QtWidgets.QMenu(self.menubar)
        self.menuD_zen.setObjectName("menuD_zen")
        self.menuG_r_n_m = QtWidgets.QMenu(self.menubar)
        self.menuG_r_n_m.setObjectName("menuG_r_n_m")
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setMinimumSize(450,540)
        MainWindow.setMaximumSize(450, 540)

#        self.statusbar = QtWidgets.QStatusBar(MainWindow)
#       self.statusbar.setObjectName("statusbar")
#       MainWindow.setStatusBar(self.statusbar)
        self.actionYeni = QtWidgets.QAction(MainWindow)
        self.actionYeni.setObjectName("actionYeni")
        self.actionSil = QtWidgets.QAction(MainWindow)
        self.actionSil.setObjectName("actionSil")
        self.actionHepsini_Kapat = QtWidgets.QAction(MainWindow)
        self.actionHepsini_Kapat.setObjectName("actionHepsini_Kapat")
        self.actionGe_erli_Sayfay_Kapat = QtWidgets.QAction(MainWindow)
        self.actionGe_erli_Sayfay_Kapat.setObjectName("actionGe_erli_Sayfay_Kapat")
        self.menuKapat.addAction(self.actionGe_erli_Sayfay_Kapat)
        self.menuKapat.addAction(self.actionHepsini_Kapat)
        self.menuDosya.addAction(self.actionYeni)
        self.menuDosya.addAction(self.actionSil)
        self.menuDosya.addAction(self.menuKapat.menuAction())
        self.menuDosya.addSeparator()
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuD_zen.menuAction())
        self.menubar.addAction(self.menuG_r_n_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TELEFON REHBERİ"))
        self.label.setText(_translate("MainWindow", "YENİ KAYIT"))
        self.label_2.setText(_translate("MainWindow", "Adı Soyadı"))
        self.label_3.setText(_translate("MainWindow", "Telefon"))
        self.label_4.setText(_translate("MainWindow", "E-Posta"))
        self.label_5.setText(_translate("MainWindow", "KAYIT LİSTESİ"))
        self.BtnKaydet.setText(_translate("MainWindow", "KAYDET"))
        self.BtnListele.setText(_translate("MainWindow", "LİSTELE"))
        self.BtnCikis.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuKapat.setTitle(_translate("MainWindow", "Kapat"))
        self.menuD_zen.setTitle(_translate("MainWindow", "Düzen"))
        self.menuG_r_n_m.setTitle(_translate("MainWindow", "Görünüm"))
        self.actionYeni.setText(_translate("MainWindow", "Yeni"))
        self.actionSil.setText(_translate("MainWindow", "Sil"))
        self.actionHepsini_Kapat.setText(_translate("MainWindow", "Hepsini Kapat"))
        self.actionGe_erli_Sayfay_Kapat.setText(_translate("MainWindow", "Geçerli Sayfayı Kapat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
