'''
Created on May 9, 2015

@author: James Culbertson
'''

import os

APPLICATION_NAME = "Responsive Layout Creator"

RESOURCES_FOLDER = "resources"

AVAILABLE_LAYOUT_ELEMENTS_FILE = os.path.join(RESOURCES_FOLDER,"available_layouts.json")
AVAILABLE_LAYOUT_ITEM_NAME = "name"
AVAILABLE_LAYOUT_ITEM_SNIPPET_FILE = "snippetFile"

TEMPLATE_EXTENSION = ".tpl"

#Inputs
INPUT_TITLE = "title"
INPUT_KEYWORDS = "keywords"
INPUT_DESCRIPTION = "description"
INPUT_PAGE_URL = "pageUrl"
INPUT_YOUTUBE_IFRAME = "youTubeIframe"

#Config
CONFIG_USER = "User"
CONFIG_USER_LAST_TEMPLATE_FILE = "LastTemplateFile"
CONFIG_USER_LAST_SAVE_FOLDER = "LastSaveFolder"