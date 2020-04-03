'''
    QtNotePad

    Simple notepad using python and QtGui wrapper.

    Author: Anwesh Dahal
    Version: 2020.April
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QFont
import sys

class QtNotePad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # self refers to QMainWindow

        self.te_main = QTextEdit(self)
        self.setWindowTitle("QtNotePad")
        self.setGeometry(100,100,500,500)
        self.setMinimumSize(200, 200)
        self.buildUi()


    def buildUi(self):
        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        new_menu = QAction('New', self)
        new_menu.setShortcut('Ctrl+N')
        new_menu.triggered.connect(self.clear_window)
        file_menu.addAction(new_menu)

        save_menu = QAction('Save', self)
        save_menu.setShortcut('Ctrl+S')
        save_menu.triggered.connect(self.save)
        file_menu.addAction(save_menu)

        edit_menu = menu_bar.addMenu("Edit")
        comment_menu = QAction('Comment', self)
        comment_menu.setShortcut('Ctrl+/')
        comment_menu.triggered.connect(self.comment)

        theme_menu = QAction('Theme', self)
        edit_menu.addAction(comment_menu)

        default_style = "font: 12pt 'Hack'; color: #dddddd; background-color: #111111;"
        self.te_main.setStyleSheet(default_style)

        # Setting a vertical box layout
        vertical_box = QVBoxLayout() # instantiating the QVBoxLayout
        vertical_box.addWidget(self.te_main) # adding the text editor to layout
        vertical_box.setStretchFactor(self.te_main, 1) # setting the stretch factor
        vertical_box.setContentsMargins(0, 0, 0, 0) # setting the margins

        centralWidget = QWidget() # widget to hold the text editor
        centralWidget.setLayout(vertical_box)
        self.setCentralWidget(centralWidget)

    def clear_window(self):
        self.te_main.setPlainText("")
    def comment(self):
        self.te_main.insertHtml("# ")
    def save(self):
        save_file = QFileDialog.getSaveFileName(self, 'Save',)
        text_to_save = self.te_main.toPlainText()
        print(save_file[0])
        try:
            f = open(save_file[0], "w+")
            f.write(text_to_save)
            f.close()
        except Exception:
            print(Exception)
        self.post_save(save_file[0])
    def post_save(self, filename):
        window_title = "QtNotePad - " + filename
        self.setWindowTitle(window_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main_window = QtNotePad()
    main_window.show()
    sys.exit(app.exec_())

