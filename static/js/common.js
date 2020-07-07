
function movePage(action){
    var form = document.getElementById("navigation_form");
    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);
    form.submit();
}

function moveToDetail(action, key){

    var form = document.getElementById("navigation_form");

    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);

    var elm2 = document.createElement("input");
    elm2.setAttribute("name", "key");
    elm2.setAttribute("type", "hidden");
    elm2.setAttribute("value", key);
    form.appendChild(elm2);

    form.submit();
}

function moveToDetailFromList(action, key){
    var form = document.getElementById("list_form");

    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);

    var elm2 = document.createElement("input");
    elm2.setAttribute("name", "key");
    elm2.setAttribute("type", "hidden");
    elm2.setAttribute("value", key);
    form.appendChild(elm2);

    form.submit();
}

function deleteRecord(action, key){
    var form = document.getElementById("list_form");
    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);

    var elm2 = document.createElement("input");
    elm2.setAttribute("name", "key");
    elm2.setAttribute("type", "hidden");
    elm2.setAttribute("value", key);
    form.appendChild(elm2);

    form.submit();
}

$(".tab_label").on("click",function(){
 var $th = $(this).index()+1;
 $(".tab_label").removeClass("active");
 $(".tab_panel").removeClass("active");
 $(this).addClass("active");
 $("#panel"+$th).addClass("active").appendTo($("#cj_panelarea"));
});

function like(api_url, comment_id) {
    var btn = document.getElementById("like-count-" + comment_id);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            var received_data = JSON.parse(request.responseText);
            btn.innerText = received_data.like;
        }
    }
    request.open("GET",api_url);
    request.send();
}
