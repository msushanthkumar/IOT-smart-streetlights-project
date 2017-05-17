var username = " " ;

function check(){
     username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    if((username== "harsha") && (password=="1234")){
    $.mobile.changePage("#welcome","fade");
    document.getElementById('name_main').innerHTML="welcome  "+ username
}
else{ alert("invalid login information") ;}
}
//  function user () {
//  	  var username = document.getElementById('username').value;


//  document.getElementById('welcome').innerHTML="welcome"+username
// // 	// body...
//  }