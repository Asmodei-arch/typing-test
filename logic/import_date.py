from PyQt5.QtWidgets import QWidget, QFileDialog

from logic.base import Base
from ui_files.import_data_ui import Ui_Form
from pathlib import Path
from PyQt5.QtCore import Qt
import csv


class ImportData(QWidget, Ui_Form):
    def __init__(self, username):
        super(ImportData, self).__init__()
        self.file = None
        self.setupUi(self)
        self.chooseFileButton.clicked.connect(self.chooseFile)
        self.importButton.clicked.connect(self.importData)
        self.setWindowModality(Qt.WindowModal)

        self.userName = username

    def chooseFile(self):
        start_directory = f'{Path.home()}'
        file_formats = 'csv (*.csv)'

        self.file = QFileDialog.getOpenFileName(self, 'Сохранить файл', start_directory,
                                                file_formats)[0]

    def importData(self):
        data = self.getDataFromFile()

        self.saveDataToDB(data)

    def saveDataToDB(self, data):
        cursor = Base()
        query = '''
        INSERT INTO Events
        VALUES (NULL, ?, ?, ?, ?, ?, ?) 
        '''

        for i in data:
            args = self.userName, *i
            cursor.executeAndCommit(query, args)

    def getDataFromFile(self):
        data = []
        with open(self.file) as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                data.append(row)

        return data
