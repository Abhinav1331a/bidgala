$(document).ready(function() {
	$( "form" ).submit(function( event ) {  
  		
  		var id = $(this).attr("id")

  		if($("#tracking_id_" + id).val().trim().length || $($(this.id).context.activeElement).val() == 'DECLINE') {
  			return true
  		} else {
  			$("#tracking_id_" + id).css({ "border": '#FF0000 1px solid'});
  			return false
  		}
  	
  	});  

})