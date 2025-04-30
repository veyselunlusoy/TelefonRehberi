from PyQt5.QtWidgets import QApplication # type: ignore
from  _Form import FormWindow

uygulama = QApplication([])
pencere = FormWindow()
pencere.show()
uygulama.exec_()