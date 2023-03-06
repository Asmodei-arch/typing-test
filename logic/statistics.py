from datetime import datetime
from time import strptime, mktime

import pyqtgraph
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

import constants
from logic.base import Base
from logic.event import Event
from ui_files.statistics_ui import Ui_Form


class Statistics(QWidget, Ui_Form):
    def __init__(self, seconds_elapsed, error_cnt, symbol_typed, event=None):
        super(Statistics, self).__init__()
        self.graph = None
        self.setupUi(self)

        self.setWindowModality(Qt.WindowModal)

        self.error_cnt = error_cnt
        self.secondsElapsed = seconds_elapsed
        self.errorCnt = error_cnt

        if symbol_typed == 0:
            symbol_typed = 1
            self.error_cnt = 1
            self.secondsElapsed = 1
        self.symbolTyped = symbol_typed

        if event is None:
            event = Event()
        self.event = event

        self.printStatistics()
        self.insertEventToBase()

        if event.username != 'anon':
            self.showPlot()

    def printStatistics(self):
        self.speedField.setValue(self.symbolTyped * 60 / self.secondsElapsed)
        self.accuracyField.setValue(1 - self.errorCnt / self.symbolTyped)
        self.errorCntField.setValue(self.errorCnt)
        self.symbolTypedField.setValue(self.symbolTyped)

    def insertEventToBase(self):
        cursor = Base(constants.DATA_BASE_NAME)
        query = '''
        INSERT into Events Values(NULL, ?, ?, ?, ?, ?, ?) 
        '''
        args = (
            self.event.username, self.event.textName, datetime.now(),
            1 - self.errorCnt / self.symbolTyped, self.symbolTyped, self.secondsElapsed)
        cursor.executeAndCommit(query, args)

    def getUserEvents(self):
        query = '''
        SELECT datetime, secondsElapsed, symbolTyped from Events
        WHERE user=?
        ORDER BY datetime
        '''
        args = self.event.username,
        cursor = Base()
        events = cursor.executeAndFetch(query, args)
        events.sort(key=lambda x: x[0])

        return events

    def showPlot(self):
        plotting_data = self.getUserEvents()
        speeds = list(map(lambda x: x[2] / x[1], plotting_data))
        dates = list(map(lambda x: x[0], plotting_data))
        self.graph = pyqtgraph.PlotWidget()

        for index, date in enumerate(dates):
            dates[index] = int(mktime(strptime(date, '%Y-%m-%d %H:%M:%S.%f')))

        axis = pyqtgraph.DateAxisItem(orientation='bottom')
        line = pyqtgraph.PlotCurveItem(clear=True, pen="g")
        self.graph.addItem(line)
        self.graph.setAxisItems({"bottom": axis})

        self.graph.plot(dates, speeds)
        self.graph.show()
