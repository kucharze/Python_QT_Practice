from PySide6.QtWidgets import QWidget, QTabWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QApplication, QSizePolicy, QMessageBox, QMainWindow, QToolBar,QPushButton,QStatusBar,QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# def addPic():
#     print("Add pic")
#     Cardpic = QLabel("Hello There good sir how are you today?")
#     Cardpic.setPixmap(QPixmap('./2c.png'))
#     layout.addWidget(Cardpic)

app = QApplication()

window = QMainWindow()

wid = QWidget()
Mainlayout = QVBoxLayout()
wid.setLayout(Mainlayout)

comLayout = QHBoxLayout()
Cardpic = QLabel("Hello There good sir how are you today?")
playLayout = QHBoxLayout()
Cardpictwo = QLabel("Hello There good sir how are you today?")
comLayout.addWidget(Cardpic)
playLayout.addWidget(Cardpictwo)

Mainlayout.addLayout(comLayout)
Mainlayout.addLayout(playLayout)

window.setCentralWidget(wid)
window.show()

app.exec()