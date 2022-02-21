$(document).ready(function(){

  $("#password , #email").keydown(function(event) 
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
       if(element.parent('.input-group').length) {
           error.insertAfter(element.parent());
       } else {
           error.insertAfter(element);
       }
   },
    highlight:function(element){
      $(element).closest(".form-group").addClass("has-error");

    },
    unhighlight:function(element)
    {
      $(element).closest(".form-group").removeClass("has-error");
    }
  });


  $.validator.addMethod("notEqualTo", function(value, element, param) {
    return this.optional(element) || value != $(param).val();
  }, "Passwords do not match");


  $("#register-form").validate({
    rules:{
      email:{
        required:true,
        email:true
      },
      password:{
        required:true,
        minlength:8
      },
      first_name: {
        required:true,
        minlength:1,
        maxlength:40
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
      email:{
        required:"Please enter an email address.",
        email:"Please enter a valid email address."
      },
      password:{
        required:"Please enter the password.",
        minlength: "Password must be at least 8 characters long."
      },
      first_name:{
        required:"Please enter the first name",
        
      }
    }
  });
});