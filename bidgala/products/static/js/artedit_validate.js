$(document).ready(function(){

  $("#price, #s_price, #quantity, #category, #subcategory").keydown(function(event)
  {
    if(event.which==32)
    {
      return false;
    }
  });

  $.validator.addMethod("categoryCheck", function (value, element) {
        if( $("#category").val() == 0){
          return true;
        }
        return false;
    }, 'Please select a category');



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



$.validator.addMethod(
        "pattern",
        function(value, element, regexp) {
            if (regexp.constructor != RegExp)
                regexp = new RegExp(regexp);
            else if (regexp.global)
                regexp.lastIndex = 0;
            return this.optional(element) || regexp.test(value);
        },
        "Please check your input."
);

  $("#artedit").validate({
    rules:{
      artname:{
        required:true,
      },

      artdescription:{
        required: true,
      },
      price:{
        required:true,
        pattern: /^[1-9]\d*(\.\d+)?$/,
        
      },
      s_price:{
        required:false,
        pattern: /^[1-9]\d*(\.\d+)?$/,
        
      },
      

      height:{
        required:true,
         pattern: /^[1-9]\d*(\.\d+)?$/,
        
      },

      width:{
        required:true,
         pattern: /^[1-9]\d*(\.\d+)?$/,
        
      },

      depth:{
        required: false,
        pattern: /^[0-9]\d*(\.\d+)?$/,
        
      },

      shipcanada:{
        required:true,
        pattern: /^[1-9]\d*(\.\d+)?$/,
        
      },

      

      measure: {
        required:true,
      }

    },
    highlight: function(element) {
        $(element).css('background', '#ffdddd');
    },
    unhighlight: function(element) {
        $(element).css('background', '#ffffff');
    },
  
    messages:{
      
      shipcanada:{
        required:"Please enter the shipping charges within canada. Put it 0 incase no shipping price.",
        pattern: "Please enter a valid number.",
        
      },

    
      height:{
        required:"",
        
        
      },

      width:{
        required:"",
       
        
      },

      depth:{
        
        pattern: "",
        
      },
      artdescription:{
        required:"Please enter the art description."
      },
      email:{
        required:"Please enter the art name.",
        
      },
      price:{
        required:"Please enter the price.",
        pattern: "Please enter a valid number.",
        
      },
      s_price:{
        required:"Please enter shipping price.",
        pattern: "Please enter a valid number.",
        
      },
      
       

      measure:{
        required:"Please select a dimension type.",
        
        
      }, 
    }
  });
});