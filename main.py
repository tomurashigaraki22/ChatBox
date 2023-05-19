# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)
from PySide6 import QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 600)
        Widget.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 30px;\n"
"background-color: black;")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 0, 401, 91))
        self.frame.setStyleSheet(u"background-color: blue;\n"
"border-top-left radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 251, 61))
        self.label.setStyleSheet(u"border: none;\n"
"border-top-left-radius: 0px;\n"
"font: italic 24pt \"Times New Roman\";\n"
"border-top-right-radius: 0px;\n"
"color: white;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 51, 51))
        self.label_2.setStyleSheet(u"border: none;")
        self.label_2.setPixmap(QPixmap(u"C:/Users/Tomura Shigaraki/Downloads/comment.png"))
        self.label_2.setScaledContents(True)
        self.plainTextEdit = QPlainTextEdit(Widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(213, 90, 181, 51))
        self.plainTextEdit.setStyleSheet(u"background-color: gray;\n"
"border-radius: 20px;")
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 560, 401, 41))
        self.lineEdit.setStyleSheet(u"background-color: gray;\n"
"border-radius: 20px;\n"
"padding-left: 38px;")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 565, 41, 31))
        self.pushButton.setStyleSheet(u"border-image: url(C:/Users/Tomura Shigaraki/Downloads/send-message.png);\n"
"border: none;\n"
"background-color: transparent;")
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 570, 31, 24))
        self.pushButton_2.setStyleSheet(u"background-color: transparent;\n"
"border-image: url(C:/Users/Tomura Shigaraki/Downloads/attachment.png);")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"ChatBox", None))
        self.label_2.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QWidget
    from PySide6.QtCore import Qt
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainGUIfile = QtWidgets.QWidget()
    ui = Ui_Widget()
    mainGUIfile.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    ui.setupUi(mainGUIfile)
    mainGUIfile.show()
    sys.exit(app.exec())