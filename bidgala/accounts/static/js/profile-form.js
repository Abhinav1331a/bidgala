$(document).ready(function() { 




$('.stripe-start').on('click', function(e) {
	 
	$(this).prop('disabled',true); 
	$("#preloader-active").css("display", "block");
})



	 var readURL = function(input) {

        if (input.files && input.files[0]) {

            var reader = new FileReader();

            reader.onload = function (e) {
            	
                
                $('.profile .avatar').css('background-image', 'url(' + e.target.result + ')');
                $('#profile-form').submit()
            }
    
            reader.readAsDataURL(input.files[0]);
        }
    };
 


    $(".file-upload").on('change', function(){
        readURL(this);

    });
    
    $(".upload-button").on('click', function() {
       $(".file-upload").click();
    });

    $(document).on('click', '.submit-profile-edit', function(){
  	

		var firstname = $("input[name='firstname']").val();
		var lastname = $("input[name='lastname']").val();
		var username = $("input[name='username']").val();
		var phone = $("input[name='phone']").val();
		var bio = $("#comment").val();
		var account_type = $("select[name='account_type']").val();
		var location = $("select[name='location']").val();
		var pic = $("input[name='user_profile_pic']").val();
		var region =  $("#region").val();
		var country =  $('#region :selected').parent().attr('value');
		var cname = $("input[name='cname']").val();
		var cemail = $("input[name='cemail']").val();
		var cweb = $("input[name='cweb']").val();
		var instagram = $("input[name='instagram']").val();
		var twitter = $("input[name='twitter']").val();
		var facebook = $("input[name='facebook']").val();
		var linkedin = $("input[name='linkedin']").val();
		var headline = $("input[name='headline']").val();

		var blog = false;
		var newsletter = false;
		var offers = false;

		if ($("#notifications-blog").is( 
                      ":checked")) { 
                        blog = true
                    } 
        
        if ($("#notifications-news").is( 
                      ":checked")) { 
                        newsletter = true
                    } 

        if ($("#notifications-offers").is( 
                      ":checked")) { 
                        offers = true
          	        } 

		var token = $("input[name='csrfmiddlewaretoken']").val();
		
		
		$.ajax({
			url : "/profile-update",
			type : "POST",
			data : {
				csrfmiddlewaretoken: token,
				'firstname' : firstname,
				'lastname' : lastname,
				'username' : username,
				'bio' : bio,
				'account_type' : account_type,
				'location' : location,
				'phone' : phone,
				'user_profile_pic': pic,
				'region' : region,
				'country' : country,
				'blog' : blog,
				'newsletter' : newsletter,
				'offer' : offers,
				'cname' : cname,
				'cemail' : cemail,
				'instagram' : instagram,
				'twitter': twitter,
				'facebook': facebook,
				'linkedin': linkedin,
				'headline': headline,
				'cweb' : cweb,
			},
			headers : {
                    'X-CSRF-Token': token 
               },

			success : function(result) {
				if($("select[name='account_type']").val() != 'pro') {
						
						$("input[name='cname']").val('');
						$("input[name='cemail']").val('');
					}

				if (result.status != "success") {

					
					$("#showMessage").append("<div class='alert alert-danger'>"+result.message+"</div>").delay(4000).fadeOut(function() {
   				$(this).empty();
   				$(this).removeAttr('style');
				});
				}
				else {
				$("#showMessage").append("<div class='alert alert-success'>"+ result.message +"</div>").delay(4000).fadeOut(function() {
   				$(this).empty();
   				$(this).removeAttr('style');
				});
			}

			},

			error : function(XMLHttpRequest, textStatus, errorThrown) {
				$("#showMessage").append("<div class='alert alert-danger'>Something went wrong :-(</div>").delay(4000).fadeOut(function() {
   				$(this).empty();
   				$(this).removeAttr('style');
				});

			}

			
		})


	})
})