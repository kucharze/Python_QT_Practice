from PySide6.QtWidgets import QWidget, QTabWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QApplication, QSizePolicy, QMessageBox, QMainWindow, QToolBar,QPushButton,QStatusBar,QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

playerhand = []
comhand = []

def addPic():
    print("Add pic")
    Cardpic = QLabel("")
    Cardpic.setPixmap(QPixmap('./2c.png'))
    playLayout.addWidget(Cardpic)
    abutton = QPushButton("Play card")
    abutton.clicked.connect(addPic)
    playButtonLayout.addWidget(abutton)


def displayPlayerHand():
    print("Player")
    for card in playerhand:
        print(card)
        Cardpic = QLabel("")
        Cardpic.setPixmap(QPixmap('./2c.png'))
        playLayout.addWidget(Cardpic)
        abutton = QPushButton("Play card")
        abutton.clicked.connect(addPic)
        playButtonLayout.addWidget(abutton)

def displayComHand():
    print("com")
    for card in comhand:
        print(card)
        Cardpic = QLabel("")
        Cardpic.setPixmap(QPixmap('./2c.png'))
        comLayout.addWidget(Cardpic)


app = QApplication()

window = QMainWindow()

wid = QWidget()
Mainlayout = QVBoxLayout()
wid.setLayout(Mainlayout)

comLayout = QHBoxLayout()
Cardpic = QLabel("Computer")
comLayout.addWidget(Cardpic)

playLayout = QHBoxLayout()
button = QPushButton("Add card")
button.clicked.connect(addPic)
Cardpictwo = QLabel("Player")

# playLayout.addWidget(Cardpictwo)
# playLayout.addWidget(button)
playButtonLayout = QHBoxLayout()
# playButtonLayout.addWidget(button)


Mainlayout.addLayout(comLayout)
Mainlayout.addWidget(Cardpictwo)
Mainlayout.addLayout(playLayout)
Mainlayout.addLayout(playButtonLayout)
Mainlayout.addWidget(button)

window.setCentralWidget(wid)
window.show()

app.exec()