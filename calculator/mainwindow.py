# This Python file uses the following encoding: utf-8
import sys
import os

# from modules import *

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

ERROR_MSG = "ERROR"


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # global widgets
        # widgets = self.ui

        self.display = self.ui.lineEdit

    def setDisplayText(self, text):
        """
        设置显示文本
        :param text:
        :return:
        """
        self.display.setText(text)
        self.display.setFocus()

        # Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # App Title
        title = "Modern - Calculator"
        # Apply App Title
        self.setWindowTitle(title)

        # Removes Title Bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # RESIZE EVENTS
    # def resizeEvent(self, event):
    #     # Update Size Grips
    #     UIFunctions.resize_grips(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("images/icons/logo.png"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

