from PyQt5.QtCore import (QRect, QSettings, QSize, Qt, QTextStream)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow, QTextEdit, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createStatusBar()

        msgBox = QMessageBox()
        msgBox.setMinimumWidth(500)
        msgBox.setText('Locating paired Sphero')
        msgBox.setInformativeText('searching for the nearest Sphero...')
        msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        # msgBox.adjustSize()
        msgBox.setSizePolicy()
        msgBox.exec_()

        self.setMinimumWidth(600)
        self.setMinimumHeight(400)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def about(self):
        QMessageBox.about(self, "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modern GUI applications using Qt, with a menu bar, "
                "toolbars, and a status bar.")


    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)

    def createActions(self):
        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

        self.aboutAct = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())