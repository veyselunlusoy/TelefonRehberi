import sys ,os , sqlite3
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
        self.anaForm.BtnListele.clicked.connect(self.Listele)
        self.anaForm.BtnCikis.clicked.connect(self.cikis)

    def baglan(self):
        sqlFile= os.path.join(os.path.dirname(__file__), "rehber.db")
        with sqlite3.connect(sqlFile)as baglanti:
            return baglanti

    def kaydet (self):
        try:
            from random import randint
            kayıtNo=str(randint(1111, 9999))
            baglanti=self.baglan()
            sorgu=baglanti.cursor()
            sorgu.execute(f"insert into RehberTBL values('{kayıtNo}','{self.adSoyad.text()}','{self.telefon.text()}','{self.eposta.text()}')")
        #   imput teksatırsa text(), çoksatırlı alan okunacaksa toPlainText(), spinlerde value(), combo boxlarda currentText()
            baglanti.commit()
            self.temiz()
            self.adSoyad.setFocus()
            QMessageBox.information(self, 'Bildirim','Kayıt Başarılı')

        except Exception as hata:
            QMessageBox.critical(self, 'Hata', 'Hata Oluştu:\n' + hata)

        print('kaydedildixx')

    def Listele (self):
        try:
            self.liste.clear()
            sutunlar= ['No', 'Ad Soyad','Telefon','E-Posta']
            self.liste.setColumnCount(len(sutunlar))
            self.liste.setHorizontalHeaderLabels(sutunlar)
            baglanti = self.baglan()
            sorgu = baglanti.cursor()
            sorgu.execute("SELECT * FROM RehberTBL")
            kayitlar = sorgu.fetchall()
            if kayitlar:
                self.liste.setRowCount(len(kayitlar))
                kayitSay = 0
                for kayit in kayitlar:
                    for i in range(len(sutunlar)):
                        self.liste.setItem(kayitSay, i, QTableWidgetItem(str(kayit[i])))
                    kayitSay+=1
            else:
                QMessageBox.warning(self, "Uyarı", "Kayıt Bulunamadı")

        except Exception as hata:
            QMessageBox.critical(self, 'Hata', 'Hata Oluştu:\n' + hata)



    def cikis (self):
        sys.exit()
        print('Çıkıldı')

    def temiz (self):
        self.adSoyad.clear()
        self.telefon.clear()
        self.eposta.clear()
