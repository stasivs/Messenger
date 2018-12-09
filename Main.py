import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())