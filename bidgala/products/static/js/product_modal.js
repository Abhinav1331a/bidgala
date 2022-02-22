
/*function showContent(contentIndex){
        var i;
        var tabButtons = document.querySelectorAll(".btn__tab");
        var tabContent = document.querySelectorAll(".tab");

        for(i = 0; i < tabButtons.length; i++){
            tabButtons[i].style.backgroundColor = "";
        }
        tabButtons[contentIndex].style.backgroundColor = "#F3F3F3";

        tabContent.forEach(function (node){
            node.style.display = "none";
        });
        tabContent[contentIndex].style.display = "block";
        tabContent[contentIndex].style.backgroundColor = "#F3F3F3";

}

showContent(0);*/


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
/*$('#productModal').on('show.bs.modal', function () {
    $(this).find('.modal-body').css({
        width:'auto', //probably not needed
        height:'auto', //probably not needed
        'max-height':'100%'
    });
});

$( "#t2" ).on('click', function (e){

});

 */


/*Modal*/

$(document).ready(function () {
    var host_name = window.location.host;
    var protocol = window.location.protocol;
    $(".showProduct").on('click', function (e) {
        e.preventDefault();
        let path = $(this).attr('href');
        const pathArray = path.split('/');
        let product_id = pathArray[pathArray.length - 2];
        let profilePath = $(this).siblings('h6').find('#usernameData').attr('href');

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
                $('.carousel-indicators').append($('<li data-target="#carouselProductControls" data-slide-to="0" class="active" aria-current="true" style="width: 100px;"><img class="d-block w-100 indicator-img" src='+ obj_m.image +'></li>'));
                for (let j = 0; j < arr.length; j++) {
                    $('.carousel-indicators').append($('<li data-target="#carouselProductControls" data-slide-to='+ (j+1) + " " +'aria-current="true" style="width: 100px;"><img class="d-block w-100 indicator-img" src='+ arr[j] +'></li>'));
                }
                /*$('.carousel-inner').append($('<div class="carousel-item active"><img class="d-block w-100" src='  + obj_m.image + '></div>'));*/
                $('.carousel').carousel();

                /*('.carousel-item.active').prepend($('<img>',{
                    class: 'd-block w-100',
                    src: obj_m.image,
                    alt: 'new_preview'
                }));


                 /*alert(imgs.join('\n'));*/
                if ($(window).width() < 992) {
                    $(".col").prop("onclick", null).off("click");
                }

                $('#artTitle').text(obj_m.art_title);
                $('#artCategory').text('');
                $('#artistName').text('by '+obj_m.owner_first_name + ' ' + obj_m.owner_last_name);
                $('#artistName').attr('href',profilePath);
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

                $('get_shipping_price').text(($("#shipping_prices").val()));

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
                    //$('#purchase-btn').attr('href', product_view_page);
                    $('#purchase-btn').on('click', function(evt){
                        location.href = product_view_page + "?showModal=1";
                    });
                    /*$('#purchase-btn').on('click', function (event) {
                        event.preventDefault();
                        window.open(product_view_page + '#purchase-review-modal', '');
                    });
                    $(window).load(function () {
                        $(window.location.hash).modal("show");
                    });*/
                }


                $('.full-details').attr('href', protocol + "//" + host_name + "/art/product_view/" + product_id);
                /*$.each(obj_m, function (i, item) {
                    // build your html here and append it to your .modal-body
                    if( item.match(/\.(jpe?g|png|gif)$/) && (i.hasOwnProperty('image'))){
                        imgs.push(item);
                    }
                });*/
               /* $('#p-image').attr('src', obj_m.image);
                document.getElementsByClassName("product-name mb-2 pb-2").innerHTML= "<small>"+ obj_m.art_title " - " {{product.art_obj.first_name}} {{product.art_obj.last_name}}</small>";
*/
                $("#productModal").modal();


            }
        })
    });

    $('#productModal').on('hidden', function() {
        clear()
    });
});


