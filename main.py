import sys
from PySide import QtGui, QtCore
from main_ui import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.show()

    def init_ui(self):
        pass
        

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()
    sys.exit()

if __name__ == '__main__':
    main()