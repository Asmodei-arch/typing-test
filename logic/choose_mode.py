from PyQt5.QtWidgets import QWidget

from ui_files.choose_mode_ui import Ui_Form


class ChooseMode(QWidget, Ui_Form):
    def __init__(self, event):
        super(ChooseMode, self).__init__()
        self.test_window = None
        self.event = event
        self.setupUi(self)
        self.boringMode.clicked.connect(self.activateBoringMode)
        self.oneErrorMode.clicked.connect(self.activateOneErrorMode)

    def activateBoringMode(self):
        self.event.setCurrentMode('boring')
        self.hide()

    def activateOneErrorMode(self):
        self.event.setCurrentMode('oneError')
        self.hide()
