# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Sat May 09 13:58:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 749)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.listViewSelected = QtGui.QListView(self.centralwidget)
        self.listViewSelected.setMinimumSize(QtCore.QSize(250, 500))
        self.listViewSelected.setObjectName("listViewSelected")
        self.gridLayout.addWidget(self.listViewSelected, 2, 2, 1, 1)
        self.listViewAvailable = QtGui.QListView(self.centralwidget)
        self.listViewAvailable.setMinimumSize(QtCore.QSize(250, 500))
        self.listViewAvailable.setObjectName("listViewAvailable")
        self.gridLayout.addWidget(self.listViewAvailable, 2, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.ButtonMoveUp = QtGui.QPushButton(self.centralwidget)
        self.ButtonMoveUp.setObjectName("ButtonMoveUp")
        self.verticalLayout_3.addWidget(self.ButtonMoveUp)
        self.ButtonMoveDown = QtGui.QPushButton(self.centralwidget)
        self.ButtonMoveDown.setObjectName("ButtonMoveDown")
        self.verticalLayout_3.addWidget(self.ButtonMoveDown)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 3, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.ButtonRemove = QtGui.QPushButton(self.centralwidget)
        self.ButtonRemove.setObjectName("ButtonRemove")
        self.horizontalLayout_4.addWidget(self.ButtonRemove)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ButtonAdd = QtGui.QPushButton(self.centralwidget)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.verticalLayout_4.addWidget(self.ButtonAdd)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 1, 1, 1)
        self.LabelAvailableLayouts = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.LabelAvailableLayouts.setFont(font)
        self.LabelAvailableLayouts.setObjectName("LabelAvailableLayouts")
        self.gridLayout.addWidget(self.LabelAvailableLayouts, 1, 0, 1, 1)
        self.LabelSelectedLayouts = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.LabelSelectedLayouts.setFont(font)
        self.LabelSelectedLayouts.setObjectName("LabelSelectedLayouts")
        self.gridLayout.addWidget(self.LabelSelectedLayouts, 1, 2, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuLoadLayoutTemplate = QtGui.QAction(MainWindow)
        self.menuLoadLayoutTemplate.setObjectName("menuLoadLayoutTemplate")
        self.menuSaveLayoutTemplate = QtGui.QAction(MainWindow)
        self.menuSaveLayoutTemplate.setObjectName("menuSaveLayoutTemplate")
        self.menuSaveHtmlFile = QtGui.QAction(MainWindow)
        self.menuSaveHtmlFile.setObjectName("menuSaveHtmlFile")
        self.menuFile.addAction(self.menuLoadLayoutTemplate)
        self.menuFile.addAction(self.menuSaveLayoutTemplate)
        self.menuFile.addAction(self.menuSaveHtmlFile)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Responsive Layout Creator", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonMoveUp.setText(QtGui.QApplication.translate("MainWindow", "Move Up", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonMoveDown.setText(QtGui.QApplication.translate("MainWindow", "Move Down", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonRemove.setText(QtGui.QApplication.translate("MainWindow", "Remove Selected Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonAdd.setText(QtGui.QApplication.translate("MainWindow", "Add >>", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelAvailableLayouts.setText(QtGui.QApplication.translate("MainWindow", "Available Layout Elements", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelSelectedLayouts.setText(QtGui.QApplication.translate("MainWindow", "Selected Layout Elements", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Save to HTML File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLoadLayoutTemplate.setText(QtGui.QApplication.translate("MainWindow", "Load Layout Template", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSaveLayoutTemplate.setText(QtGui.QApplication.translate("MainWindow", "Save to Layout Template", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSaveHtmlFile.setText(QtGui.QApplication.translate("MainWindow", "Save to HTML File", None, QtGui.QApplication.UnicodeUTF8))

