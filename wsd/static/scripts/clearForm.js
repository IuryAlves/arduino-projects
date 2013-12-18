'use strict'

var buttonClear = document.getElementById("buttonClear");

buttonClear.onclick = function(){
	var form = document.getElementsByName("msg");
	form = form[0];
	form.value = "";
}