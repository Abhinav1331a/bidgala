$(document).ready(function(){
  trackChars();
  // validateFields();
  formatLinks();
  validateForms();
  
  
});

$(document).on("click", function(){
  validateForms();
});

function validateForms() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
}




function formatLinks() {
  $(document).on("input", function(event){
    if (event.target.type === "url") {
      if (event.target.value.includes("http://") || event.target.value.includes("https://")) {

        return
      } else {
        $(`#${event.target.id}`).val('')
        var withHttps = ("https://").concat(event.target.value)
        $(`#${event.target.id}`).val(withHttps)

      }
    
    
  };
})
}



function trackChars() {
  $(document).on("input", function(event) {
    var long = 1500;
    var short = 150;
    var med = 500;

    var longElements = ["artist-statement", "art-des", "des", "skills-data", "interests-data", "acc-des", "ex-des", "edit-des", "acc-des-edit", "ex-des-edit"]
    var shortElements = ["art-title", "school", "degree", "field-of-study", "acc-title", "acc-title-edit", "ex-title", "ex-location", "school", "degree", "field-of-study", "ex-title-edit" , "ex-location-edit", "ex-des-edit"]
    var medEls = ["acc-link", "ex-link", "acc-link-edit", "ex-link-edit"]

    if (longElements.includes(event.target.id)) {
      var count = $(`#${event.target.id}`).val().length;
        
      if (count == long) {
          $(`#${event.target.id}`).after("<span><small class='error text-danger'>Max characters reached (1500)</small></span>")
      } else {
          $(".error").empty()
      }
    } else if (shortElements.includes(event.target.id)) {
      var count = $(`#${event.target.id}`).val().length;
        
      if (count == short) {
          $(`#${event.target.id}`).after("<span><small class='error text-danger'>Max characters reached (150)</small></span>")
      } else {
          $(".error").empty()
      }
    } else if (medEls.includes(event.target.id)) {
      var count = $(`#${event.target.id}`).val().length;
        
      if (count == med) {
          $(`#${event.target.id}`).after("<span><small class='error text-danger'>Max characters reached (500)</small></span>")
      } else {
          $(".error").empty()
      }
    }
  })
}


// function validateFields() {
//   $(document).on("click",".submit-btn",function(event) {
//       event.preventDefault();  
//       console.log(event.target)
//       let formId = $(`#${event.target.form.id}`).attr('id');

//       let form = $(`#${formId}`)
//       var forms = form.get()

//       if (forms.checkValidity()) {
//         forms.submit();
//       } else {
//         console.log($(`#${formId}`).checkValidity())
//       }
  
//   });
// }

