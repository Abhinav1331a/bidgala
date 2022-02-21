
$( document ).ready(function() {
  $('.grid').imagesLoaded().done(function() {
    $('.grid').masonry({
    itemSelector: '.grid-item',
    columnWidth: '.grid-sizer',
    horizontalOrder: true,
    gutter: 15,
    percentPosition: true,
    
    
  });
});
});

