import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton
from PyQt6.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.url_bar = QTextEdit(self)

        self.go_btn = QPushButton(self)

        self.eng1 = QPushButton(self)
        self.eng2 = QPushButton(self)
        self.eng3 = QPushButton(self)

        self.browser = QWebEngineView(self)

        self.init()

        self.setWindowTitle("Undefined Browser")
        self.setGeometry(0, 0, 1400, 1000)

    def init(self):
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setFixedWidth(1090)
        self.url_bar.move(0, 0)

        self.go_btn.setText("Go !")
        self.go_btn.setMaximumHeight(30)
        self.go_btn.move(1090, 0)
        self.go_btn.clicked.connect(lambda: self.get_url(self.url_bar.toPlainText()))

        self.browser.setUrl(QUrl('https://google.com'))
        self.browser.move(0, 30)
        self.browser.setFixedWidth(1200)
        self.browser.setFixedHeight(900)
        self.browser.iconUrl()
        self.search_engines()

    def search_engines(self):
        urls = ['https://google.com', 'https://searx.thegpm.org/', 'https://www.startpage.com/']

        self.eng1.setText("Google")
        self.eng2.setText("Searx")
        self.eng3.setText("StartPage")

        self.eng1.move(1200, 30)
        self.eng1.setFixedHeight(100)
        self.eng1.setFixedWidth(100)

        self.eng2.move(1200, 130)
        self.eng2.setFixedHeight(100)
        self.eng2.setFixedWidth(100)

        self.eng3.move(1200, 230)
        self.eng3.setFixedHeight(100)
        self.eng3.setFixedWidth(100)

        self.eng1.clicked.connect(lambda: self.browser.setUrl(QUrl(urls[0])))
        self.eng2.clicked.connect(lambda: self.browser.setUrl(QUrl(urls[1])))
        self.eng3.clicked.connect(lambda: self.browser.setUrl(QUrl(urls[2])))

    def get_url(self, url: str):
        self.browser.setUrl(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
