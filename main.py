from PyQt5.QtWidgets import QApplication
from  _Form import FormWindow

uygulama = QApplication([])
pencere = FormWindow()
pencere.show()
uygulama.exec_()

# exe ye çevirmek için konsola aşağıdaki kod yazılacak
# pyinstaller --windowed --onefile --onedir --clean --noconsole --add-data "rehber.db:." -w main.py