//Update Search Bar Dropdown Option and animate click
var btn = document.getElementById("btn");
var input = document.getElementById("input");

btn.addEventListener("click", function(){
   this.classList.toggle("btn_active");
   input.classList.toggle("input_active");
})