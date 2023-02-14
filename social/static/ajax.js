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
function add_work(){

}
$(document).ready(function(){
    $("#update_work").on("click",function(){
        let work=$("#new_work").val();
        let from=$("#from").val();
        let to_date=$("#to_date").val();
        let work_place=$("#work_place").val();
        $.ajax({
            url:"/ajax/add/work",
            type:"POST",
            data:{job:work,start_date:from,end_date:to_date,country:work_place,csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
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
    });
});