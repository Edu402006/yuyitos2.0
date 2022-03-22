let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")

menu.addEventListener("click", function(){
    if(nav.style.height == "60px" || nav.offsetHeight == 60){
        nav.style.height = 60 + nav.offsetHeight + "px"
    } else{
        nav.style.height = "60px"
    }    
})

window.addEventListener("resize", function(){
    let ancho = document.documentElement.clientWidth
    if(ancho > 540){
        nav.style = ""
    }
})
$(document).ready(function(){
    $('.dropdown-toggle').dropdown()
});