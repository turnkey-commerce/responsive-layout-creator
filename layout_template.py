'''
Created on May 12, 2015

@author: James
'''

import json

class LayoutTemplate:
    '''
    Manages the loading and saving templates from the Layout Creator.
    '''
    def __init__(self, mainWindow):
        self.template = []
        self.ui = mainWindow
        
    def load_template(self, fileName):
        '''Load the template from JSON into the template list.'''
        file_open = open(fileName, 'r')
        file_contents = file_open.read()
        self.template = json.loads(file_contents)
        self._set_ui_from_template()

    def save_template(self, fileName):
        '''Save the template as a JSON string.'''
        self._get_template_from_ui()
        file_save = open(fileName, 'w')
        file_save.write(json.dumps(self.template))
        
    def _get_template_from_ui(self):
        '''Get the template as an ordered list of elements from the currently selected list in UI.'''
        self.template = []
        for index in range(self.ui.listWidgetSelected.count()):
            self.template.append(self.ui.listWidgetSelected.item(index).text())
            
    def _set_ui_from_template(self):
        '''Sets the currently selected list in the UI from the template.'''
        self.ui.listWidgetSelected.clear()
        for template_element in self.template:
            self.ui.listWidgetSelected.addItem(template_element)
            