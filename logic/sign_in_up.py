import hashlib

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from logic.base import Base
from logic.event import Event
from ui_files.sign_in_up_ui import Ui_Form


def isLoginUsed(login):
    query = f'''
    SELECT name from Users 
    WHERE name = ?
    '''
    args = login,
    cursor = Base()

    try:
        cursor.executeAndFetch(query, args)[0][0]
    except IndexError:
        return False
    return True


def insertUser(login, password):
    query = '''
    INSERT into Users Values(?, ?)
    '''
    args = login, password

    cursor = Base()
    cursor.executeAndCommit(query, args)


class SignInUp(QWidget, Ui_Form):
    def __init__(self, mode='up', event=None):
        super(SignInUp, self).__init__()
        self.setupUi(self)
        if event is None:
            event = Event()
        self.event = event

        self.setWindowModality(Qt.WindowModal)

        self.canAddToBase = False

        self.currentAction = 'Войти' if mode == 'in' else 'Зарегестрироваться'
        self.loginInput.textChanged.connect(self.checkLogin)

        self.signButton.setText(self.currentAction)
        self.signButton.clicked.connect(self.sign)

    def checkLogin(self):
        should_be_used = True if self.currentAction == 'Войти' else False

        if isLoginUsed(self.loginInput.text()) != should_be_used:
            error_message = 'Пользователя не существует' if self.currentAction == 'Войти' \
                else 'Пользователь уже существует'
            self.errorField.setText(error_message)
            self.canAddToBase = False
            return

        self.errorField.setText('')
        self.canAddToBase = True

    def sign(self):
        if not self.canAddToBase:
            return

        if self.currentAction == 'Войти':
            self.signIn()
            return

        self.signUp()

    def signIn(self):
        if not is_passwords_equal(self.loginInput.text(), self.passwordInput.text()):
            self.errorField.setText('Пароль неверный')
            return
        self.event.setUsername(self.loginInput.text())
        self.hide()

    def signUp(self):
        password = self.passwordInput.text().encode('utf-8')
        password = hashlib.md5(password).hexdigest()
        insertUser(self.loginInput.text(), password)
        self.event.setUsername(self.loginInput.text())
        self.hide()


def is_passwords_equal(login, curr_password):
    user_password_hash = getPasswordFromUserWithLogin(login)
    curr_password = curr_password.encode('utf-8')

    if user_password_hash != hashlib.md5(curr_password).hexdigest():
        return False
    return True


def getPasswordFromUserWithLogin(login):
    query = '''
    SELECT password from Users
    WHERE name = ?   
    '''
    args = login,
    cursor = Base()

    return cursor.executeAndFetch(query, args)[0][0]
