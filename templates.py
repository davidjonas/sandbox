"""
Widgetry templates for sandbox
"""
from davidjonas.widgetry.html_generator import Page, Template
from davidjonas.sandbox.widgets import *

class MainPage(Page):
    def __init__(self, request, title):
        super(MainPage, self).__init__(title, request=request)
        
        self.addHeadDirective('<link rel="shortcut icon" href="/static/favicon.ico?v=1" />')
        self.addCSSFile('/static/css/base.css')
        self.addCSSFile('/static/css/blocks.css')
        self.addCSSFile('http://fonts.googleapis.com/css?family=Merriweather:700|Open+Sans+Condensed:300')
        self.addJSFile('/static/js/jquery-1.9.1.min.js')
        

class HomeTemplate(Template):
    def __init__(self, parent):
        super(HomeTemplate, self).__init__(parent)
        
        self.addWidget(EditableBlockWidget(contentId = "hello_world"))
        self.addWidget(EditableBlockWidget(contentId = "test_content"))