var cropper;
var additional_img_1 = "";
var additional_img_2 = "";
var additional_img_3 = "";
var additional_img_4 = "";


$('.price_toggle').change(function() {
    var id = $(this).attr('id');
    var input_id = $(this).attr('data-parent');
    if (!$('#' + id).is(":checked")) {
        $("#" + input_id).prop('disabled', true);
        $("#" + input_id).css('background-color', '#ced4da');


    } else {
        $("#" + input_id).prop('disabled', false);
        $("#" + input_id).css('background-color', '#ffffff');
    }
});
 
function readURL(input) {

    if (input.id == 'pic1') {
        id = "#img_display_1"
    } else if (input.id == 'pic2') {
        id = "#img_display_2"
    } else if (input.id == 'pic3') {
        id = "#img_display_3"
    } else if (input.id == 'pic4') {
        id = "#img_display_4"
    }

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            $(id).attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);

        reader.onloadend = function() {

            if (input.id == 'pic1') {
                additional_img_1 = reader.result;
            } else if (input.id == 'pic2') {
                additional_img_2 = reader.result;
            } else if (input.id == 'pic3') {
                additional_img_3 = reader.result;
            } else if (input.id == 'pic4') {
                additional_img_4 = reader.result;
            }
        }
    }
};


$('#onClose').click(function(event) {

    location.reload();

});

$(document).ajaxStart(function() {
    $("#preloader-active").css("display", "block");
});



$(document).ajaxComplete(function() {
    $("#preloader-active").css("display", "none");
});



var input_tag = document.querySelector('textarea[name=tags2]'),
    tagify = new Tagify(input_tag, {
        pattern: /^.{0,20}$/, // Validate typed tag(s) by Regex. Here maximum chars length is defined as "20"
        delimiters: ",| ", // add new tags when a comma or a space character is entered
        keepInvalidTags: false, // do not remove invalid tags (but keep them marked as invalid)
        editTags: 1, // single click to edit a tag
        transformTag: transformTag,
        backspace: "edit",
        placeholder: "type tags",
        duplicates: false,
        originalInputValueFormat: valuesArr => valuesArr.map(item => item.value).join(','),
        dropdown: {
            enabled: 3,
        }
    })
    // generate a random color (in HSL format, which I like to use)
function getRandomColor() {
    function rand(min, max) {
        return min + Math.random() * (max - min);
    }
    var h = rand(1, 360) | 0,
        s = rand(40, 70) | 0,
        l = rand(65, 72) | 0;
    return 'hsl(' + h + ',' + s + '%,' + l + '%)';
}

function transformTag(tagData) {
    tagData.style = "--tag-bg:" + getRandomColor();
    if (tagData.value.toLowerCase() == 'shit')
        tagData.value = 's✲✲t'
}






$(window).load(function() {

    if (localStorage.getItem("title") != undefined || localStorage.getItem("title") !== null) {
        $('#artname').prop('value', localStorage.getItem("title"));

    }

    if (localStorage.getItem("desc") != undefined || localStorage.getItem("desc") !== null) {
        $('#artdescription').val(localStorage.getItem("desc")).trigger('change');
    }

    if (localStorage.getItem("height") != undefined || localStorage.getItem("height") !== null) {
        $('#height').val(localStorage.getItem("height"))
    }

    if (localStorage.getItem("width") != undefined || localStorage.getItem("width") !== null) {
        $('#width').val(localStorage.getItem("width"))
    }

    if (localStorage.getItem("depth") != undefined || localStorage.getItem("depth") !== null) {
        $('#depth').val(localStorage.getItem("depth"))
    }

    if (localStorage.getItem("price") != undefined || localStorage.getItem("price") !== null) {
        $('#price').val(localStorage.getItem("price"))
    }

    if (localStorage.getItem("shipcanada") != undefined || localStorage.getItem("shipcanada") !== null) {
        $('#shipcanada').val(localStorage.getItem("shipcanada"))
    }

    if (localStorage.getItem("shipus") != undefined || localStorage.getItem("shipus") !== null) {
        $('#shipus').val(localStorage.getItem("shipus"))
    }

    if (localStorage.getItem("shipuk") != undefined || localStorage.getItem("shipuk") !== null) {
        $('#shipuk').val(localStorage.getItem("shipuk"))
    }

    if (localStorage.getItem("shipasia") != undefined || localStorage.getItem("shipasia") !== null) {
        $('#shipasia').val(localStorage.getItem("shipasia"))
    }

    if (localStorage.getItem("shipeurope") != undefined || localStorage.getItem("shipeurope") !== null) {
        $('#shipeurope').val(localStorage.getItem("shipeurope"))
    }

    if (localStorage.getItem("shipother") != undefined || localStorage.getItem("shipother") !== null) {
        $('#shipother').val(localStorage.getItem("shipother"))
    }

    if (localStorage.getItem("shipaunz") != undefined || localStorage.getItem("shipaunz") !== null) {
        $('#shipaunz').val(localStorage.getItem("shipaunz"))
    }

});


$('#upload_image').on('change', function() {


    $("#upload_image").attr("disabled", "disabled");

    var reader = new FileReader();
    reader.onload = function(event) {


        $("#imagecrop").attr(
            'src', event.target.result
        );
        // var data = document.querySelector('#data');
        var minCroppedWidth = 1000;
        var minCroppedHeight = 1000;
        var maxCroppedWidth = 4096 * 8;
        var maxCroppedHeight = 4096 * 8;

        const image = document.getElementById('imagecrop');
        cropper = new Cropper(image, {
            viewMode: 3,
            zoomable: true,
            zoom: -1,
            data: {
                width: (minCroppedWidth + maxCroppedWidth) / 2,
                height: (minCroppedHeight + maxCroppedHeight) / 2,
            },
            crop: function(event) {
                var width = event.detail.width;
                var height = event.detail.height;

                if (
                    width < minCroppedWidth ||
                    height < minCroppedHeight ||
                    width > maxCroppedWidth ||
                    height > maxCroppedHeight
                ) {
                    cropper.setData({
                        width: Math.max(minCroppedWidth, Math.min(maxCroppedWidth, width)),
                        height: Math.max(minCroppedHeight, Math.min(maxCroppedHeight, height)),
                    });
                }


            },

        });





    };

    $('#uploadimageModal').modal({
        backdrop: 'static',
        keyboard: false
    });


    reader.readAsDataURL(this.files[0]);
    $('#uploadimageModal').modal('show')
});


$("#artname").change(function() {
    localStorage.setItem("title", $('#artname').val());
});

$('#artdescription').change(function() {
    localStorage.setItem("desc", $('#artdescription').val());
});

$('#height').change(function() {
    localStorage.setItem("height", $('#height').val());
});

$('#width').change(function() {
    localStorage.setItem("width", $('#width').val());
});

$('#depth').change(function() {
    localStorage.setItem("depth", $('#depth').val());
});

$('#price').change(function() {
    localStorage.setItem("price", $('#price').val());
});

$('#shipcanada').change(function() {
    localStorage.setItem("shipcanada", $('#shipcanada').val());
});

$('#shipus').change(function() {
    localStorage.setItem("shipus", $('#shipus').val());
});

$('#shipuk').change(function() {
    localStorage.setItem("shipuk", $('#shipuk').val());
});

$('#shipasia').change(function() {
    localStorage.setItem("shipasia", $('#shipasia').val());
});

$('#shipeurope').change(function() {
    localStorage.setItem("shipeurope", $('#shipeurope').val());
});

$('#shipaunz').change(function() {
    localStorage.setItem("shipaunz", $('#shipaunz').val());
});

$('#shipother').change(function() {
    localStorage.setItem("shipother", $('#shipother').val());
});


$('.crop_image').click(function(event) {
    // $("#preloader-active").css("display", "block");
    var styles = '';
    var materials = '';
    
    var is_signed = $('input[name="signed_art"]:checked').val();
    var is_framed_ready = $('input[name="framed_ready"]:checked').val();
    
    
    $('.style_art').each(function() {
        if (this.checked === true) {
            styles = styles.concat($(this).val(), ',');
        }
    });

    $('.material_art').each(function() {
        if (this.checked === true) {
            materials = materials.concat($(this).val(), ',');
        }
    });


    if (cropper !== 'null' && cropper !== 'undefined')

        cropper.getCroppedCanvas().toBlob((blob) => {


        if ($("#artuploadform").valid()) {
            $('#forerrormessage').empty();
            if ($("#category").val().length != 0) {
                if ($('textarea[name="tags2"]').val().length != 0) {
                    if (!($('#shipcan').val() === "" && $('#shipus').val() === "" && $('#shipuk').val() === "" && $('#shipaunz').val() === "" && $('#shipasia').val() === "" && $('#shipeurope').val() === "" && $('#shipother').val() === "")) {
                        $("#preloader-active").css("display", "block");
                        let reader = new FileReader();
                        reader.readAsDataURL(blob);
                        var base64data;

                        
                        reader.onloadend = function() {
                            $("#preloader-active").css("display", "block");
                            console.log("hello")

                            $.ajax({
                                url: "/art/add-art",
                                type: "POST",
                                data: {
                                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
                                    "art_img": cropper.getCroppedCanvas().toDataURL("image/jpeg", 0.75),
                                    "color": $('#custom').val(),
                                    "color_1": $('#custom1').val(),
                                    "color_2": $('#custom2').val(),
                                    "color_3": $('#custom3').val(),
                                    "color_4": $('#custom4').val(),
                                    "title": $('#artname').val(),
                                    "desc": $('#artdescription').val(),
                                    "tags": $('textarea[name="tags2"]').val(),
                                    "height": $('#height').val(),
                                    "width": $('#width').val(),
                                    "depth": $('#depth').val(),
                                    "cat": $('#category').val(),
                                    "subcat": $('#subcategory').val(),
                                    "measure": $('#measure').val(),
                                    "price": $('#price').val(),
                                    "s_price_can": $('#shipcan').val(),
                                    "s_price_us": $('#shipus').val(),
                                    "s_price_uk": $('#shipuk').val(),
                                    "s_price_aunz": $('#shipaunz').val(),
                                    "s_price_asia": $('#shipasia').val(),
                                    "s_price_europe": $('#shipeurope').val(),
                                    "s_price_other": $('#shipother').val(),
                                    "show_price_can": $('#shipcan_toggle').is(":checked"),
                                    "show_price_us": $('#shipus_toggle').is(":checked"),
                                    "show_price_uk": $('#shipuk_toggle').is(":checked"),
                                    "show_price_aunz": $('#shipaunz_toggle').is(":checked"),
                                    "show_price_asia": $('#shipasia_toggle').is(":checked"),
                                    "show_price_europe": $('#shipeurope_toggle').is(":checked"),
                                    "show_price_other": $('#shipother_toggle').is(":checked"),
                                    "styles": styles.slice(0, -1),
                                    "materials": materials.slice(0, -1),
                                    "is_signed": is_signed,
                                    "is_framed_ready": is_framed_ready,
                                    "additional_img_1": additional_img_1,
                                    "additional_img_2": additional_img_2,
                                    "additional_img_3": additional_img_3,
                                    "additional_img_4": additional_img_4,


                                },
                                headers: {
                                    'X-CSRF-Token': $("input[name='csrfmiddlewaretoken']").val()
                                },
                                success: function(result) {
                                    $("#preloader-active").css("display", "none");

                                    if (result.status == 'success') {

                                       localStorage.setItem("title", "");
                                       localStorage.setItem("desc", "");
                                       localStorage.setItem("height", "");
                                       localStorage.setItem("width", "");
                                       localStorage.setItem("depth", "");
                                       localStorage.setItem("price", "");
                                       localStorage.setItem("shipcanada", "");
                                       localStorage.setItem("shipus", "");
                                       localStorage.setItem("shipuk","");
                                       localStorage.setItem("shipasia", "");
                                       localStorage.setItem("shipeurope", "");
                                       localStorage.setItem("shipaunz", "");
                                       localStorage.setItem("shipother", "");
                                        $('#forerrormessage').empty()
                                        $('#forerrormessage').append("<div class='alert alert-success'>" + "Art posted successfully." + "</div>").delay(2000).fadeOut(function() {
                                            $(this).empty();
                                            $(this).removeAttr('style');
                                        });
                                    }
                                    setTimeout(function() {
                                        location.reload();
                                    }, 1000);

                                },
                                error: function(request, ajaxOptions, thrownError) {
                                    $("#preloader-active").css("display", "none");
                                    $('#forerrormessage').empty()
                                    $('#forerrormessage').append("<div class='alert alert-danger'>" + "Something went wrong. Please try again later." + "</div>").delay(4000).fadeOut(function() {
                                        $(this).empty();
                                        $(this).removeAttr('style');
                                    });

                                }

                            })
                        }



                    } else {
                        $("#preloader-active").css("display", "none");
                        $('#forerrormessage').empty()
                        $('#forerrormessage').append("<div class='alert alert-danger'>" + "Please enter at least one shipping price" + "</div>").delay(4000).fadeOut(function() {
                            $(this).empty();
                            $(this).removeAttr('style');
                        });
                    }

                } else {
                    $("#preloader-active").css("display", "none");
                    $('#forerrormessage').empty()
                    $('#forerrormessage').append("<div class='alert alert-danger'>" + "Please enter the tags" + "</div>").delay(4000).fadeOut(function() {
                        $(this).empty();
                        $(this).removeAttr('style');
                    });
                }

            } else {
                $("#preloader-active").css("display", "none");
                $('#forerrormessage').empty()
                $('#forerrormessage').append("<div class='alert alert-danger'>" + "Please select category" + "</div>").delay(4000).fadeOut(function() {
                    $(this).empty();
                    $(this).removeAttr('style');
                });
            }

        }

    });



});


$("#custom").spectrum({
    preferredFormat: "hex",
    showPaletteOnly: true,
    color: "#f00",
    palette: [
        ["#000", "#444", "#666", "#999", "#ccc", "#eee", "#f3f3f3", "#fff"],
        ["#f00", "#f90", "#ff0", "#0f0", "#0ff", "#00f", "#90f", "#f0f"],
        ["#f4cccc", "#fce5cd", "#fff2cc", "#d9ead3", "#d0e0e3", "#cfe2f3", "#d9d2e9", "#ead1dc"],
        ["#ea9999", "#f9cb9c", "#ffe599", "#b6d7a8", "#a2c4c9", "#9fc5e8", "#b4a7d6", "#d5a6bd"],
        ["#e06666", "#f6b26b", "#ffd966", "#93c47d", "#76a5af", "#6fa8dc", "#8e7cc3", "#c27ba0"],
        ["#c00", "#e69138", "#f1c232", "#6aa84f", "#45818e", "#3d85c6", "#674ea7", "#a64d79"],
        ["#900", "#b45f06", "#bf9000", "#38761d", "#134f5c", "#0b5394", "#351c75", "#741b47"],
        ["#600", "#783f04", "#7f6000", "#274e13", "#0c343d", "#073763", "#20124d", "#4c1130"]
    ]
});

$("#custom1").spectrum({
    preferredFormat: "hex",
    showPaletteOnly: true,
    allowEmpty: true,
    palette: [
        ["#000", "#444", "#666", "#999", "#ccc", "#eee", "#f3f3f3", "#fff"],
        ["#f00", "#f90", "#ff0", "#0f0", "#0ff", "#00f", "#90f", "#f0f"],
        ["#f4cccc", "#fce5cd", "#fff2cc", "#d9ead3", "#d0e0e3", "#cfe2f3", "#d9d2e9", "#ead1dc"],
        ["#ea9999", "#f9cb9c", "#ffe599", "#b6d7a8", "#a2c4c9", "#9fc5e8", "#b4a7d6", "#d5a6bd"],
        ["#e06666", "#f6b26b", "#ffd966", "#93c47d", "#76a5af", "#6fa8dc", "#8e7cc3", "#c27ba0"],
        ["#c00", "#e69138", "#f1c232", "#6aa84f", "#45818e", "#3d85c6", "#674ea7", "#a64d79"],
        ["#900", "#b45f06", "#bf9000", "#38761d", "#134f5c", "#0b5394", "#351c75", "#741b47"],
        ["#600", "#783f04", "#7f6000", "#274e13", "#0c343d", "#073763", "#20124d", "#4c1130"]
    ]
});

$("#custom2").spectrum({
    preferredFormat: "hex",
    showPaletteOnly: true,
    allowEmpty: true,
    palette: [
        ["#000", "#444", "#666", "#999", "#ccc", "#eee", "#f3f3f3", "#fff"],
        ["#f00", "#f90", "#ff0", "#0f0", "#0ff", "#00f", "#90f", "#f0f"],
        ["#f4cccc", "#fce5cd", "#fff2cc", "#d9ead3", "#d0e0e3", "#cfe2f3", "#d9d2e9", "#ead1dc"],
        ["#ea9999", "#f9cb9c", "#ffe599", "#b6d7a8", "#a2c4c9", "#9fc5e8", "#b4a7d6", "#d5a6bd"],
        ["#e06666", "#f6b26b", "#ffd966", "#93c47d", "#76a5af", "#6fa8dc", "#8e7cc3", "#c27ba0"],
        ["#c00", "#e69138", "#f1c232", "#6aa84f", "#45818e", "#3d85c6", "#674ea7", "#a64d79"],
        ["#900", "#b45f06", "#bf9000", "#38761d", "#134f5c", "#0b5394", "#351c75", "#741b47"],
        ["#600", "#783f04", "#7f6000", "#274e13", "#0c343d", "#073763", "#20124d", "#4c1130"]
    ]
});

$("#custom3").spectrum({
    preferredFormat: "hex",
    showPaletteOnly: true,
    allowEmpty: true,
    palette: [
        ["#000", "#444", "#666", "#999", "#ccc", "#eee", "#f3f3f3", "#fff"],
        ["#f00", "#f90", "#ff0", "#0f0", "#0ff", "#00f", "#90f", "#f0f"],
        ["#f4cccc", "#fce5cd", "#fff2cc", "#d9ead3", "#d0e0e3", "#cfe2f3", "#d9d2e9", "#ead1dc"],
        ["#ea9999", "#f9cb9c", "#ffe599", "#b6d7a8", "#a2c4c9", "#9fc5e8", "#b4a7d6", "#d5a6bd"],
        ["#e06666", "#f6b26b", "#ffd966", "#93c47d", "#76a5af", "#6fa8dc", "#8e7cc3", "#c27ba0"],
        ["#c00", "#e69138", "#f1c232", "#6aa84f", "#45818e", "#3d85c6", "#674ea7", "#a64d79"],
        ["#900", "#b45f06", "#bf9000", "#38761d", "#134f5c", "#0b5394", "#351c75", "#741b47"],
        ["#600", "#783f04", "#7f6000", "#274e13", "#0c343d", "#073763", "#20124d", "#4c1130"]
    ]
});

$("#custom4").spectrum({
    preferredFormat: "hex",
    showPaletteOnly: true,
    allowEmpty: true,
    palette: [
        ["#000", "#444", "#666", "#999", "#ccc", "#eee", "#f3f3f3", "#fff"],
        ["#f00", "#f90", "#ff0", "#0f0", "#0ff", "#00f", "#90f", "#f0f"],
        ["#f4cccc", "#fce5cd", "#fff2cc", "#d9ead3", "#d0e0e3", "#cfe2f3", "#d9d2e9", "#ead1dc"],
        ["#ea9999", "#f9cb9c", "#ffe599", "#b6d7a8", "#a2c4c9", "#9fc5e8", "#b4a7d6", "#d5a6bd"],
        ["#e06666", "#f6b26b", "#ffd966", "#93c47d", "#76a5af", "#6fa8dc", "#8e7cc3", "#c27ba0"],
        ["#c00", "#e69138", "#f1c232", "#6aa84f", "#45818e", "#3d85c6", "#674ea7", "#a64d79"],
        ["#900", "#b45f06", "#bf9000", "#38761d", "#134f5c", "#0b5394", "#351c75", "#741b47"],
        ["#600", "#783f04", "#7f6000", "#274e13", "#0c343d", "#073763", "#20124d", "#4c1130"]
    ]
});