var dev_ip = " ";
var dev_port = " ";
var dev_obj ;

function login() {
	var username = $("#user").val();
	var password = $("#pswd").val();
		
	if(username=='sushanth' && password=='123456') {
		$.mobile.changePage("#home", "fade");
		//document.getElementById("name").innerHTML = "Welcome <b>" + username + "</b>";
    $("#name").html('welcom<b>'+username+'<b>');
	} else {
		alert("Retry");
		document.getElementById("user").value = "";
		document.getElementById("pswd").value = "";
	} 
}


/*function to get the  setting details */


function connect (){



//alert("working");
/**/
// dev_ip =document.getElementById("ip_add").value;
  //dev_port =document.getElementById("ip_port").value;//these above two statements are converted into jquery for efficient code
dev_ip=$("#ip_add").val();
dev_port=$("#ip_port").val();
if(dev_ip==''||dev_port=='')
{
  $("#con_status").empty();
  $("#con_status").append('enter the valid data');
}

  dev_obj = new WebSocket( 'ws://'+ dev_ip + ':' +dev_port );

 console.log(dev_port);
 console.log(dev_ip);

   /**/

    dev_obj.onopen=function (){

     $('#con_status').empty();
	 $('#con_status').append('Device connected');
   $('#con_btn').empty();
   $('#con_btn').append('device disconnected');
   //  dev_obj_CONNECT = true;
   //   dev_obj_con_control();
   //   status_log('dev_obj is now connected!');

       
     
  };
  
  dev_obj.onclose=function(){


  	  $('#con_status').empty();
	 $('#con_status').append('Not connected');
   
  // dev_obj_CONNECT=false;
  // dev_obj_con_control();
   
 // status_log('dev_obj lost its connection .Check your network or IP !!');
   
   };


dev_obj.onmessage = function (e) {
  console.log(e.data);
//  status_log('Server: ' + e.data);
};

/*
dev_obj.on('message',function(message){
		
	
		status_log(message); 
		
		});


*/        




}

/* Use the Device object to send  msg  to the Device

  var new_toggle = $("#flip-1").val() ; 

  if(new_toggle =="on") {

console.log('its on') ;
 //dev_obj.send('on');

  }

  if(new_toggle == "off" ){

  	console.log('its off');

  //	dev_obj.send('off');


  }


  */

/*--------------*/
$( document ).delegate( "#flip-1", "change", function() {

var new_toggle = $("#flip-1").val() ; 

if(new_toggle =="on") {

//console.log('its on') ;
 dev_obj.send('on');

  }

  if(new_toggle == "off" ){

  //	console.log('its off');

  	dev_obj.send('off');


  }



//console.log(new_toggle) ;

})
