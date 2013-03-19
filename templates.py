"""
Widgetry templates for sandbox
"""

from davidjonas.widgetry.html_generator import Page, Template

class MainPage(Page):
    def __init__(self, request, title):
        super(MainPage, self).__init__(title, request=request)
        

class HomeTemplate(Template):
    def __init__(self, parent):
        super(HomeTemplate, self).__init__(parent)
        
        self.add("<h1>Hello sandbox</h1>")