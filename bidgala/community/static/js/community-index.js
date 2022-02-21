
$('.icon-submit').click(function() {
  var text = $(this).parent().siblings('textarea').val();
  $('#newDivs').append('<div>' + text + '</div>');
});



$(function () {
  $(".like").click(function () {
      $(this).toggleClass('cs');
  })
})


// Hide the thread
$(document).ready(function () {
  $('.thread-title').click(function () {
    $('div#container').show();
  });
  $('a.close').click(function () {
    $('div#container').hide();
  });
});


//Show/hide the comment textarea
$(document).ready(function () {
  $('.comment-new').click(function () {
    $(this).siblings('.comment-window').slideToggle("slow");
  });
});

    /* When the user clicks on the button,
    toggle between hiding and showing the dropdown content */
    // function myFunction() {
    //     document.getElementById("myDropdown").classList.toggle("show");
    // }
  function showDropDown(element) {
      var elements = ".dropdown-content";
      var elements_buttons = ".dropbtn";
      var element_click = $(element).next(elements);
      if (element_click.hasClass("show")) {
          element_click.removeClass('show');
          $(element).css('background-color', '#FFFFFF');
      } else {
          $(elements).removeClass('show');
          $(elements_buttons).css('background-color', '#FFFFFF');
          $(element).css('background-color', '#E8E8E8');
          element_click.toggleClass("show");
      }

  }

  // Close the dropdown if the user clicks outside of it
  window.onclick = function (event) {
      if (!$(event.target).parent().hasClass('dropbtn') && !$(event.target).parent().hasClass('dropdown')) {
          var dropdowns = document.getElementsByClassName("dropdown-content");
          var i;
          for (i = 0; i < dropdowns.length; i++) {
              var openDropdown = dropdowns[i];
              if (openDropdown.classList.contains('show')) {
                  openDropdown.classList.remove('show');
              }
          }
          $('.dropbtn').css('background-color', '#FFFFFF');
      }
  }

  function hideContent(element) {
      $(element).closest(".thread").hide();
  }

//Like function
  $(document).ready(function () {
      $(".fa-thumbs-o-up").click(function () {
          $(this).toggleClass("fa-thumbs-o-up fa-thumbs-up");
          $(this).parent().siblings().toggleClass("down active");
      });


  });
    // function clickLike(x) {
    //     x.classList.toggle("fa-thumbs-up");
    // }

  // $(document).ready(() => {
  //     $('div.channels').slick();
  //     $(window).resize();
  // });
  //
  //
  // $(window).resize(function(e){
  //     if($(window).width() <= 320)
  //     {
  //         $('div.channels').slick('unslick');
  //         $('div.channels').slick({
  //           slidesToShow: 2,
  //           slidesToScroll: 1,
  //           infinite: true,
  //           arrows: true,
  //           variableWidth: true,
  //           prevArrow: $('.prev'),
  //           nextArrow: $('.next'),
  //         });
  //     }
  //
  //     else if($(window).width() <= 480)
  //     {
  //         $('div.channels').slick('unslick');
  //         $('.channels').slick({
  //             slidesToShow: 2,
  //             slidesToScroll: 1,
  //             infinite: true,
  //             arrows: true,
  //             variableWidth: true,
  //             prevArrow: $('.channel-prev'),
  //             nextArrow: $('.channel-next'),
  //         });
  //     }
  //
  //     else if($(window).width() <= 542)
  //     {
  //         $('div.channels').slick('unslick');
  //         $('.channels').slick({
  //             slidesToShow: 3,
  //             slidesToScroll: 1,
  //             infinite: true,
  //             arrows: true,
  //             variableWidth: true,
  //             prevArrow: $('.channel-prev'),
  //             nextArrow: $('.channel-next'),
  //         });
  //     }
  //
  //     else if($(window).width() <= 767)
  //     {
  //         $('div.channels').slick('unslick');
  //         $('.channels').slick({
  //             slidesToShow: 4,
  //             slidesToScroll: 1,
  //             infinite: true,
  //             arrows: true,
  //             variableWidth: true,
  //             prevArrow: $('.channel-prev'),
  //             nextArrow: $('.channel-next'),
  //         });
  //         // $( ".slick-prev" ).append( "<i class='fa fa-chevron-left' aria-hidden='true'></i>" );
  //         // $( ".slick-next" ).append( "<i class='fa fa-chevron-right' aria-hidden='true'></i>" );
  //     }
  // 
  //     else{
  //         $('div.channels').slick('unslick');
  //         // $('.channels').slick({
  //         //     slidesToShow: 5,
  //         //     slidesToScroll: 1,
  //         // });
  //     }
  //
  // });





  $(document).on('click','.like-bt-click',function(){
      var post_id = $(this).data("id")
      current_element = $(this)

          $.ajax({
                  url:'/community/add-like',
                  type:'POST',
                  data:{
                      'post_id': post_id,
                      'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                  },
                  success:function(data){

                      if(data.result == 'increment') {
                      $(".like-button .like-btn"+data.postid).attr("id", "unlike-btn")
                      $(".like-count"+data.postid).html(parseInt($(".like-count"+data.postid).html(), 10)+1)
                      $(this).data('status', 'like')
                      current_element.empty().html('<i class="fa fa-thumbs-up" aria-hidden="true"></i>')
                      $("#count-" + post_id).removeClass("down").addClass("active")

                      } else {
                          $(".like-button .like-btn"+data.postid).attr("id", "like-btn")
                          $(".like-count"+data.postid).html(parseInt($(".like-count"+data.postid).html(), 10)-1)
                          $(this).data('status', 'unlike')

                          current_element.empty().html('<i class="fa fa-thumbs-o-up" aria-hidden="true"></i>')
                          $("#count-" + post_id).removeClass("active").addClass("down")
                      }
                  },
                  error: function(xhr, status, error) {
                      var err = eval("(" + xhr.responseText + ")");
                      console.log(err.Message);
                  },
              });


  });


  // Populate value of channel name when selecting a channel from the dropdown so it can be sent in form data
  $(".dropdown-menu a").on("click", function() {
      $('.dropdown-channel').text($(this).text());
      $('#channel-name').val($('.dropdown-channel').text())
      $('.dropdown-menu').removeClass('open');
  });
