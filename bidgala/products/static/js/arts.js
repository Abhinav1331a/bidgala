$(document).ready(function () {

  $("#clearPrice").on("click", function() {
    $('input[name="price"]').prop('checked', false);
    $('input[name="price"]').trigger('change');
  });

  $(".grid")
    .imagesLoaded()
    .done(function () {
      $(".grid").masonry({
        itemSelector: ".grid-item",
        columnWidth: ".grid-sizer",
        horizontalOrder: true,
        gutter: 15,
        percentPosition: true,
        transitionDuration: 0,
      });
    });
});

//javascript to handle "sort-dropdown"
const dropdown = document.querySelector('.sort-dropdown');
const dropdownContent = dropdown.querySelector('.sort-dropdown-content');
const dropdownButtonText = dropdown.querySelector('.button-text');
const defaultSelection = dropdownContent.querySelector('#default-sort');
const lowestSelection = dropdownContent.querySelector('#lowest-first');
const highestSelection = dropdownContent.querySelector('#highest-first');
const defaultCheck = dropdownContent.querySelector('.default-check');
const lowestCheck = dropdownContent.querySelector('.lowest-check');
const highestCheck = dropdownContent.querySelector('.highest-check');
dropdown.addEventListener('click', function(event) {
    event.preventDefault();
    dropdownContent.style.display = 'block';
    const setDropdown = (sort, defaultFontWeight, lowestFontWeight, highestFontWeight, defCheck, lowCheck, highCheck) => {
        dropdownButtonText.textContent = sort;
        defaultSelection.style.fontWeight = defaultFontWeight;
        lowestSelection.style.fontWeight = lowestFontWeight;
        highestSelection.style.fontWeight = highestFontWeight;
        defaultCheck.style.visibility = defCheck;
        lowestCheck.style.visibility = lowCheck;
        highestCheck.style.visibility = highCheck;
        dropdownContent.style.display = 'none';
    }
    if (event.target.id === 'default-sort') setDropdown('Default', 'bold', 'normal', 'normal', 'visible', 'hidden', 'hidden');
    else if (event.target.id === 'lowest-first') setDropdown('Price: Lowest', 'normal', 'bold', 'normal', 'hidden', 'visible', 'hidden');
    else if (event.target.id === 'highest-first') setDropdown('Price: Highest', 'normal', 'normal', 'bold', 'hidden', 'hidden', 'visible');
})
document.addEventListener('click', function(event) {
    if (event.target.closest('.sort-dropdown')) return;
    dropdownContent.style.display = 'none';
})
//javascript to handle "sort-dropdown"

$(document).ready(function () {
  $("#filter").click(function () {
      $("#sidebar").toggleClass("sidebar-open");
      $("#overlay-arts").toggleClass("show-overlay-arts");
      $('body').toggleClass("overflow-y-hidden");
  });

  $(".close").click(function () {
      $("#sidebar").removeClass("sidebar-open");
      $("#overlay-arts").removeClass("show-overlay-arts");
      $('body').removeClass("overflow-y-hidden");
  });



});
function openFeatures(evt, feature){
  var i, boxcontent, collinks;
  boxcontent = document.getElementsByClassName("box");
  for (i = 0; i < boxcontent.length; i++) {
    boxcontent[i].style.display = "none";
  }
  collinks = document.getElementsByClassName("col");
  for (i = 0; i < collinks.length; i++) {
    collinks[i].className = collinks[i].className.replace(" active", "");
  }
  document.getElementById(feature).style.display = "block";

  evt.currentTarget.className+= " active";
}

$(document).ready(function () {
  var is_active_request = true;
  var page = 1;
  var category = [];
  var subcategory = [];
  var style = [];
  var color = [];
  var sort_by = "df" //This is a global variable. Please make changes accordingly
  var min_price = "";
  var min_price_custom = "";
  var max_price_custom = "";
  var measurement_unit = "";
  var width_min = "";
  var width_max = "";
  var height_min = "";
  var height_max = "";
  var depth_min = "";
  var depth_max = "";
  var can_scroll_to_load = true;
  var host_name = window.location.host;
  var protocol = window.location.protocol;

  $(".filter_product_section").on("click", ".fav-product", function () {
    id = this.id.replace("fav-", "");
    current = $(this);
    var token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
      url: "/art/favourite/",
      type: "POST",
      data: {
        csrfmiddlewaretoken: token,
        id: id,
      },
      headers: {
        "X-CSRF-Token": token,
      },

      success: function (result) {
        if (result.status == "added") {
          current.empty();
          current.html('<i class="fas fa-heart" style="color:black"></i>');
        } else if (result.status == "removed") {
          current.empty();
          current.html('<i class="far fa-heart" style="color:black"></i>');
        }
      },

      error: function (XMLHttpRequest, textStatus, errorThrown) {},
    });
  });

  function range(start, stop, step) {
    if (typeof stop == "undefined") {
      // one param defined
      stop = start;
      start = 0;
    }

    if (typeof step == "undefined") {
      step = 1;
    }

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
      return [];
    }

    var result = [];
    for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
      result.push(i);
    }

    return result;
  }

  function noScroll() {
    //get current scroll position
    var xPosition =
      window.scrollX || window.pageXOffset || document.body.scrollLeft;
    var yPosition =
      window.scrollY || window.pageYOffset || document.body.scrollTop;

    window.scrollTo(xPosition - xPosition / 2, yPosition - yPosition / 2);
  }

  async function loadMore() {
    collectData();
    page = page + 1;
    // $("#preloader-active").css("display", "block");
    getData(page, false, category, subcategory, style, color, min_price,sort_by,min_price_custom,max_price_custom,measurement_unit,width_min,width_max,height_min,height_max,depth_min,depth_max);

    // await new Promise(resolve => setTimeout(resolve, 2000));

    window.onscroll = function () {};
    // $("#preloader-active").css("display", "none");
    document.body.style.overflow = "visible";
  }

  function getData(
    page_number,
    remove_existing,
    category_selected,
    subcategory_selected,
    style_selected,
    color_selected,
    min_price_selected,
    sort_by_,
    min_price_custom_,
    max_price_custom_,
    measurement_unit_,
    width_min_,
    width_max_,
    height_min_,
    height_max_,
    depth_min_,
    depth_max_
  ) {
    is_active_request = false;
    var token = $("input[name='csrfmiddlewaretoken']").val();
    var loc = window.location.href
    

    $.ajax({
      url: "/art/filter-art",
      type: "POST",
      data: {
        csrfmiddlewaretoken: token,
        category: JSON.stringify(category_selected),
        subcategory: JSON.stringify(subcategory_selected),
        style: JSON.stringify(style_selected),
        color: JSON.stringify(color_selected),
        min_price: min_price_selected,
        page: page_number,
        is_curator:loc.includes("curator"),
        sort_by:sort_by_,
        min_price_custom:min_price_custom_,
        max_price_custom:max_price_custom_,
        measurement_unit:measurement_unit_,
        width_min:width_min_,
        width_max:width_max_,
        height_min:height_min_,
        height_max:height_max_,
        depth_min:depth_min_,
        depth_max:depth_max_,
      },
      headers: {
        "X-CSRF-Token": token,
      },

      success: function (result) {
       
        // var path_arr = []
        // for (var a = 0; a < category_selected.length; a++) {
        //   if (path_arr.indexOf(category_selected[a]) === -1){
        //     path_arr.unshift(category_selected[a])
        //   }
        //   // path_arr.push(category_selected[a])
        // }
        // console.log(path_arr)
        // console.log(category_selected)
        // if (!($('#path').html().includes(path_arr[0]))){
        //   $('#path').append(path_arr[0] + ' / ')
        // }
        // // $('#path').append(path_arr[0])

        if (remove_existing) {
          $(".grid").masonry("remove", $(".grid").find(".grid-item"));
          $(".grid").empty();
        }

        if (JSON.parse(JSON.stringify(result)) == "[]") {
          can_scroll_to_load = false;
          if ($(".grid").html() == "") {
            $(".grid").append(
              "<div class='alert alert-primary text-center' role='alert' style='width:100%'>No match found</div>"
            );
          }
        } else {
          can_scroll_to_load = true;

          num_avail_objects = JSON.parse(JSON.stringify(result)).length;

          parsed_result = JSON.parse(JSON.stringify(result));

          var col_str = "";

          for (var j = 0; j < parsed_result.length; j++) {
            product_str = "";

            obj_ = parsed_result[j];

            var measure_type = "";

            if (obj_ == null) {
              continue;
            }


            if (obj_.fields.dim_measurement == "m") {
              measure_type = "m";
            } else if (obj_.fields.dim_measurement == "cm") {
              measure_type = "cm";
            } else {
              measure_type = "inches";
            }

            var depth = "";
            if (obj_.fields.depth != null) {
              depth = " x " + obj_.fields.depth + "D";
            }

            fav_html = "";
            artist_full_name = obj_.fields.first_name + ' ' + obj_.fields.last_name;

            if (obj_.fields.fav == true && obj_.authenticated == true) {
              fav_html =
                  '<a  id="fav-' +
                  obj_.pk +
                  '" class="fav-product"><i class="fas fa-heart"></i> </a>';
            } else if (obj_.fields.fav == false && obj_.authenticated == true) {
              fav_html =
                  '<a  id="fav-' +
                  obj_.pk +
                  '" class="fav-product"><i class="far fa-heart"></i> </a>';
            } else {
              fav_html =
                  '<a href="#" data-toggle="modal" data-target="#loginModal"><i class="far fa-heart"></i></a>';
            }

            product_str =
                "<a href='" +
                "/art/product_view/" +
                obj_.pk +
                // "' target='blank'>" +
                "' class='showProductDyn' data-bs-toggle='modal' data-bs-target='#productModal' id='someid'>" +
                "<img src='" +
                obj_.fields.img_host_url +
                obj_.fields.image +
                obj_.fields.img_optimize_param +
                "' alt=''>" +
                "<h6 class='mt-2 mb-1 text-truncate font-weight-bold dynamic' data-username='" + obj_.fields.username + "'>" +
                artist_full_name + "</h6>"
                +
                "<small><i>" +
                obj_.fields.art_title +
                "</i></small><br/>" +
                "<small class='text-muted'>$" +
                parseInt(obj_.fields.price).toLocaleString() +
                "</small><br/>" +
                "<div class='w-100 d-flex justify-content-between'>" +
                "<small class='text-muted'>" +
                obj_.fields.width +
                "W x </small>" +
                "<small class='text-muted'>" +
                obj_.fields.height +
                "H</small>" +
                "<small class='text-muted'>" +
                depth +
                "</small>" +
                " " +
                "<small class='text-muted'>" +
                measure_type +
                "</small>" +
                fav_html +
                "</div>" +
                "<div class='modal fade' id='productModal' tabindex='-1' aria-labelledby='productModalLabel' aria-hidden='true'>" +
                "<div class='modal-dialog modal-dialog-centered modal-dialog-scrollable modal-lg'>" +
                "<div class='modal-content'>"+
                "<div class='modal-header border-0'>" +
                "<button type='button' class='close' data-dismiss='modal' aria-label='Close'>"+
                "<span aria-hidden='true'>&times;</span>"+
                "</button>"+
                "</div>" +
                "<div class='modal-body row' id='modalBodyDyn'>" +
                "</div>" +
                "</div>"+
                "</div>" +
                "</div>" +
                "</a>";

            var $grid = $(".grid").imagesLoaded(function () {
              $grid.masonry({
                itemSelector: ".grid-item",
                columnWidth: ".grid-sizer",
                horizontalOrder: true,
                gutter: 15,
                percentPosition: true,
                transitionDuration: 0,
              });
            });

            $(".grid").append('<div class="grid-sizer"></div>');

            product_str = '<div class="grid-item">' + product_str + "</div>";

            $newElems = $(product_str);

            $grid.append($newElems).masonry("reloadItems").masonry("layout");
          }

          //the product popup modal rendering
          const pic1 = "static/img/free_returns.png"
          var purBtn ="<div class=\"col-sm-6\">\n" +
              "      <div id=\"carouselProductControls\" class=\"carousel slide\" data-ride=\"carousel\" data-bs-touch=\"false\" data-bs-interval=\"false\">\n" +
              "          <div class=\"carousel-inner\">\n" +
              "              <!--div class=\"carousel-item active\">\n" +
              "              </div-->\n" +
              "\n" +
              "              <div class=\"carousel-item\">\n" +
              "              </div>\n" +
              "\n" +
              "              <div class=\"carousel-item\">\n" +
              "              </div>\n" +
              "\n" +
              "          </div>\n" +
              "          <a class=\"carousel-control-prev\" href=\"#carouselProductControls\" role=\"button\" data-slide=\"prev\">\n" +
              "              <span class=\"carousel-control-prev-icon\" aria-hidden=\"true\"></span>\n" +
              "              <span class=\"sr-only\">Previous</span>\n" +
              "          </a>\n" +
              "          <a class=\"carousel-control-next\" href=\"#carouselProductControls\" role=\"button\" data-slide=\"next\">\n" +
              "              <span class=\"carousel-control-next-icon\" aria-hidden=\"true\"></span>\n" +
              "              <span class=\"sr-only\">Next</span>\n" +
              "          </a>\n" +
              "<ol class=\"carousel-indicators\"</ol>"+
              "      </div>\n" +
              "  </div>\n" +
              "  <div class=\"col-sm-6 right\">\n" +
              "\n" +
              "      <div class=\"tabContainer\">\n" +
              "                    <div class=\"buttonContainer\">\n" +
              "                        <!--button class=\"btn__tab\" onclick=\"showContent(0)\">Current</button-->\n" +
              "\n" +
              "\n" +
              "                        <!--button class=\"btn__tab\" onclick=\"showContent(1)\">More from {{ product.art_obj.owner.user.first_name}} {{ product.art_obj.owner.user.last_name }}</button-->\n" +
              "                    </div>\n" +
              "\n" +
              "                    <div class=\"tab\" id=\"t1\">\n" +
              "                        <h1 id=\"artTitle\"></h1>\n" +
              "                        <p id=\"artCategory\" class=\"art-category\"></p>\n" +
              "                        <a id=\"artistName\" class=\"art-artist\" style=\"text-decoration: underline\"></a>\n" +
              "                        <p id=\"artState\" class=\"art-state\"></p>\n" +
              "                        <p id=\"artPrice\" class=\"art-price\" style=\"font-weight: bold\"></p>\n" +
              "<div class=\"shipping\">\n" +
              "                <p><strong>+ USD <span id=\"get_shipping_price\"></span></strong>Shipping: </p>\n" +
              "                <select class=\"custom-select\" id=\"shipping_prices\">\n" +
              "\n" +
              "                </select>\n" +
              "            </div>" +
              "                        <div class=\"box\" id=\"sb1\">\n" +
              "                            <h2>Satisfaction Guaranteed</h2>\n" +
              "                            <p>Our 7-day, no questions asked, 100% money-back guarantee allows you to purchase with the total peace of mind.</p>\n" +
              "                        </div>\n" +
              "                        <div class=\"box\" id=\"sb2\">\n" +
              "                            <h2>Secure Payments</h2>\n" +
              "                            <p>All payments are 100% secured through our trusted partner Stripe.</p>\n" +
              "                        </div>\n" +
              "                        <div class=\"box\" id=\"sb3\">\n" +
              "                            <h2>Contact Us</h2>\n" +
              "                            <p>Purchase with confidence, knowing our Support Team is always here to help you navigate the experiences.</p>\n" +
              "                        </div>\n" +
              "                        <div class=\"box\" id=\"sb4\">\n" +
              "                            <h2>Support The Artist</h2>\n" +
              "                            <p>Purchase this piece directly from the artist, helping them earn a living doing what they love.</p>\n" +
              "                        </div>\n" +
              "                        <div class=\"container feature\">\n" +
              "                            <div class=\"row feature\">\n" +
              "                                <div class=\"col\" onclick=\"openFeatures(this, 'sb1' );\" id='free-returns'>\n" +
              "                                    <p>Free Returns</p>\n" +
              "                                </div>\n" +
              "                                <div class=\"col\" onclick=\"openFeatures(this, 'sb2' );\" id='secure'>\n" +
              "                                    <p>Secure Payment</p>\n" +
              "                                </div>\n" +
              "                                <div class=\"col\" onclick=\"openFeatures(this, 'sb3' );\" id='support'>\n" +
              "                                    <p>24/7 Support</p>\n" +
              "                                </div>\n" +
              "                                <div class=\"col\" onclick=\"openFeatures(this, 'sb4' );\" id='art-support'>\n" +
              "                                    <p>Support Artists</p>\n" +
              "                                </div>\n" +
              "                            </div>\n" +
              "                        </div>\n";
          if(currentUser) {

            purBtn = purBtn + "<div class=\"btn-group-vertical\">\n" +
                  "                            <a href=\"#\" class =\"art-info-button text-center\" style=\"color:white;\"\n" +
                  "                                    onmouseover=\"this.style.color='black'\" id=\"purchase-btn\"\n" +
                  "                                    onmouseout=\"this.style.color='white'\"\n" +
                  "                            >CONTINUE TO PURCHASE</a>\n" +
                  "\n" +
                  "                            <a href=\"#\" type=\"button\" class =\"art-info-button outlined text-center\" style=\"color:black;\"\n" +
                  "                               onmouseover=\"this.style.color='white'\" id=\"message_artist\"\n" +
                  "                               onmouseout=\"this.style.color='black'\"\n" +
                  "                            >MESSAGE ARTIST</a>\n" +
                  "                        </div>\n";
          }
          else {
            purBtn= purBtn + "<div class=\"btn-group-vertical\">\n" +
                "                            <button class=\"art-info-button text-center\" data-toggle=\"modal\" data-target=\"#loginModal\" style=\"color:white;\"\n" +
                "                                    onmouseover=\"this.style.color='black'\" id=\"purchase-btn\"\n" +
                "                                    onmouseout=\"this.style.color='white'\"\n" +
                "                                    onclick=\"$('#productModal').modal('toggle');\"\n" +
                "                            >CONTINUE TO PURCHASE</button>\n" +
                "\n" +
                "                            <button data-toggle=\"modal\" data-target=\"#loginModal\" class =\"art-info-button outlined text-center\" style=\"color:black;\"\n" +
                "                                    onmouseover=\"this.style.color='white'\" id=\"message_artist\"\n" +
                "                                    onmouseout=\"this.style.color='black'\"\n" +
                "                                    onclick=\"$('#productModal').modal('toggle');\"\n" +
                "                            >MESSAGE ARTIST</button>\n" +
                "                        </div>\n";
          }
          purBtn = purBtn +
              "<div class=\"container-details\">\n" +
              "                <a href=\"#\" class=\"full-details\" style=\"text-decoration: underline\">View full details</a>\n" +
              "            </div>"+
              "</div>\n" +
              "\n" +
              "      </div>\n" +
              "\n" +
              "  </div>\n" +
              "\n";

          document.getElementById("modalBodyDyn").innerHTML= purBtn;
          $('#free-returns').html(
              '<img src="/static/img/free_returns.png" alt="free-returns"><p>Free Returns</p>');
          $('#secure').html(
              '<img src="/static/img/secure_payments.png" alt="secure-payments"><p>Secure Payment</p>');

          $('#support').html(
              '<img src="/static/img/support.png" alt="support"><p>24/7 Support</p>');

          $('#art-support').html(
              '<img src="/static/img/artist_support.png" alt="artist-support"><p>Support Artists</p>');

          $(".showProductDyn").on('click', function (e){
            e.preventDefault();
            let path = $(this).attr('href');
            const pathArray = path.split('product_view/');
            let product_id = pathArray[pathArray.length - 1];
            let profilePath = $(this).find('h6').attr('data-username');

            $.ajax({
              type: "GET",
              url: protocol + "//" + host_name + "/art/api/product/" + product_id,
              success: function (resp) {

                const obj_m = resp;
                var arr = [];

                if (obj_m["additional_image_1"] != null) {
                  arr.push(obj_m["additional_image_1"]);
                }
                if (obj_m["additional_image_2"] != null) {
                  arr.push(obj_m["additional_image_2"]);
                }
                if (obj_m["additional_image_3"] != null) {
                  arr.push(obj_m["additional_image_3"]);
                }
                if (obj_m["additional_image_4"] != null) {
                  arr.push(obj_m["additional_image_4"]);
                }

                $('.carousel-inner').empty();
                $('.carousel-inner').append($('<div class="carousel-item active"><img class="d-block w-100" src=' + obj_m.image + '></div>'));
                for (let j = 0; j < arr.length; j++) {
                  $('.carousel-inner').append($('<div class="carousel-item"><img class="d-block w-100" src=' + arr[j] + '></div>'));
                }

                $('.carousel-indicators').empty();
                $('.carousel-indicators').append($('<li data-target="#carouselProductControls" data-slide-to="0" class="active" aria-current="true" style="width: 100px;"><img class="d-block w-100" src='+ obj_m.image +'></li>'));
                for (let j = 0; j < arr.length; j++) {
                  $('.carousel-indicators').append($('<li data-target="#carouselProductControls" data-slide-to='+ (j+1) + " " + 'aria-current="true" style="width: 100px;"><img class="d-block w-100" src='+ arr[j] +'></li>'));
                }

                /*$('.carousel-inner').append($('<div class="carousel-item active"><img class="d-block w-100" src='  + obj_m.image + '></div>'));*/
                $('.carousel').carousel();

                if ($(window).width() < 992) {
                  $(".col").prop("onclick", null).off("click");
                }

                $('#artTitle').text(obj_m.art_title);
                $('#artCategory').text("");
                $('#artistName').text('by '+obj_m.owner_first_name + ' ' + obj_m.owner_last_name);
                $('#artistName').attr('href', '/p/' + profilePath);
                $('#artPrice').text('USD ' + obj_m.price);

                $('#shipping_prices').empty();
                for (var ky in obj_m) {
                  if (ky.includes('shipping_price') && !(ky.includes('show'))) {
                    let tmpArr = ky.split('_');

                    if (tmpArr[2] === 'aunz') {
                      $('#shipping_prices').append($('<option value=' + obj_m[ky] + '>AUSTRALIA/NEW ZEALAND</option>'));
                    } else {
                      $('#shipping_prices').append($('<option value=' + obj_m[ky] + '>' + tmpArr[2].toUpperCase() + '</option>'));
                    }
                  }
                }
                $("#shipping_prices").val($("#shipping_prices option:first").val());
                $("#get_shipping_price").text($("#shipping_prices").val() + ' ');
                $("#shipping_prices").on('change', function() {
                  $("#get_shipping_price").text($("#shipping_prices").val() + ' ');
                });

                $('#message_artist').attr('href',protocol + "//" + host_name + "/messages/" + obj_m.owner_message_id); /* doesn't check if message is to yourself */
                if (obj_m.is_framed_or_hang === "yes") {
                  $('#artState').text("Ready To Hang");
                }



                $('#productModal').on('show.bs.modal', function () {
                  $(this).find('.modal-body').css({
                    width:'auto', //probably not needed
                    height:'auto', //probably not needed
                    'max-height':'100%'
                  });
                });

                $( "#t2" ).on('click', function (e){

                });

                if($('#purchase-btn').attr('href') !== undefined) {
                  let product_view_page = protocol + "//" + host_name + "/art/product_view/" + product_id;
                  $('#purchase-btn').on('click', function(evt){
                    window.location.href = product_view_page + "?showModal=1";
                  });
                }
                $('.full-details').attr('href', protocol + "//" + host_name + "/art/product_view/" + product_id);

                $("#productModal").modal();


              }
            })
          });

          function openFeatures(evt, feature){
            var i, boxcontent, collinks;
            boxcontent = document.getElementsByClassName("box");
            for (i = 0; i < boxcontent.length; i++) {
              boxcontent[i].style.display = "none";
            }
            collinks = document.getElementsByClassName("col");
            for (i = 0; i < collinks.length; i++) {
              collinks[i].className = collinks[i].className.replace(" active", "");
            }
            document.getElementById(feature).style.display = "block";

            evt.currentTarget.className+= " active";
          };

          $('#productModal').on('hidden', function() {
            clear()
          });

          // var final_row = "<div class='row_'>" + col_str + "</div>"
          //  $(".filter_product_section").append(final_row)

          is_active_request = true;
        }
      },

      error: function (XMLHttpRequest, textStatus, errorThrown) {
        $(".filter_product_section").empty();
        $(".filter_product_section").append(
          "<div class='alert alert-danger text-center' role='alert' style='width:100%'>Something went wrong.</div>"
        );
      },
    });
  }

  function collectData(obj) {
    category = [];
    subcategory = [];
    style = [];
    color = [];
    min_price = "";
    min_price_custom = "";
    max_price_custom = "";
    measurement_unit = "";
    width_min = "";
    width_max = "";
    height_min = "";
    height_max = "";
    depth_min = "";
    depth_max = "";

    // if (obj && obj.attr("name") == "filter-option-color") {
    //   if (obj.is(":checked")) {
    //     obj.parent().removeClass("gray-border").addClass("selected-border");
    //   } else {
    //     obj.parent().removeClass("selected-border").addClass("gray-border");
    //   }
    // }


    $('input[name="category"]').each(function () {
      if (this.checked) {
        category.push($(this).attr("data-value"));
      }
    });


    // sort_by = $('input[name="sort-by"]:checked').val();

    measurement_unit = $('input[name="measure-unit"]:checked').val();


    min_price_custom = $('input[id="min-price-custom"]').val();

    max_price_custom = $('input[id="max-price-custom"]').val();

    width_min = $('input[id="min-width"]').val();
    width_max = $('input[id="max-width"]').val();

    height_max = $('input[id="max-height"]').val();
    height_min = $('input[id="min-height"]').val();

    depth_max = $('input[id="max-depth"]').val();
    depth_min = $('input[id="min-depth"]').val();

    $('input[name="subcategory"]').each(function () {
      if (this.checked) {
        subcategory.push($(this).attr("data-value"));
      }
    });

    $('input[name="style"]').each(function () {
      if (this.checked) {
        style.push($(this).attr("data-value"));
      }
    });

    $('input[name="filter-option-color"]').each(function () {
      if (this.checked) {
        color.push($(this).attr("color"));
      }
    });

    $('input[name="price"]').each(function () {
      if (this.checked) {
        min_price = $(this).attr("data-value");
      }
    });
  }

  $('input[name="sort-by"]').change(function() {
    sort_by = $(this).val()
    collectData($(this));
    page = 1;
    getData(1, true, category, subcategory, style, color, min_price,sort_by,min_price_custom,max_price_custom,measurement_unit,width_min,width_max,height_min,height_max,depth_min,depth_max);
  })

  $(
    'input[name="category"],input[id="min-width"],input[id="max-width"], input[id="max-height"], input[id="min-height"],input[id="max-depth"], input[id="min-depth"],input[name="measure-unit"], input[id="max-price-custom"], input[id="min-price-custom"],input[name="subcategory"], input[name="subcategory"], input[name="style"], input[name="filter-option-color"], input[name="price"]'
  ).change(function () {


    current_context = $(this);
    collectData($(this));
    page = 1;
    getData(1, true, category, subcategory, style, color, min_price,sort_by,min_price_custom,max_price_custom,measurement_unit,width_min,width_max,height_min,height_max,depth_min,depth_max);
  });


  $(
    '#default-sort, #highest-first, #lowest-first'
  ).click(function () {

    current_context = $(this);
    sort_by = current_context.data('value')
    collectData($(this));
    page = 1;
    getData(1, true, category, subcategory, style, color, min_price,sort_by,min_price_custom,max_price_custom,measurement_unit,width_min,width_max,height_min,height_max,depth_min,depth_max);
  });


  $(window).bind("scroll", function () {
    if (
      window.innerHeight + window.scrollY >=
      document.body.offsetHeight * 0.85
    ) {
      if (can_scroll_to_load == true && is_active_request == true) {
        document.body.style.overflow = "hidden";
        window.addEventListener("scroll", noScroll);
        loadMore(null);
        window.removeEventListener("scroll", noScroll);
      }
    }
  });

  window.onload = function () {
    document.body.style.overflow = "visible";

    if (window.innerHeight > 992) {
      loadMore();
    }
  };

    $(document.body).on('click', '.dynamic', function(event) {
       window.location = "/p/" + $(this).data('username');
    })
});