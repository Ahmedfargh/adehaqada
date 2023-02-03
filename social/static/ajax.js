function add_to_my_favorite(fav_nam){
    $.ajax({
        url:"/ajax/ad/fav",
        type:"POST",
        data:{fav_name:fav_nam,csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
        success:function(data){
            alert("تمت العملية بنجاح");
        },
        statusCode:{
            404:function(data){
                alert("أفحص أتصالك بالأنترنت");
            },
            503:function(data){
                alert("خطأ فى الخادم");
            }
        }
    });
}
function delete_interest(personal_fav_id){
    alert("fuck fuck go");
    $.ajax({
        url:"/ajax/del/fav",
        type:"POST",
        data:{personal_fav_id:personal_fav_id,csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
        success:function(data){
            alert("تمت العملية بنجاح");
        },
        statusCode:{
            404:function(data){
                alert("أفحص أتصالك بالأنترنت");
            },
            503:function(data){
                alert("خطأ فى الخادم");
            }
        }
    });
}
$(document).ready(function(){
});