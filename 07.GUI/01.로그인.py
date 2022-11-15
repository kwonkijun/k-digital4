from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

# 디자인 파일 경로
UI_PATH = "07.GUI/login.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)

QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())