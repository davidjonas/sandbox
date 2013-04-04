from davidjonas.widgetry.html_generator import Page, Template, Widget
from models import *
from django.core.exceptions import ObjectDoesNotExist

class EditableBlockWidget(Widget):
    DEFAULT_CONTENT_TEMPLATE = """
            <h1>Title</h1>
            <p>Body text</p>
    """
    
    def __init__(self, contentId=None):
        self.requireJSFile("/static/js/api.js");
        self.requireJSFile("/static/js/EditableBlock.js");
        
        content = self.getContent(contentId)
        
        html = """
        <div class="block editable" id="%(id)s">
            %(content)s    
        </div>
        """%{"id": contentId, "content": content}
        
        self.add(html)
        
    def getContent(self, contentId):
        try:
            content = EditableBlock.objects.get(pk=contentId).content
        except ObjectDoesNotExist:
            content = self.DEFAULT_CONTENT_TEMPLATE
            
        return content