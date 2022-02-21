$(function() {
$(".art-delete").click(function(){


	var id = $(this).attr('id')

$("#mi-modal").modal('show');

$("#modal-btn-si").on("click", function(){

	var token = $("input[name='csrfmiddlewaretoken']").val();

	$.ajax({

			url : "/art/delete-art",
			type : "POST",
			data : {
				csrfmiddlewaretoken: token,
				'id' : id,
			},

		headers : {
                   'X-CSRF-Token': token ,
               },
        success : function(result) {


        		$("#mi-modal").modal('hide');
        		$("div").remove("#" + id + "_div");
        		$("#mi-success-message").modal('show');
        		$("#modal-btn-success-close").on("click", function(){

        				$("#mi-success-message").modal('hide');
        			});
				singleArtCard();

			},
		error : function(XMLHttpRequest, textStatus, errorThrown) {


					$("#mi-modal").modal('hide');
					$("#mi-error-message").modal('show');
					$("#modal-btn-error-close").on("click", function(){
						$("#mi-error-message").modal('hide');
        			});
			}
});
});

$("#modal-btn-no").on("click", function(){

$("#mi-modal").modal('hide');
});

});
})
