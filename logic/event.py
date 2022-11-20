class Event:
    def __init__(self, username='anon', current_mode=None, text_name=None):
        self.username = username
        self.currentMode = current_mode
        self.textName = text_name

    def setUsername(self, username):
        self.username = username

    def setCurrentMode(self, mode):
        self.currentMode = mode

    def setTextName(self, text):
        self.textName = text
