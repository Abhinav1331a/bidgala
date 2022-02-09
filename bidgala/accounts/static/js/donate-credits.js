
$(document).on('click','#donate-credits',function(){
  var donationAmount = $(this).data('credits');
  console.log(donationAmount)

  $.ajax({
      url:'/donate-credits',
      type:'POST',
      data:{
          'donation_amount': donationAmount,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
      },
      success:function(response){
          if (response.status == "success") {
              $('#confirm-donation-modal').modal('hide');
              $('#thank-you-modal').modal('show');
              $('#donated-credits').html(parseInt($('#donated-credits').html(), 10)+donationAmount)
              $('#available-credits').html(parseInt($('#available-credits').html(), 10)-donationAmount)
              if ($('#available-credits').html() == 0) {
                $("#donate-credits-btn").attr("data-target", "#not-enough-credits")
              }
          }
      },
      error:function(){
          console.log('error')
      },
  });
});