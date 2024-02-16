from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys

class XOBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(XOBrowser, self).__init__(*args, **kwargs)
        self.setStyleSheet("background-color: #36393f; color: #ffffff;")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.status.setStyleSheet("background-color: #202225; color: #ffffff;")
        self.setStatusBar(self.status)
        navtb = QToolBar("Navigation")
        navtb.setStyleSheet("background-color: #202225; color: #ffffff;")
        self.addToolBar(navtb)
        back_btn = QAction("<-", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)
        next_btn = QAction("->", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)
        reload_btn = QAction("↻", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
        home_btn = QAction("⌂", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        navtb.addSeparator()
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setStyleSheet("background-color: #202225; color: #ffffff;")
        navtb.addWidget(self.urlbar)
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
        self.show()
        
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - xo browser [the unhackable browser]" % title)
        
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.duckduckgo.com"))
        
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)
        
    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
        
app = QApplication(sys.argv)
app.setApplicationName("xo Browser - the unhackable browser")
window = XOBrowser()
app.exec_()
