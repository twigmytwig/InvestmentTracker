from PySide6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QToolBar, QStatusBar
from PySide6.QtCore import QSize, QPointF
from PySide6.QtGui import QAction, QPainter
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from graph import Chart

from investmentData import InvestmentData

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Investment Tracker")
        self.app = app

        #Menubar and menu
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        file_open = file_menu.addAction("Open file...")
        file_open.triggered.connect(self.open_file)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        #toolbar
        toolbar = QToolBar("Main Tool Bar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        toolbar.addSeparator()

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        #status bar
        self.setStatusBar(QStatusBar(self))

        path = "C:\\Users\\Trevor\\Dropbox\\My PC (DESKTOP-7CBII96)\\Documents\\Test\\test.txt"
        investmentData = InvestmentData()
        investmentData = Chart.file_reader(path)

        chartData = Chart(investmentData)
        self.setCentralWidget(chartData._chart_view)

    def quit_app(self):
        self.app.quit()

    #Open file explorer
    def open_file(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec():
            fileNames = dialog.selectedFiles()
    
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message!", 3000)