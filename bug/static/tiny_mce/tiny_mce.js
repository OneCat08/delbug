//editorId是富文本的id
function SetTinyMceContent(editorId, content) {
    //给富文本编辑器设置内容
    tinyMCE.getInstanceById(editorId).getBody().innerHTML = content;
    //获取富文本编辑器的内容
    var con = tinyMCE.getInstanceById(editorId).getBody().innerHTML;
}