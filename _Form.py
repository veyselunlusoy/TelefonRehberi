import sys
from PyQt5.QtWidgets import *
from Form import Ui_MainWindow

class FormWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anaForm = Ui_MainWindow()
        self.anaForm.setupUi(self)
        self.adSoyad= self.anaForm.TxtAdiSoyadi
        self.telefon= self.anaForm.TxtTelefon
        self.eposta= self.anaForm.TextEposta
        self.liste= self.anaForm.TblListe

        self.anaForm.BtnKaydet.clicked.connect(self.kaydet)
        self.anaForm.BtnTemizle.clicked.connect(self.temizle)
        self.anaForm.BtnCikis.clicked.connect(self.cikis)


    def kaydet (self):
        print('kaydedildi')

    def temizle (self):
        self.adSoyad.clear()
        self.telefon.clear()
        self.eposta.clear()
        print('temizlendi')

    def cikis (self):
        sys.exit()
        print('Çıkıldı')
