from datetime import datetime
from math import ceil
from random import choice
from string import punctuation

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import constants
from logic.base import Base
from logic.event import Event
from logic.statistics import Statistics
from ui_files.test_ui import Ui_Form


class Test(QWidget, Ui_Form):
    def __init__(self, event=None, text_options: dict = None):
        super(Test, self).__init__()
        self.setupUi(self)

        if event is None:
            event = Event()
            event.setCurrentMode('boring')
        self.event = event

        self.text_options = text_options
        if self.text_options is None:
            self.text_options = {}

        self.mode = event.currentMode

        self.startTest()
        self.closeEvent = self.endTest

    def startTest(self):
        self.currentIndex = 0
        self.writtenTextEndIndex = 0
        self.errorCnt = 0
        self.previousErrorIndex = -1

        self.currentColor = constants.GREEN

        self.text = getText()
        self.event.setTextName(self.text)
        self.updateText()

    def keyPressEvent(self, key: QtGui.QKeyEvent):
        if not key.text().isalnum() and key.text() not in {' ', *punctuation}:
            return
        if self.currentIndex == 0:
            self.startTime = datetime.now()

        if key.text() != self.text[self.currentIndex]:
            self.error()
        else:
            self.currentIndex += 1
            self.currentColor = constants.GREEN

        if self.currentIndex == len(self.text):
            self.endTest()
            return

        self.updateText()
        self.updateCounters()

        self.progressBar.setValue(ceil((self.currentIndex * 100 / len(self.text))))

    def updateText(self):
        written_text = self.text[:self.currentIndex]
        curr_symbol = change_background_on_index(self.text, self.currentIndex, self.currentColor)
        left_text = change_text_color(self.text[self.currentIndex + 1:], "grey")

        formatted = f'{written_text}' \
                    f'{curr_symbol}' \
                    f'{left_text}'

        self.textField.setText(formatted)

    def updateCounters(self):
        self.speed.setValue(self.currentIndex / (
                (datetime.now() - self.startTime).total_seconds() / 60))

    def error(self):
        if self.previousErrorIndex == self.currentIndex:
            return
        if self.mode == 'oneError':
            self.endTest()
            return

        self.errorCnt += 1
        self.previousErrorIndex = self.currentIndex
        self.currentColor = constants.RED

        if self.currentIndex == 0:
            self.accuracy.setValue(0)
            return
        self.accuracy.setValue(100 - (self.errorCnt / self.currentIndex) * 100)

    def endTest(self, *args):
        self.statistic = Statistics((datetime.now() - self.startTime).total_seconds(),
                                    self.errorCnt, self.currentIndex, self.event)
        self.statistic.show()
        self.hide()


def change_background_on_index(text: str, index: int, color: str):
    return f'<span style="background-color:{color}">{text[index]}</span>'


def change_text_color(text: str, color: str):
    return f'<span style="color:{color}">{text}</span>'


def getNameOfTextWithParameters(text_parameter):
    query = f'''SELECT name from Texts
WHERE length BETWEEN ? AND ?
AND language in {str(text_parameter['language'])}
'''
    args = (text_parameter['min_len'], text_parameter['max_len'])

    cursor = Base()
    res = cursor.executeAndFetch(query, args)
    text_name = choice(res)[0]
    return text_name


def getText(text_parameter: dict = None):
    if text_parameter is None:
        text_parameter = {}
    text_parameter = {
        key: (text_parameter[key] if key in text_parameter
              else constants.DEFAULT_TEXT_OPTIONS[key])
        for key in constants.DEFAULT_TEXT_OPTIONS.keys()}

    text_name = getNameOfTextWithParameters(text_parameter)

    with open(f'texts/{text_name}') as f:
        text = f.read().strip()

    return text
