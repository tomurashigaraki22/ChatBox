import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QApplication
from PySide6 import QtGui
from PySide6.QtCore import QThread
from PySide6.QtCore import Qt
import subprocess

from main import Ui_Widget

class chatting(QThread):
    def __init__(self):
        super(chatting, self).__init__()
        subprocess.run("python", "server.py")
        subprocess.run("python", "client_me.py")
        


class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Main FILE")
        self.chatUI = Ui_Widget()
        self.chatUI.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.chatUI.pushButton.clicked.connect(self.sendMessage)

    def sendMessage(self):
        pass
        

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec())