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



  $("#artuploadform").validate({
    
    invalidHandler: function(form, validator) {
        
        if (!validator.numberOfInvalids())
            return;
        
        $('html, body').animate({
            scrollTop: $(validator.errorList[0].element).offset().top -500
        }, 100);
        
    },

    rules:{
      artname:{
        required:true,
      },

      artdescription:{
        required: true,
      },
      price:{
        required:true,
        digits: true,
        
      },
      s_price:{
        required:true,
        digits: true,
        
      },
      quantity:{
        required:true,
        digits: true,
        
      },
      
      subcategory:{
        required:true
      },

      tags2: {
        required:true
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
        pattern: /^[1-9]\d*(\.\d+)?$/,
        
      },

      shipcanada:{
        digits: true,
        min: 0,
        
      },

      shipus:{
        digits: true,
        min: 0,
        
      },

      shipuk:{
        digits: true,
        min: 0,
        
      },

      shipaunz:{
        digits: true,
        min: 0,
        
      },
      
      shipasia:{
        digits: true,
        min: 0,
        
      },

      shipother:{
        digits: true,
        min: 0,
        
      },

      shipeurope:{
       
        digits: true,
        min: 0,
        
      },

      measure: {
        required:true,
      }

    },
    // invalidHandler: function(form, validator) {
        
    //     if (!validator.numberOfInvalids())
    //         return;
        
    //     $('#uploadimageModal').animate({
    //         scrollTop: $(validator.errorList[0].element).first().offset().top + 300
    //     }, 4000);
        
    // },
    highlight: function(element) {
        $(element).css('background', '#ffdddd');
    },
    unhighlight: function(element) {
        $(element).css('background', '#ffffff');
    },
  
    messages:{
      
      shipcanada:{
        
        digits: "Please enter a valid number.",
        min: "Shipping price cannot be less than 0.",
        
      },


      shipus:{
        
        digits: "Please enter a valid number.",
        min: "Shipping price cannot be less than 0.",
        
      },

      shipuk:{
        
        digits: "Please enter a valid number.",
        min: "Shipping price cannot be less than 0.",
        
      },

      shipaunz:{
        
        digits: "Please enter a valid number.",
        min: "Shipping price cannot be less than 0.",
        
      },
      
      shipasia:{
       
        digits: "Please enter a valid number.",
        min: "Shipping price cannot be less than 0.",
        
      },

      shipeurope:{
       
        digits: "Please enter a valid number.",
        min: "Shipping price cannot be less than 0.",
        
      },

      shipother:{
      
        digits: "Please enter a valid number.",
        min: "Shipping price cannot be less than 0.",
        
      },

    
      height:{
        required:"",
        pattern: "",
        
      },

      width:{
        required:"",
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
        digits: "Please enter a valid number.",
        
      },
      s_price:{
        required:"Please enter shipping price.",
        digits: "Please enter a valid number.",
        
      },
      quantity:{
        required:"Please enter available quantity.",
        digits: "Please enter a valid number.",
        
      },
      category:{
        required:"Please select a category.",
        categoryCheck: "Please select an option.",
        
      },  
      subcategory:{
        required:"Please select a subcategory.",
        
      },  

      measure:{
        required:"Please select a dimension type.",
        
        
      }, 
    }
  });
});