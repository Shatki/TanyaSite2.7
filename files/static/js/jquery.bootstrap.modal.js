/* ====================================================
 * jQuery Bootstrap 4 modal.
 *
 * ==================================================== */
(function(a){a.createModal=function(b){
    defaults={
        title:"title",
        message:"Your Message Goes Here!",
        closeButton:true,
        scrollable:false};
    var b=a.extend({}, defaults,b);
    var c=(b.scrollable===true)?'style="max-width: 800px; max-height: 480px;overflow-y: auto;"':"";
    html='<div class="modal fade" id="pdfModal">';
    html+='<div class="modal-dialog">';
    html+='<div class="modal-content">';
    html+='<div class="modal-header">';
    if(b.title.length>0){
        html+='<h4 class="modal-title">'+b.title+"</h4>"}html+="</div>";html+='<div class="modal-body" '+c+">";
    html+=b.message;
    html+="</div>";
    html+='<div class="modal-footer">';
    if(b.closeButton===true){
        html+='<button type="button" class="btn btn-primary" data-dismiss="modal">Закрыть</button>'}html+="</div>";
    html+="</div>";html+="</div>";
    html+="</div>";
    a("body").prepend(html);
    a("#pdfModal").modal().on("hidden.bs.modal",function(){
        a(this).remove()
    })}
})(jQuery);