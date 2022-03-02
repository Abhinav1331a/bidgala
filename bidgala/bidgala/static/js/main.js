(function ($) {
  "use strict";

  /* Preloder */
  $(window).on("load", function () {
    $("#preloader-active").delay(450).fadeOut("slow");
    $("body").delay(450).css({
      overflow: "visible",
    });
  });

  $("#account-demo").on("focus", function (event) {
    $("#account-demo").hover();
    $("#account-demo").trigger("hover");
    $("#account-demo").trigger("mouseover");
  });

  // /* Custom Sticky Nav  */
  // var previousScroll = 0;
  // $(window).on("scroll", function () {
  //     var scroll = $(this).scrollTop();
  //     if (scroll > previousScroll) {
  //         $(".header-sticky").removeClass("sticky-bar");
  //         $(".header-sticky").removeClass("sticky");
  //         $(".dropdown-container-desktop").removeClass("sticky-menu");
  //     } else {
  //         $(".header-sticky").addClass("sticky-bar");
  //         $(".header-sticky").addClass("sticky");
  //         $(".dropdown-container-desktop").addClass("sticky-menu");
  //         if(scroll==0){
  //             $(".header-sticky").removeClass("sticky-bar");
  //             $(".header-sticky").removeClass("sticky");
  //             $(".dropdown-container-desktop").removeClass("sticky-menu");
  //         }
  //     }
  //     previousScroll = scroll;
  // });

  /* Scroll Up */
  $.scrollUp({
    scrollName: "scrollUp", // Element ID
    topDistance: "300", // Distance from top before showing element (px)
    topSpeed: 300, // Speed back to top (ms)
    animation: "fade", // Fade, slide, none
    animationInSpeed: 200, // Animation in speed (ms)
    animationOutSpeed: 200, // Animation out speed (ms)
    scrollText: '<i class="fas fa-angle-up"></i>', // Text for element
    activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
  });

  // Slick slider
  $(".slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    speed: 300,
    infinite: true,
    asNavFor: ".slider-nav-thumbnails",
    autoplay: true,
    pauseOnFocus: true,
    dots: true,
  });

  $(".slider-nav-thumbnails").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: ".slider",
    focusOnSelect: true,
    infinite: true,
    prevArrow: false,
    nextArrow: false,
    centerMode: true,
    responsive: [
      {
        breakpoint: 480,
        settings: {
          centerMode: false,
        },
      },
    ],
  });

  // Search Toggle
  $("#search_input_box").hide();
  $("#search_1").on("click", function () {
    $("#search_input_box").slideToggle();
    $("#search_input").focus();
  });
  $("#close_search").on("click", function () {
    $("#search_input_box").slideUp(500);
  });

  $(".select_option_dropdown").hide();
  $(".select_option_list").click(function () {
    $(this)
      .parent(".select_option")
      .children(".select_option_dropdown")
      .slideToggle("100");
    $(this).find(".right").toggleClass("fas fa-caret-down, fas fa-caret-up");
  });

  $(".select_option_list").click(function () {
    $(this)
      .parent(".select_option")
      .children(".open_option_dropdown")
      .slideToggle("100");
    $(this).find(".right").toggleClass("fas fa-caret-up, fas fa-caret-down");
  });

  if ($(".new_arrival_iner").length > 0) {
    var containerEl = document.querySelector(".new_arrival_iner");
    var mixer = mixitup(containerEl);
  }

  $(".controls").on("click", function () {
    $(this).addClass("active").siblings().removeClass("active");
  });

  // Mobile menu
  $(document).ready(function () {
    $(".button-nav-toggle").click(function () {
      $(".main").toggleClass("open");
      $(".menu").toggleClass("open");
      $(".nav-main").addClass("open");
      $("body").toggleClass("overflow-y-hidden");
    });

    $(".close").click(function () {
      $(".main").removeClass("open");
      $(".menu").removeClass("open");
      $(".nav-main").removeClass("open");
      $("body").removeClass("overflow-y-hidden");
      $(".nav-container").removeClass("show-sub");
      $(".has-sub-nav").removeClass("active");
      $(".dropdown-container").removeClass("show");
      $("i.fa-angle-down").toggleClass("fa-angle-down fa-angle-right");
    });

    $(".nav-main li:has(ul)")
      .addClass("has-sub-nav")
      .prepend('<div class="sub-toggle"></div>');

    $(".has-sub-nav a.second-level").click(function () {
      $(this).parent().addClass("active");
      $(".nav-container").addClass("show-sub");
    });

    $(".has-sub-nav .back").click(function () {
      $(".nav-container").removeClass("show-sub");

      $(".has-sub-nav").removeClass("active");
    });

    $("a.child-level").click(function () {
      $(this).children("i").toggleClass("fa-angle-right fa-angle-down");
      $(this).siblings("div.dropdown-container").toggleClass("show");
    });

    $(".shop-button").click(function () {
      $(".dropdown-container-desktop").toggleClass("d-none");
    });

    $(document).on("click", function (event) {
      var trigger = $(".shop-button")[0];
      var dropdown = $(".dropdown-container-desktop");
      if (
        dropdown !== event.target &&
        !dropdown.has(event.target).length &&
        trigger !== event.target
      ) {
        $(".dropdown-container-desktop").addClass("d-none");
      }
    });
  });

  // Mobile search menu
  $(document).ready(function () {
    $("#mobile-search-btn").click(function () {
      $("#searchfield").toggleClass("show-search");
      $("#overlay").toggleClass("show-overlay");
      $("#searchfield").toggleClass("d-flex");
      $("body").toggleClass("overflow-y-hidden");
    });

    $(".close").click(function () {
      $("#searchfield").removeClass("show-search");
      $("#overlay").removeClass("show-overlay");
      $("#searchfield").removeClass("d-flex");
      $("body").removeClass("overflow-y-hidden");
    });
  });

  $(document).ready(function () {
    // Optimalisation: Store the references outside the event handler:
    var $window = $(window);

    function checkWidth() {
      //close the sidebar menu automatically
      var windowsize = $window.width();
      if (windowsize > 440) {
        //if the window is greater than 440px wide then turn on jScrollPane..
        $(".main").removeClass("open");
        $(".menu").removeClass("open");
        $("body").removeClass("overflow-y-hidden");
      }
    }
    // Execute on load
    checkWidth();
    // Bind event listener
    $(window).resize(checkWidth);

    function closeDropdownMenu() {
      //close the dropdown menu automatically
      var windowsize = $window.width();
      if (windowsize < 992) {
        //if the window is greater than 440px wide then turn on jScrollPane..
        $(".dropdown-container-desktop").removeClass("d-flex");
      }
    }
    // Execute on load
    closeDropdownMenu();
    // Bind event listener
    $(window).resize(closeDropdownMenu);
  });
})(jQuery);

$(document).ready(function () {
  $("#top-banner-notify").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 5000,
    arrows: false,
  });
});
