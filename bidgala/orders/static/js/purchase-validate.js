$(document).ready(function(){

  $("#phone_popup").keydown(function(event) 
  {
    if(event.which==32)
    {
      return false;
    }
  });

  $.validator.setDefaults({
    errorClass:"help-block",
    errorElement:"span",
    errorPlacement: function(error, element) {
      return true;
  },
    highlight:function(element){
      $(element).closest(".form-group").addClass("has-error");

    },
    unhighlight:function(element)
    {
      $(element).closest(".form-group").removeClass("has-error");
    }
  });




  $("#purchase-request-form").validate({
    rules:{
      first_name_popup:{
        required:true,
      },
      last_name_popup:{
        required:true,
        
      },
      phone_popup: {
        required:true,
        
      },
      address_popup: {
        required:true,
        
      },
      city_popup: {
        required:true,
        
      },
      state_popup: {
        required:true,
        
      },
      postal_popup: {
        required:true,
        
      },
      purchase_req_agree: {
        required:true,
        
      }
    },
    highlight: function(element) {
        $(element).css('background', '#ffdddd');
    },
    unhighlight: function(element) {
        $(element).css('background', '#ffffff');
    },
    submitHandler:function(form) {
      form.submit();
    },

    messages:{
      first_name_popup:{
        required:"Please enter the first name",
      },
      last_name_popup:{
        required:"Please enter the last name",
        
      },
      phone_popup: {
        required:"Please enter the phone number",
        
      },
      address_popup: {
        required:"Please enter the address",
        
      },
      city_popup: {
        required:"Please enter the city",
        
      },
      state_popup: {
        required:"Please enter the state",
        
      },
      postal_popup: {
        required:"Please enter the postal code",
        
      
      purchase_req_agree: {
        required:"Please agree to the terms",
        
      },
    
 }
}
})})