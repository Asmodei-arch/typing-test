from PyQt5.QtWidgets import QWidget, QFileDialog

from logic.base import Base
from ui_files.export_data_ui import Ui_Form
from pathlib import Path
from PyQt5.QtCore import Qt
import csv


class ExportData(QWidget, Ui_Form):
    def __init__(self, username):
        super(ExportData, self).__init__()
        self.file = None
        self.setupUi(self)
        self.chooseFileButton.clicked.connect(self.chooseFile)
        self.exportButton.clicked.connect(self.export)
        self.setWindowModality(Qt.WindowModal)

        self.userName = username

    def chooseFile(self):
        start_directory = f'{Path.home()}'
        file_formats = 'csv (*.csv)'

        self.file = QFileDialog.getSaveFileName(self, 'Сохранить файл', start_directory,
                                                file_formats)[0]

    def export(self):
        if self.file is None:
            self.errorField.setText('Выберите имя для файла сохранения')
            return

        user_data = self.getUserData()
        self.writeUserDataToCsv(user_data)
        self.errorField.setText('Данные успешно сохранены')

    def writeUserDataToCsv(self, data):
        with open(f'{self.file}.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)

            for row in data:
                writer.writerow(row)

    def getUserData(self):
        cursor = Base()
        query = '''
        SELECT text, datetime, accuracy, symbolTyped, secondsElapsed from Events
        WHERE user=?
        ORDER BY datetime
        '''
        args = self.userName,

        data = cursor.executeAndFetch(query, args)

        return data
