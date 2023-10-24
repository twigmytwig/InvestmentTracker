from PySide6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QToolBar, QStatusBar
from PySide6.QtCore import QSize, QPointF
from PySide6.QtGui import QAction, QPainter
from PySide6.QtCharts import QChart, QChartView, QLineSeries

from investmentData import InvestmentData

class Chart():
    def __init__(self, data):
        super().__init__()
        self.series = QLineSeries()
        for x in data.dollarValues:
            for y in data.weeks:
                self.series.append(int(y),float(x))
                data.weeks.pop(0)
                break

        self.chart = QChart()
        self.chart.legend().show()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")
        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)
        
    def file_reader(path):
        file = open(path ,"r")
        lines = file.readlines()

        investmentData = InvestmentData()
        count = 0
        for line in lines:
            if(count == 0):
                count += 1
                investmentData.dollarValues = line.strip('\\n\n').split(", ")
            else:
                investmentData.weeks = line.strip('\\n\n').split(", ")
        return investmentData