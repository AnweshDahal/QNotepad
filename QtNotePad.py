"""
    Peppercorn Notepad

    Simple notepad using python and QtGui wrapper.

    Author: Peppercorn
    Version: 2020.April

"""

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QAction, QFileDialog
from PyQt5.QtWidgets import QMessageBox, QFontDialog
from PyQt5.QtGui import QIcon, QFont
import sys


class QtNotePad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # self refers to QMainWindow
        self.filename = None
        self.file_open = False
        self.te_main = QTextEdit(self)
        self.setWindowTitle("Peppercorn Notepad")
        self.setGeometry(100, 100, 800, 500)
        self.setMinimumSize(200, 200)
        self.build_ui()

    def build_ui(self):
        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        new_menu = QAction('New', self)
        new_menu.setShortcut('Ctrl+N')
        new_menu.triggered.connect(self.new)
        file_menu.addAction(new_menu)

        open_menu = QAction('Open', self)
        open_menu.setShortcut('Ctrl+O')
        open_menu.triggered.connect(self.open)
        file_menu.addAction(open_menu)


        save_menu = QAction('Save', self)
        save_menu.setShortcut('Ctrl+S')
        save_menu.triggered.connect(self.save)
        file_menu.addAction(save_menu)

        edit_menu = menu_bar.addMenu("Edit")

        comment_menu = QAction('Comment', self)
        comment_menu.setShortcut('Ctrl+/')
        comment_menu.triggered.connect(self.comment)
        edit_menu.addAction(comment_menu)

        copy_menu = QAction('Copy', self)
        copy_menu.setShortcut('Ctrl+C')
        copy_menu.triggered.connect(self.copy)
        edit_menu.addAction(copy_menu)

        cut_menu = QAction('Cut', self)
        cut_menu.setShortcut('Ctrl+X')
        cut_menu.triggered.connect(self.cut)
        edit_menu.addAction(cut_menu)

        paste_menu = QAction('Paste', self)
        paste_menu.setShortcut('Ctrl+V')
        paste_menu.triggered.connect(self.paste)
        edit_menu.addAction(paste_menu)

        preference_menu = edit_menu.addMenu('Preferences')

        font_menu = QAction('Font', self)
        font_menu.triggered.connect(self.set_font)
        preference_menu.addAction(font_menu)

        about_menu = menu_bar.addMenu("Help")
        help_menu = QAction("About", self)
        help_menu.setShortcut('F7')
        help_menu.triggered.connect(self.about_app)
        about_menu.addAction(help_menu)

        # Setting a vertical box layout
        vertical_box = QVBoxLayout()  # instantiating the QVBoxLayout
        vertical_box.addWidget(self.te_main)  # adding the text editor to layout
        vertical_box.setStretchFactor(self.te_main, 1)  # setting the stretch factor
        vertical_box.setContentsMargins(0, 0, 0, 0)  # setting the margins

        central_widget = QWidget()  # widget to hold the text editor
        central_widget.setLayout(vertical_box)
        self.setCentralWidget(central_widget)

    def copy(self):
        self.te_main.copy()
        copyright()
        credits()

    def cut(self):
        self.te_main.cut()

    def set_font(self):
        font, valid = QFontDialog().getFont()
        if valid:
            self.te_main.setFont(QFont(font))


    def paste(self):
        self.te_main.paste()

    def new(self):
        self.filename = None
        self.file_open = False
        self.te_main.clear()

    def open(self):
        self.te_main.setPlainText("")
        open_file = QFileDialog.getOpenFileName(self, 'Open')
        self.file_open = True
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
        <h3>Peppercorn Notepad by Peppercorn build 2020.APR</h3>
        <b>Project</b>: Peppercorn Notepad<br>
        <b>Build</b>: 2020.APR<br>
        <b>Author</b>: Peppercorn<br>
            <b>Team</b>: Anwesh Dahal<br>
        <b>Github</b>: <a href="https://github.com/AnweshDahal/QtNotepad.git">https://github.com/AnweshDahal/QtNotepad.git</a>
        """
        QMessageBox.about(self, "About", message)

    def comment(self):
        self.te_main.insertHtml("# ")

    def save(self):
        save_file = None
        if not self.file_open:
            save_file = QFileDialog.getSaveFileName(self, 'Save')
            self.filename = save_file[0]
            self.file_open = True
        text_to_save = self.te_main.toPlainText()

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
