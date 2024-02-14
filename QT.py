from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QApplication, QSizePolicy, QMessageBox, QMainWindow, QToolBar,QPushButton,QStatusBar,QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

app = QApplication()

def hello():
    print("hello")

#Create the main window
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
line_edit.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)

button = QPushButton("Hello there good sir")
button.clicked.connect(hello)
button.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)

otherButton = QPushButton("Hello there Other person")
otherButton.clicked.connect(hello)
otherButton.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)

#The main display
wid = QWidget()

layout = QVBoxLayout()
layout.addWidget(button,3)
layout.addWidget(otherButton,1)
wid.setLayout(layout)

label = QLabel("Hello There good sir how are you today?")
# label.setPixmap(QPixmap('./minions.png'))

layouttwo = QHBoxLayout()
layouttwo.addWidget(label)
layouttwo.addWidget(line_edit)
# layouttwo.addWidget(otherButton)

#Grid code copied from code along
button_1 = QPushButton("One")
button_2 = QPushButton("Two")
button_3 = QPushButton("Three")
button_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
button_4 = QPushButton("Four")
button_5 = QPushButton("Five")
button_6 = QPushButton("Six")
button_7 = QPushButton("Seven")
button_8 = QPushButton("Eight")
button_9 = QPushButton("Nine")
button_9.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
button_10 = QPushButton("Ten")

grid = QGridLayout()
grid.addWidget(button_1,0,0)
grid.addWidget(button_2,0,1,1,2) #Take up 1 row and 2 columns
grid.addWidget(button_3,1,0,2,1) #Take up 2 rows and 1 column
grid.addWidget(button_4,1,1)
grid.addWidget(button_5,1,2)
grid.addWidget(button_6,2,1)
grid.addWidget(button_7,2,2)
grid.addWidget(button_8,0,3,3,1)
grid.addWidget(button_9,3,2,1,3)
grid.addWidget(button_10,0,2,1,1)

layout.addLayout(layouttwo)
layout.addLayout(grid)

window.setCentralWidget(wid)
window.show()

app.exec()