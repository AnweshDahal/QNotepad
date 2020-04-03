"""
    Peppercorn Notepad

    Simple notepad using python and QtGui wrapper.

    Author: Peppercorn
    Version: 2020.April

"""

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QAction, QFileDialog
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
import sys


class QtNotePad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # self refers to QMainWindow
        self.filename = None
        self.te_main = QTextEdit(self)
        self.setWindowTitle("Peppercorn Notepad")
        self.setGeometry(100, 100, 500, 500)
        self.setMinimumSize(200, 200)
        self.build_ui()

    def build_ui(self):
        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        new_menu = QAction('New', self)
        new_menu.setShortcut('Ctrl+N')
        new_menu.triggered.connect(self.new)

        open_menu = QAction('Open', self)
        open_menu.setShortcut('Ctrl+O')
        open_menu.triggered.connect(self.open)
        file_menu.addAction(open_menu)
        file_menu.addAction(new_menu)

        save_menu = QAction('Save', self)
        save_menu.setShortcut('Ctrl+S')
        save_menu.triggered.connect(self.save)
        file_menu.addAction(save_menu)

        edit_menu = menu_bar.addMenu("Edit")
        comment_menu = QAction('Comment', self)
        comment_menu.setShortcut('Ctrl+/')
        comment_menu.triggered.connect(self.comment)
        edit_menu.addAction(comment_menu)

        about_menu = menu_bar.addMenu("Help")
        help_menu = QAction("About", self)
        help_menu.setShortcut('F7')
        help_menu.triggered.connect(self.about_app)
        about_menu.addAction(help_menu)

        default_style = "font: 12pt 'Hack'; color: #111111;"
        self.te_main.setStyleSheet(default_style)

        # Setting a vertical box layout
        vertical_box = QVBoxLayout()  # instantiating the QVBoxLayout
        vertical_box.addWidget(self.te_main)  # adding the text editor to layout
        vertical_box.setStretchFactor(self.te_main, 1)  # setting the stretch factor
        vertical_box.setContentsMargins(0, 0, 0, 0)  # setting the margins

        central_widget = QWidget()  # widget to hold the text editor
        central_widget.setLayout(vertical_box)
        self.setCentralWidget(central_widget)

    def new(self):
        self.filename = None
        self.te_main.setPlainText("")

    def open(self):
        self.te_main.setPlainText("")
        open_file = QFileDialog.getOpenFileName(self, 'Open')
        self.filename = open_file[0]
        try:
            o = open(self.filename, "r")
            content = o.read()
            self.te_main.setPlainText(content)
            o.close()
        except IOError:
            print()
        self.post_save()

    def about_app(self):
        message = """
        Peppercorn Notepad by Peppercorn build 2020.APR
        Powered by Python 3 and PyQt5
        \tgithub repository:
        https://github.com/AnweshDahal/QtNotepad.git
        """
        QMessageBox.about(self, "About", message)


    def comment(self):
        self.te_main.insertHtml("# ")

    def save(self):
        save_file = QFileDialog.getSaveFileName(self, 'Save')
        text_to_save = self.te_main.toPlainText()
        self.filename = save_file[0]
        try:
            f = open(self.filename, "w+")
            f.write(text_to_save)
            f.close()
        except IOError:
            pass
        self.post_save()

    def post_save(self):
        window_title = "QtNotePad - " + self.filename
        self.setWindowTitle(window_title)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main_window = QtNotePad()
    main_window.setWindowIcon(QIcon("logo.png"))
    main_window.show()
    sys.exit(app.exec_())
