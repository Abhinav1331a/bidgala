$(window).on('load', function(){
  var state = localStorage.getItem('order_viewing');
  if (state == 'buying') {
    $('.buying').click();
    $('.buying').addClass('active');
  } else {
    $('.selling').click();
    $('.selling').addClass('active');
  }
});

$('.selling').on('click', function(){
    localStorage.setItem('order_viewing', 'selling');
    $('.selling').addClass('active');
    $('.buying').removeClass('active');
    $('.container-buying').addClass('d-none');
    $('.container-selling').removeClass('d-none');
    $('.container-sales').addClass('d-none');
    $('.container-all-purchases').addClass('d-none');
});

$('.buying').on('click', function(){
    localStorage.setItem('order_viewing', 'buying');
    $('.buying').addClass('active');
    $('.selling').removeClass('active');
    $('.container-selling').addClass('d-none');
    $('.container-buying').removeClass('d-none');
    $('.container-sales').addClass('d-none');
    $('.container-all-purchases').addClass('d-none');
});


// fix this below

$('.sales').on('click', function(){
    $('.container-sales').removeClass('d-none');
    $('.container-selling').addClass('d-none');
    $('.container-buying').addClass('d-none');
    $('.container-all-purchases').addClass('d-none');
});

$('.all-purchases').on('click', function(){
    $('.container-sales').addClass('d-none');
    $('.container-selling').addClass('d-none');
    $('.container-buying').addClass('d-none');
    $('.container-all-purchases').removeClass('d-none');
});

  