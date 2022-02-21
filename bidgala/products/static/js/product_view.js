// Carousel for individual art posting images

// $(document).ready(function(){ 
//   $(".slider-for").slick({
//     slidesToShow: 1,
//     slidesToScroll: 1,
//     nextArrow: $(".next-arrow"),
//     prevArrow: $(".previous-arrow"),
//     fade: true,
//     asNavFor: ".slider-nav",
//     autoplay: false,
//   });
//   $(".slider-nav").slick({
//     slidesToShow: 4,
//     slidesToScroll: 1,
//     asNavFor: ".slider-for",
//     dots: false,
//     centerMode: true,
//     focusOnSelect: true,
//     nextArrow: $(".next-arrow"),
//     prevArrow: $(".previous-arrow"),
//   });
//   $('.slider-for').slick('refresh');



//   $(".product-page").on("contextmenu",function(e){
//     return false;
//  });


// });

const singleImage = document.querySelector('.single-image');
const moreItems = document.querySelectorAll('.more-items');
moreItems.forEach(moreItem => moreItem.addEventListener('click', () => {
    singleImage.src = moreItem.firstElementChild.src;
}))

$(document).ready(function() {
    const moreFromArtist = document.querySelector('.more-from-artist');
    const moreFromArtistLinks = moreFromArtist.querySelectorAll('a');
    const artCard = moreFromArtist.querySelectorAll('.art-card');
    const leftArrow = document.querySelector('#prev-more-from');
    const rightArrow = document.querySelector('#next-more-from');
    if (moreFromArtistLinks.length >= 6) {
        $(".more-from-artist").slick({
            dots: false,
            infinite: true,
            speed: 300,
            slidesToScroll: 1,
            variableWidth: true,
            nextArrow: $("#next-more-from"),
            prevArrow: $("#prev-more-from"),
        });
    } else {
        leftArrow.remove();
        rightArrow.remove();
        artCard.forEach(art => {
            art.style.height = '125px';
        })
        moreFromArtist.style.marginBottom = '65px';
    }
});


// $(window).on('load resize orientationchange', function() {


//   $('.more-from-artist').each(function(){
//       var $carousel = $(this);
//       /* Initializes a slick carousel only on mobile screens */
//       // slick on mobile
//       var mq = window.matchMedia( "(max-width: 1200px)" );

//       if (!mq.matches) {
//           if ($carousel.hasClass('slick-initialized')) {
//               $carousel.slick('unslick');
//           }
//       }
//       else{
//           if (!$carousel.hasClass('slick-initialized')) {
//               $carousel.slick({
//                   nextArrow: $("#next-channels"),
//                   prevArrow: $("#prev-channels"),
//                   slidesToShow: 3,
//                   slidesToScroll: 1,
//                   centerMode: true,
//                   variableWidth: true,
              
//               });
//           }
//       }
//   });
// });