document.getElementById('add-student-form').onsubmit=function(){
   var bio_cred = document.getElementsByClassName("bio-cred")[0]
   css(bio_cred, {
       "opacity":"1"
   });
   var cred = document.getElementsByClassName("cred")[0]
   css(cred, {
       "opacity":"0.9"
   });
   var submit_btn=document.getElementById("submit-btn");
   css(submit_btn, {
        "display":"none"
    });
}
document.getElementsByClassName('bio-cred')[0].onclick=function(){
    var bio_cred = document.getElementsByClassName("bio-cred")[0]
   css(bio_cred, {
       "color":"#4BA56A"
   });
   document.getElementById('finish-btn').className='btn btn-primary';
}


function css(element, style) {
    for (const property in style)
        element.style[property] = style[property];
}