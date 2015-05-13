import sys, os
from PySide import QtGui
from main_ui import Ui_MainWindow
from string import Template
import constants as c
from layout_template import LayoutTemplate

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.available_layout_elements = []
        self.init_ui()
        self.template = LayoutTemplate(self.ui)
        self.show()

    def init_ui(self):
        self.setWindowTitle(c.APPLICATION_NAME)
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
        if current_item is not None:
            self.ui.listWidgetSelected.addItem(current_item.text())

    def remove_selected_item(self):
        for item in self.ui.listWidgetSelected.selectedItems():
            self.ui.listWidgetSelected.takeItem(self.ui.listWidgetSelected.row(item))
        #Remove selection to prevent accidents with multiple clicks.
        for index in range(self.ui.listWidgetSelected.count()):
            self.ui.listWidgetSelected.item(index).setSelected(False)

    def save_html_file(self):
        # Assemble the content from the snippet file list from the selected elements.
        fileName = QtGui.QFileDialog.getSaveFileName(self, "Save HTML File", "", "HTML Files (*.htm *.html)")
        if fileName[0] is not None and fileName[0] is not u'':
            snippet_files = self._get_snippet_file_list()
            content = self._get_content_from_snippet_files(snippet_files)
            # Check if file exists and if so back it up to .bak
            if os.path.exists(fileName[0]):
                import shutil
                shutil.copyfile(fileName[0], fileName[0] + ".bak")
            file_save = open(fileName[0], 'w')
            file_save.write(content)
            
    def load_template(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Open Template File", self._get_documents_folder(), "Template Files (*%s)" % c.TEMPLATE_EXTENSION)
        if file_name[0] is not None and file_name[0] is not u'':
            self.current_file = file_name[0]
            self.template.load_template(file_name[0])
            self.change_title()
        
    def save_template(self):
        file_name = QtGui.QFileDialog.getSaveFileName(self, "Save Template File", self._get_documents_folder(), "Template Files (*%s)" % c.TEMPLATE_EXTENSION)
        if file_name[0] is not None and file_name[0] is not u'':
            self.current_file = file_name[0]
            self.template.save_template(file_name[0])
            self.change_title()
            
    def change_title(self):
        import ntpath
        file_display = ""
        if hasattr(self, 'current_file') and self.current_file:
            head, tail = ntpath.split(self.current_file)
            file_display = tail or ntpath.basename(head)
        self.setWindowTitle("%s - %s" % (c.APPLICATION_NAME, file_display))
            
# Private methods

    def _get_documents_folder(self):
        return os.path.join(os.path.expanduser('~'), 'Documents')
   
    def _get_snippet_file_list(self):
        snippet_file_list = []
        #always add a header snippet that will contain boilerplate for the header.
        snippet_file_list.append(os.path.join(c.RESOURCES_FOLDER, "header_snippet.txt"))
        for index in range(self.ui.listWidgetSelected.count()):
            element_name = self.ui.listWidgetSelected.item(index).text()
            index = self._find(self.available_layout_elements, c.AVAILABLE_LAYOUT_ITEM_NAME, element_name)
            snippet_name = self.available_layout_elements[index][c.AVAILABLE_LAYOUT_ITEM_SNIPPET_FILE]
            snippet_file_list.append(os.path.join(c.RESOURCES_FOLDER, snippet_name))
        #always add a footer snippet that will contain boilerplate for the footer.
        snippet_file_list.append(os.path.join(c.RESOURCES_FOLDER, "footer_snippet.txt"))
        return snippet_file_list
    
    def _get_content_from_snippet_files(self, snippet_files):
        content = ""
        for snippet_file in snippet_files:
            try:
                file_open = open(snippet_file, 'r')
                file_contents = file_open.read()
                # Map inputs to the content
                inputs = {}
                inputs[c.INPUT_TITLE] = self.ui.editTitle.text()
                inputs[c.INPUT_DESCRIPTION] = self.ui.editDescription.toPlainText()
                inputs[c.INPUT_KEYWORDS] = self.ui.editKeyWords.toPlainText()
                inputs[c.INPUT_PAGE_URL] = self.ui.editFullUrl.text()
                inputs[c.INPUT_YOUTUBE_IFRAME] =  self.ui.editYouTubeIframe.toPlainText()
                template_file_contents = Template(file_contents).substitute(inputs)
                content += template_file_contents + os.linesep
            except Exception as exc:
                self._show_message_box('Problem reading Snippet file: ' + str(exc).replace("\\\\", "\\"))
                return ""
        return content
        
    def _get_available_layout_elements(self):
        import json
        file_open = open(c.AVAILABLE_LAYOUT_ELEMENTS_FILE, 'r')
        file_contents = file_open.read()
        self.available_layout_elements  = json.loads(file_contents)
        for layout_element in self.available_layout_elements:
            self.ui.listWidgetAvailable.addItem(layout_element[c.AVAILABLE_LAYOUT_ITEM_NAME])
            
    def _find(self, lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return ValueError("Key not found")

    def _show_message_box(self, message):
        messageBox = QtGui.QMessageBox()
        messageBox.setText(message)
        messageBox.exec_()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()
    sys.exit()

if __name__ == '__main__':
    main()