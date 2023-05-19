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
        import socket

        HOST = '127.0.0.1'  # empty string represents localhost
        PORT = 22345  # choose a port number

        # create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind the socket to a specific address and port
        s.bind((HOST, PORT))
    
        # listen for incoming connections
        s.listen()
    
        print(f'Server is listening on port {PORT}')
    
        # wait for two clients to connect
        conn1, addr1 = s.accept()
     


class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Main FILE")
        self.chatUI = Ui_Widget()
        self.chatUI.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.chatUI.pushButton.clicked.connect(self.sendMessage)

    def sendMessage(self):
        import socket

        HOST = '127.0.0.1'  # replace with the server IP address if it's running on a different machine
        PORT = 22345  # same port number as the server

        # create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # connect to the server
            s.connect((HOST, PORT))
    
            # send and receive messages
            while True:
                message = self.chatUI.lineEdit.text()
                cmd = self.chatUI.plainTextEdit.toPlainText()
                c = self.chatUI.plainTextEdit
                b = self.chatUI.lineEdit
                if cmd == "":
                    c.appendPlainText(message)
                    b.clear()
                s.sendall(message.encode())
                data = s.recv(1024)
                print(f'Client 2: {data.decode()}')
        

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec())