jQuery.extend({
   postJSON: function( url, data, callback) {
      return jQuery.post(url, data, callback, "json");
   }
});

var SandboxApi = function (server)
{
    if (server)
    {
        this.server = server;
    }
    else
    {
        this.server = "/api";
    }
};

SandboxApi.prototype.saveEditableBlock = function (contentId, content, callback)
{
    $.postJSON(this.server + "/saveEditableBlock", {"contentId":contentId, "content": content}, callback);
}

SandboxApi.prototype.getEditableBlock= function (contentId, callback)
{
    $.getJSON(this.server + "/getEditableContent", {"contentId":contentId}, callback);
}

var sandbox_api = new SandboxApi();
