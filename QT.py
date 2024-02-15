from PySide6.QtWidgets import QWidget, QTabWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QApplication, QSizePolicy, QMessageBox, QMainWindow, QToolBar,QPushButton,QStatusBar,QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

app = QApplication()

window = QMainWindow()

def hello():
    print("hello")

def addPic():
    print("Add pic")
    Cardpic = QLabel("Hello There good sir how are you today?")
    Cardpic.setPixmap(QPixmap('./2c.png'))
    layout.addWidget(Cardpic)

#Create the main window

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
grid.addWidget(button_8,0,4,3,1)
grid.addWidget(button_9,3,2,1,3)
grid.addWidget(button_10,3,0,1,1)

#Tab widget copied code
        # tab_widget = QTabWidget(self)

        # #Information
        # widget_form = QWidget()
        # label_full_name = QLabel("Full name :")
        # line_edit_full_name = QLineEdit()
        # form_layout = QHBoxLayout()
        # form_layout.addWidget(label_full_name)
        # form_layout.addWidget(line_edit_full_name)
        # widget_form.setLayout(form_layout)

        # #Buttons
        # widget_buttons = QWidget()
        # button_1 = QPushButton("One")
        # button_1.clicked.connect(self.button_1_clicked)
        # button_2 = QPushButton("Two")
        # button_3 = QPushButton("Three")
        # buttons_layout = QVBoxLayout()
        # buttons_layout.addWidget(button_1)
        # buttons_layout.addWidget(button_2)
        # buttons_layout.addWidget(button_3)
        # widget_buttons.setLayout(buttons_layout)


        # #Add tabs to widget
        # tab_widget.addTab(widget_form,"Information")
        # tab_widget.addTab(widget_buttons,"Button")


        # layout = QVBoxLayout()
        # layout.addWidget(tab_widget)

        # self.setLayout(layout)

layout.addLayout(layouttwo)
layout.addLayout(grid)

picbut = QPushButton("Add a card pic")
picbut.clicked.connect(addPic)
layout.addWidget(picbut)


window.setCentralWidget(wid)
window.show()

app.exec()