$(document).ready(function(){


	$.ajax({
      url: "/track/location",
      type: "GET",
   
      success: function (result) {
      	console.log('success')
      },
      error: function (XMLHttpRequest, textStatus, errorThrown) {},

    });



})