from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Investment Tracker")
        button = QPushButton("Press me")

        self.setCentralWidget(button)