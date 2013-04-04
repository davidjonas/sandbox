var LiveContent = {};

LiveContent.currentElement = null;
LiveContent.currentElementContent = null;
LiveContent.currentElementCache = null;

LiveContent.init = function ()
{
    $('.editable').click(LiveContent.activateEvent);
}

LiveContent.activateEvent = function (evt)
{
    if (LiveContent.currentElement == evt.target)
    {
        return true;
    }
    
    if (LiveContent.currentElement != null)
    {
        LiveContent.save();
    }
    
    LiveContent.currentElement = $(evt.target);
    LiveContent.currentElementContent = $(evt.target).html();
    LiveContent.currentElementCache = $(evt.target).html();
    LiveContent.activate(evt.target);
    
    return true;
}

LiveContent.activate = function (element)
{
    var save = $('<img id="saveButton" contenteditable="false" src="/static/images/check.png"/>').click(LiveContent.save);
    var clear = $('<img id="clearButton" contenteditable="false" src="/static/images/cancel.png" />').click(LiveContent.clear);
    $(element).attr("contenteditable", "true");
    $(element).parent().append(save);
    $(element).parent().append(clear);
    LiveContent.startRecording();
}

LiveContent.deactivate = function (element)
{
    LiveContent.init();
    $(element).attr("contenteditable", "false");
    LiveContent.currentElement = null;
    LiveContent.currentElementContent = null;
    LiveContent.currentElementCache = null;

    $(element).parent().find("#saveButton").remove();
    $(element).parent().find("#clearButton").remove();
    
    LiveContent.stopRecording();
}

LiveContent.startRecording = function ()
{
    $(document).bind("keyup", LiveContent.cache);
}

LiveContent.stopRecording = function ()
{
    $(document).unbind("keyup");
}

LiveContent.cache = function ()
{
    LiveContent.currentElementCache = $(LiveContent.currentElement).html();
}

LiveContent.changed = function ()
{
    return LiveContent.currentElementContent != LiveContent.currentElementCache;
}

LiveContent.save = function ()
{
    if (LiveContent.changed())
    {
        var block = $(LiveContent.currentElement);
        LiveContent.currentElementContent = LiveContent.currentElementCache;
        LiveContent.deactivate(LiveContent.currentElement);
        
        sandbox_api.saveEditableBlock($(block).attr("id"), $(block).html(), function (data) {
            if (data["error"])
            {
                console.log(data["error"]);
            }
            else{
                $(block).html(data['content']);
            }
        });
    }
    else
    {
        console.log("No changes. Not saving");
        LiveContent.deactivate(LiveContent.currentElement);
    }
};

LiveContent.clear = function ()
{
    $(LiveContent.currentElement).html(LiveContent.currentElementContent);
    LiveContent.init();
    LiveContent.deactivate(LiveContent.currentElement);
};

$(function ()
{
    LiveContent.init();    
});