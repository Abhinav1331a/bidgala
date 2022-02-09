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
              protocol +
              "//" +
              host_name +
              "/art/product_view/" +
              obj_.pk +
              // "' target='blank'>" +
              "' >" + 
              "<img src='" +
              obj_.fields.img_host_url +
              obj_.fields.image +
              obj_.fields.img_optimize_param +
              "' alt=''>" + 
              "<h6 class='mt-2 mb-1 text-truncate font-weight-bold dynamic' data-username='"+obj_.fields.username+"'>"+artist_full_name+"</h6>"
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
