import json
from models import *
from django.core.exceptions import ObjectDoesNotExist

class SandboxApi:
    
    def _parseEditableContent(self, content):
        return content
    
    def saveEditableBlock(self, attr):
        rsp = None
        if "contentId" in attr.keys() and "content" in attr.keys():
            try:
                block = EditableBlock.objects.get(pk=attr['contentId'])
                block.content = self._parseEditableContent(attr["content"])
                block.save()
            except ObjectDoesNotExist:
                block = EditableBlock(id=attr['contentId'], content=self._parseEditableContent(attr["content"]))
                block.save()
                
            rsp = {"contentId": attr['contentId'], "content": self._parseEditableContent(attr["content"])}
        else:
            rsp = {"error": "Wrong arguments given: (%s) please send 'contentId' and 'content'."%attr}
            
        return json.dumps(rsp)
    
    def getEditableBlock(self, attr):
        rsp = None
        if "contentId" in attr.keys():
            try:
                block = EditableBlock.objects.get(pk=attr['contentId'])
                rsp = {"contentId": block.id, "content": block.content}
            except:
                rsp = {"error": "Object does not exist"}
        else:
            rsp = {"error": "Wrong arguments given: (%s) please send 'contentId'."%attr}
            
        return json.dumps(rsp)
        
        

    
    