# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Sat Jun 06 21:11:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 639)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/resources/ResponsiveLayoutCreatorIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelAvailableLayouts = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.labelAvailableLayouts.setFont(font)
        self.labelAvailableLayouts.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvailableLayouts.setObjectName("labelAvailableLayouts")
        self.gridLayout.addWidget(self.labelAvailableLayouts, 0, 0, 1, 1)
        self.labelSelectedLayouts = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.labelSelectedLayouts.setFont(font)
        self.labelSelectedLayouts.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSelectedLayouts.setObjectName("labelSelectedLayouts")
        self.gridLayout.addWidget(self.labelSelectedLayouts, 0, 2, 1, 1)
        self.listWidgetAvailable = QtGui.QListWidget(self.centralwidget)
        self.listWidgetAvailable.setMinimumSize(QtCore.QSize(200, 400))
        self.listWidgetAvailable.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidgetAvailable.setObjectName("listWidgetAvailable")
        self.gridLayout.addWidget(self.listWidgetAvailable, 1, 0, 1, 1)
        self.listWidgetSelected = QtGui.QListWidget(self.centralwidget)
        self.listWidgetSelected.setMinimumSize(QtCore.QSize(200, 400))
        self.listWidgetSelected.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidgetSelected.setObjectName("listWidgetSelected")
        self.gridLayout.addWidget(self.listWidgetSelected, 1, 2, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.buttonAdd = QtGui.QPushButton(self.centralwidget)
        self.buttonAdd.setObjectName("buttonAdd")
        self.verticalLayout_4.addWidget(self.buttonAdd)
        self.buttonRemoveSelected = QtGui.QPushButton(self.centralwidget)
        self.buttonRemoveSelected.setObjectName("buttonRemoveSelected")
        self.verticalLayout_4.addWidget(self.buttonRemoveSelected)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.buttonMoveUp = QtGui.QPushButton(self.centralwidget)
        self.buttonMoveUp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/resources/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonMoveUp.setIcon(icon1)
        self.buttonMoveUp.setIconSize(QtCore.QSize(24, 15))
        self.buttonMoveUp.setObjectName("buttonMoveUp")
        self.verticalLayout_4.addWidget(self.buttonMoveUp)
        self.buttonMoveDown = QtGui.QPushButton(self.centralwidget)
        self.buttonMoveDown.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/resources/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonMoveDown.setIcon(icon2)
        self.buttonMoveDown.setIconSize(QtCore.QSize(24, 15))
        self.buttonMoveDown.setObjectName("buttonMoveDown")
        self.verticalLayout_4.addWidget(self.buttonMoveDown)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.labelTitleAndMeta = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.labelTitleAndMeta.setFont(font)
        self.labelTitleAndMeta.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitleAndMeta.setObjectName("labelTitleAndMeta")
        self.gridLayout.addWidget(self.labelTitleAndMeta, 0, 3, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(10, -1, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.labelTitle = QtGui.QLabel(self.centralwidget)
        self.labelTitle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelTitle)
        self.editTitle = QtGui.QLineEdit(self.centralwidget)
        self.editTitle.setMinimumSize(QtCore.QSize(200, 0))
        self.editTitle.setObjectName("editTitle")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.editTitle)
        self.labelDescription = QtGui.QLabel(self.centralwidget)
        self.labelDescription.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDescription.setObjectName("labelDescription")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelDescription)
        self.editDescription = QtGui.QTextEdit(self.centralwidget)
        self.editDescription.setMaximumSize(QtCore.QSize(16777215, 150))
        self.editDescription.setAcceptRichText(False)
        self.editDescription.setObjectName("editDescription")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.editDescription)
        self.labelKeyWords = QtGui.QLabel(self.centralwidget)
        self.labelKeyWords.setObjectName("labelKeyWords")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelKeyWords)
        self.editKeyWords = QtGui.QTextEdit(self.centralwidget)
        self.editKeyWords.setMaximumSize(QtCore.QSize(16777215, 150))
        self.editKeyWords.setAcceptRichText(False)
        self.editKeyWords.setObjectName("editKeyWords")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.editKeyWords)
        self.labelFullPageUrl = QtGui.QLabel(self.centralwidget)
        self.labelFullPageUrl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFullPageUrl.setObjectName("labelFullPageUrl")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelFullPageUrl)
        self.labelFullUrl_2 = QtGui.QLabel(self.centralwidget)
        self.labelFullUrl_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFullUrl_2.setObjectName("labelFullUrl_2")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelFullUrl_2)
        self.editYouTubeIframe = QtGui.QTextEdit(self.centralwidget)
        self.editYouTubeIframe.setMaximumSize(QtCore.QSize(16777215, 125))
        self.editYouTubeIframe.setAcceptRichText(False)
        self.editYouTubeIframe.setObjectName("editYouTubeIframe")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.editYouTubeIframe)
        self.editFullUrl = QtGui.QTextEdit(self.centralwidget)
        self.editFullUrl.setMaximumSize(QtCore.QSize(16777215, 50))
        self.editFullUrl.setBaseSize(QtCore.QSize(0, 0))
        self.editFullUrl.setAcceptRichText(False)
        self.editFullUrl.setObjectName("editFullUrl")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.editFullUrl)
        self.gridLayout.addLayout(self.formLayout, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.buttonSaveHtmlFile = QtGui.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(168, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.buttonSaveHtmlFile.setPalette(palette)
        self.buttonSaveHtmlFile.setStyleSheet("background-color: rgb(168, 255, 155);")
        self.buttonSaveHtmlFile.setObjectName("buttonSaveHtmlFile")
        self.horizontalLayout.addWidget(self.buttonSaveHtmlFile)
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLayout_Template = QtGui.QMenu(self.menubar)
        self.menuLayout_Template.setObjectName("menuLayout_Template")
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
        self.menuFile.addAction(self.menuSaveHtmlFile)
        self.menuLayout_Template.addAction(self.menuLoadLayoutTemplate)
        self.menuLayout_Template.addAction(self.menuSaveLayoutTemplate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLayout_Template.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Responsive Layout Creator", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAvailableLayouts.setText(QtGui.QApplication.translate("MainWindow", "Available Layout Elements", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedLayouts.setText(QtGui.QApplication.translate("MainWindow", "Selected Layout Elements", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("MainWindow", "Add >>", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRemoveSelected.setText(QtGui.QApplication.translate("MainWindow", "<< Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTitleAndMeta.setText(QtGui.QApplication.translate("MainWindow", "Title and Meta Information", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTitle.setText(QtGui.QApplication.translate("MainWindow", "Title: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescription.setText(QtGui.QApplication.translate("MainWindow", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKeyWords.setText(QtGui.QApplication.translate("MainWindow", "Key Words:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFullPageUrl.setText(QtGui.QApplication.translate("MainWindow", "Full Page URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFullUrl_2.setText(QtGui.QApplication.translate("MainWindow", "YouTube iFrame:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSaveHtmlFile.setText(QtGui.QApplication.translate("MainWindow", "Save to HTML File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "HTML File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLayout_Template.setTitle(QtGui.QApplication.translate("MainWindow", "Layout Template", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLoadLayoutTemplate.setText(QtGui.QApplication.translate("MainWindow", "Load Layout Template", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSaveLayoutTemplate.setText(QtGui.QApplication.translate("MainWindow", "Save to Layout Template", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSaveHtmlFile.setText(QtGui.QApplication.translate("MainWindow", "Save to HTML File", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
