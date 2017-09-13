$(document).ready(function(){

    var alltypebtn = document.getElementById("alltypebtn");
    var showsortbtn = document.getElementById("showsortbtn");

    var typediv = document.getElementById("typediv");
    var sortdiv = document.getElementById("sortdiv");

    typediv.style.display = "none";
    sortdiv.style.display = "none";

    alltypebtn.addEventListener("click",function(){
        typediv.style.display = "block";
        sortdiv.style.display = "none";
    },false);

    showsortbtn.addEventListener("click",function(){
        typediv.style.display = "none";
        sortdiv.style.display = "block"
    },false);

    typediv.addEventListener("click",function(){
        this.style.display = "none"
    },false);
    sortdiv.addEventListener("click",function(){
        this.style.display = "none"
    },false);


//     var sortas  = document.getElementsByClassName("sorta")
//     for (var i = 0; i < sortas.length; i++){
//         var str = window.location.href;
//         var str1 = str.split(":")[2];
//         var arr2 = str1.split("/");
//         //  http://127.0.0.1:8000/market/103532/0/0/
//         hrefstr = "/" + arr2[1] + "/" + arr2[2] + "/" + arr2[3] + "/" + i + "/"
// //        console.log(hrefstr)
//         sortas[i].href = hrefstr
//     }


});