## Atalhos para o desenvolvimento


venv/lib/python3.11/site-packages/PySide6/designer
.venv/bin/pyside6-uic uis/main.ui -o MainWindow.py 



# Ler o arquivo python gerador pela ui_file
````
import sys
from PySide6 import QtWidgets

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
````