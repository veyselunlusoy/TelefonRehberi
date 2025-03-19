from PyQt5.QtWidgets import QApplication
from  _Form import FormWindow

uygulama = QApplication([])
pencere = FormWindow()
pencere.show()
uygulama.exec_()