$(document).ready(function(){
    var loginBtn = document.getElementById("loginBtn");

    var ui = document.getElementById("ui");
    var pi = document.getElementById("pi");

    var errorp = document.getElementById("errorp");
    errorp.style.display = "none";

    pi.addEventListener("blur",function(){
        $.get("/checkuserlogin/",{"userAccount":ui.value,"userPasswd":pi.value},function(data){

        if (data.status == "error"){
            errorp.style.display = "block"
        }
        // else {
        //     window.location.href = "http://127.0.0.1:8000/mine/"
        // }
    })
    },false)


});