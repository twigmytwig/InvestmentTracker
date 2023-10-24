import sys
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app)

window.show()
path = "C:\\Users\\Trevor\\Dropbox\\My PC (DESKTOP-7CBII96)\\Documents\\Test\\test.txt"
f = open(path ,"r")
print(f.read())
app.exec()