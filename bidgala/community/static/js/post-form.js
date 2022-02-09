// Show alert and prevent default if no channel is selected
$(document).ready(function(){ 
  $('#post-submit').on("click", function(event) {
      dropdownValue = $(".dropdown-channel").html()
      if ($.trim(dropdownValue) == "Select Channel") {
              event.preventDefault()
              $('#choose-channel-alert').show().fadeOut(5000)
      } 
  })
}); 

// For text editor
var quill = new Quill('#editor', {
    modules: {
        toolbar: [
            ['bold', 'italic'],
            ['link', 'blockquote', 'code-block', 'image'],
            [{ list: 'ordered' }, { list: 'bullet' }]
        ]
    },
    theme: 'snow', placeholder: 'Text (Optional)',
});


$("form").submit(function(event) {
    // Populate hidden form on submit
    $("#content-data").val(quill.root.innerHTML);
    return ;
});

// Populate value of channel name when selecting a channel from the dropdown so it can be sent in form data
$(".dropdown-menu a").on("click", function() {
    $('.dropdown-channel').text($(this).text());
    $('#channel-name').val($('.dropdown-channel').text())
    $('.dropdown-menu').removeClass('open');
});


