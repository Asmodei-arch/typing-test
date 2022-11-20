from PyQt5.QtWidgets import QMainWindow

from logic.choose_mode import ChooseMode
from logic.event import Event
from logic.export_data import ExportData
from logic.import_date import ImportData
from logic.sign_in_up import SignInUp
from logic.test import Test
from ui_files.start_ui import Ui_MainWindow


class StartMenu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.importWindow = None
        self.exportWindow = None
        self.testModeWindow = None
        self.test_window = None
        self.setupUi(self)

        self.chooseModeWindow = None
        self.signWindow = None

        self.anonButton.clicked.connect(self.anonTest)
        self.signInButton.clicked.connect(self.signIn)
        self.signUpButton.clicked.connect(self.signUp)

        self.importButton.setVisible(False)
        self.exportButton.setVisible(False)

        self.importButton.clicked.connect(self.importUserData)
        self.exportButton.clicked.connect(self.exportUserData)

        self.event = Event()

    def anonTest(self):
        self.chooseMode()

    def importUserData(self):
        self.importWindow = ImportData(self.event.username)
        self.importWindow.show()

    def exportUserData(self):
        self.exportWindow = ExportData(self.event.username)
        self.exportWindow.show()

    def sign(self, mode):
        self.signWindow = SignInUp(mode, event=self.event)
        self.signWindow.show()
        self.signWindow.hideEvent = self.afterSign

    def afterSign(self, _):
        if self.event.username == 'anon':
            return

        self.signInButton.setText('Войти под другим логином')
        self.signUpButton.setText('Зарегестрировать новый аккаунт')
        self.anonButton.setText('Продолжить')
        self.exportButton.setVisible(True)
        self.importButton.setVisible(True)

    def signIn(self):
        self.sign('in')

    def signUp(self):
        self.sign('up')

    def chooseMode(self):
        self.chooseModeWindow = ChooseMode(self.event)
        self.chooseModeWindow.show()
        self.chooseModeWindow.hideEvent = self.openTestWindow

    def openTestWindow(self, _):
        self.hide()
        self.testModeWindow = Test(self.event)
        self.testModeWindow.show()
        self.testModeWindow.hideEvent = self.openAfterTestEnd

    def openAfterTestEnd(self, _):
        self.show()
