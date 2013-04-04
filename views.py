
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from sandbox.templates import *
from django.views.decorators.csrf import csrf_exempt
from api import SandboxApi
# Create your views here.

def home(request):
    template = HomeTemplate(MainPage(request, "David's Sandbox"))
    return HttpResponse(template.render())

def redirect_to_home(request):
    return HttpResponseRedirect("/")

@csrf_exempt
def api(request, func=None):
    """
    Calls an api function and returns the json result
    """
    sandbox_api = SandboxApi()
    if func is not None:
        return HttpResponse(getattr(sandbox_api, func)(request.REQUEST), mimetype="application/json")
    else:
        return HttpResponse("Please request a specific function instead")
    
