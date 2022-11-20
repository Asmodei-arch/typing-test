import sys

from PyQt5.QtWidgets import QApplication
import qt_material

from logic.start_menu import StartMenu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_material.apply_stylesheet(app, theme='dark_teal.xml')
    ex = StartMenu()
    ex.show()
    sys.exit(app.exec())
