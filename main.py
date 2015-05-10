import sys
from PySide import QtGui
from main_ui import Ui_MainWindow
import constants as c

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.show()

    def init_ui(self):
        #Menu Events
        self.ui.menuLoadLayoutTemplate.activated.connect(self.menuLoadLayoutTemplate_activated)
        self.ui.menuSaveLayoutTemplate.activated.connect(self.menuSaveLayoutTemplate_activated)
        self.ui.menuSaveHtmlFile.activated.connect(self.menuSaveHtmlFile_activated)
        #Button Events
        self.ui.buttonAdd.clicked.connect(self.buttonAdd_clicked)
        self.ui.buttonMoveDown.clicked.connect(self.buttonMoveDown_clicked)
        self.ui.buttonMoveUp.clicked.connect(self.buttonMoveUp_clicked)
        self.ui.buttonRemoveSelected.clicked.connect(self.buttonRemoveSelected_clicked)
        self.ui.buttonSaveHtmlFile.clicked.connect(self.buttonSaveHtmlFile_clicked)
        #Selection Events
        self.ui.listWidgetAvailable.doubleClicked.connect(self.buttonAdd_clicked)
        #Get the initial Available List Items
        self._get_available_layout_elements()
  
    def menuLoadLayoutTemplate_activated(self):
        self.load_template()
        
    def menuSaveLayoutTemplate_activated(self):
        self.save_template()
        
    def menuSaveHtmlFile_activated(self):
        self.save_html_file()
        
    def buttonAdd_clicked(self):
        self.add_selected_item()
        
    def buttonMoveDown_clicked(self):
        self.move_selected_item_down()
    
    def buttonMoveUp_clicked(self):
        self.move_selected_item_up()
        
    def buttonRemoveSelected_clicked(self):
        self.remove_selected_item()
        
    def buttonSaveHtmlFile_clicked(self):
        self.save_html_file()
        
    def move_selected_item_up(self):
        current_index = None
        for item in self.ui.listWidgetSelected.selectedItems():
            current_index = self.ui.listWidgetSelected.row(item)
        if current_index is not None and current_index != 0:
            current_item = self.ui.listWidgetSelected.takeItem(current_index)
            self.ui.listWidgetSelected.insertItem(current_index - 1, current_item)
            self.ui.listWidgetSelected.setCurrentRow(current_index - 1)
        elif current_index:
            self.ui.listWidgetSelected.setCurrentRow(current_index)
        
    def move_selected_item_down(self):
        current_index = None
        for item in self.ui.listWidgetSelected.selectedItems():
            current_index = self.ui.listWidgetSelected.row(item)
        if current_index is not None and current_index != self.ui.listWidgetSelected.count() - 1:
            current_item = self.ui.listWidgetSelected.takeItem(current_index)
            self.ui.listWidgetSelected.insertItem(current_index + 1, current_item)
            self.ui.listWidgetSelected.setCurrentRow(current_index + 1)
        elif current_index:
            self.ui.listWidgetSelected.setCurrentRow(current_index)
        
    def add_selected_item(self):
        current_item = self.ui.listWidgetAvailable.currentItem()
        self.ui.listWidgetSelected.addItem(current_item.text())
            
    def remove_selected_item(self):
        for item in self.ui.listWidgetSelected.selectedItems():
            self.ui.listWidgetSelected.takeItem(self.ui.listWidgetSelected.row(item))
        #Remove selection to prevent accidents with multiple clicks.
        for index in range(self.ui.listWidgetSelected.count()):
            self.ui.listWidgetSelected.item(index).setSelected(False)
        
    def _get_available_layout_elements(self):
        import json
        file_open = open(c.AVAILABLE_LAYOUT_ELEMENTS_FILE, 'r')
        file_contents = file_open.read()
        layout_elements  = json.loads(file_contents)
        for layout_element in layout_elements:
            self.ui.listWidgetAvailable.addItem(layout_element)
                   

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()
    sys.exit()

if __name__ == '__main__':
    main()