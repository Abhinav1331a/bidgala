// Carousel for Featured Art

$(document).ready(function () {
  const featuredArtist = document.querySelector('.featured-artists');
  const featuredArtistLinks = featuredArtist.querySelectorAll('a');
  const leftArrow = document.getElementById('pre-top-art');
  const rightArrow = document.getElementById('next-top-art');
  if (featuredArtistLinks.length > 6) {
    $(".featured-artists").slick({
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 6,
        slidesToScroll: 6,
        nextArrow: $("#next-top-art"),
        prevArrow: $("#pre-top-art"),
        responsive: [
        {
            breakpoint: 1200,
            settings: {
            // infinite: true,
            // speed: 500,
                slidesToShow: 5,
                slidesToScroll: 5,
            // dots: false,
            // centerMode: true,
            }
        },
        {
            breakpoint: 700,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 4,
            }
        }
        ],
    });
  } else {
      leftArrow.remove();
      rightArrow.remove();
      featuredArtist.style.gap = '10px';
  }

  $(".curator-picks").slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 6,
    nextArrow: $("#next-curator-pick"),
    prevArrow: $("#pre-curator-pick"),
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 5,
          slidesToScroll: 5,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 970,
        settings: {
          infinite: true,
          slidesToShow: 4,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
        },
      },
      {
        breakpoint: 840,
        settings: {
          infinite: true,
          slidesToShow: 3,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
        },
      },
      {
        breakpoint: 650,
        settings: {
          infinite: true,
          slidesToShow: 2,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
        },
      },
      {
        breakpoint: 400,
        settings: {
          infinite: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
          arrows: true,
        },
        
      },
      
    ],
  });

  $(".articles").slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 4,
    variableWidth: true,
    centerMode: true,
    nextArrow: $("#next-articles"),
    prevArrow: $("#prev-articles"),
    responsive: [
     
    ],
  });



  

  $(".trending-art").slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 6,
    nextArrow: $("#next-trending"),
    prevArrow: $("#prev-trending"),
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 5,
          slidesToScroll: 5,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 970,
        settings: {
          infinite: true,
          slidesToShow: 4,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
        },
      },
      {
        breakpoint: 840,
        settings: {
          infinite: true,
          slidesToShow: 3,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
        },
      },
      {
        breakpoint: 650,
        settings: {
          infinite: true,
          slidesToShow: 2,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
        },
      },
      {
        breakpoint: 400,
        settings: {
          infinite: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          dots: false,
          centerMode: true,
        },
      },
    ],
  });


});


$(window).on('load resize orientationchange', function() {


  $('.channels').each(function(){
      var $carousel = $(this);
      /* Initializes a slick carousel only on mobile screens */
      // slick on mobile
      var mq = window.matchMedia( "(max-width: 1200px)" );

      if (!mq.matches) {
          if ($carousel.hasClass('slick-initialized')) {
              $carousel.slick('unslick');
          }
      }
      else{
          if (!$carousel.hasClass('slick-initialized')) {
              $carousel.slick({
                  nextArrow: $("#next-channels"),
                  prevArrow: $("#prev-channels"),
                  slidesToShow: 3,
                  slidesToScroll: 1,
                  centerMode: true,
                  variableWidth: true,
              
              });
          }
      }
  });
});