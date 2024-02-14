from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QApplication, QMessageBox, QMainWindow,QToolBar,QPushButton,QStatusBar
from PySide6.QtCore import Qt

app = QApplication()

def hello():
    print("hello")

#Create the display
window = QMainWindow()
file = window.menuBar().addMenu("File")
file.addAction("Assist")

View = window.menuBar().addMenu("View")
View.addAction("Assist")

help = window.menuBar().addMenu("Help")
help.addAction("Do")
help.addAction("You")
help.addAction("Need")
help.addAction("Assistance")

window.setWindowTitle("QT Practice")

line_edit = QLineEdit("Enter name here")

button = QPushButton("Hello there good sir")
button.clicked.connect(hello)

otherButton = QPushButton("Hello there Other person")
otherButton.clicked.connect(hello)

#The main display
wid = QWidget()

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(otherButton)
layout.addWidget(line_edit)
wid.setLayout(layout)

window.setCentralWidget(wid)
window.show()

app.exec()