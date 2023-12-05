from PyQt5.QtWidgets import QWidget, QApplication, \
    QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(1500,1000)
    w.setWindowTitle("2023 JBNU CapstoneDesign UPRIGHT")
    # w.selfWindowIcon(QIcon('파일경로'))
    w.show()
    sys.exit(app.exec_())