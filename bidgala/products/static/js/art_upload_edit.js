

    $('#onClose').click(function(event) {
    
      tagify.removeAllTags();
     $("#changedata").modal('hide');

      
    });

    $(document).ajaxStart(function(){
  $("#preloader-active").css("display", "block");
});

 

$(document).ajaxComplete(function(){
  $("#preloader-active").css("display", "none");
});



var input_tag = document.querySelector('input[name=tags2]'),

tagify = new Tagify(input_tag, {
pattern             : /^.{0,20}$/,  // Validate typed tag(s) by Regex. Here maximum chars length is defined as "20"
delimiters          : ",| ",        // add new tags when a comma or a space character is entered
keepInvalidTags     : false,         // do not remove invalid tags (but keep them marked as invalid)
editTags            : 1,            // single click to edit a tag
transformTag        : transformTag,
backspace           : "edit",
placeholder         : "type tags",
duplicates          : false,
originalInputValueFormat : valuesArr => valuesArr.map(item => item.value).join(','),
dropdown : {
enabled: 3,
}
});
// generate a random color (in HSL format, which I like to use)
function getRandomColor(){
function rand(min, max) {
return min + Math.random() * (max - min);
}
var h = rand(1, 360)|0,
s = rand(40, 70)|0,
l = rand(65, 72)|0;
return 'hsl(' + h + ',' + s + '%,' + l + '%)';
}


function transformTag( tagData ){
tagData.style = "--tag-bg:" + getRandomColor();
if( tagData.value.toLowerCase() == 'shit' )
tagData.value = 's✲✲t'
}


    
    $( ".onedit" ).click(function() {
      
      var id = $(this).attr('name');
      $("input[id='id']").val(id);
      $("#artname").attr('value', $("#" + id + "_title").val());
      $("#artdescription").val($("#" + id + "_artdescription").val());
      $("input[id='price']").val($("#" + id + "_price").val());
     
      $("input[id='shipus']").val($("#" + id + "_shipping_us").val());
      $("input[id='shipuk']").val($("#" + id + "_shipping_uk").val());
      $("input[id='shipaunz']").val($("#" + id + "_shipping_aunz").val());
      $("input[id='shipasia']").val($("#" + id + "_shipping_asia").val());
      $("input[id='shipeurope']").val($("#" + id + "_shipping_europe").val());
      $("input[id='shipother']").val($("#" + id + "_shipping_other").val());
      $("input[id='height']").val($("#" + id + "_height").val());
      $("input[id='width']").val($("#" + id + "_width").val());
      $("input[id='depth']").val($("#" + id + "_depth").val());

      // TO remove previously style values
      $(".style_art_actual_submit").each(function(i, obj) {
           
          $(this).prop( "checked", false );
        });


      $("." + id + "_style_common").each(function(i, obj) {
          
          $("#style_" +obj.value).prop( "checked", true );
        });


      if ($('#' + id+'_show_shipping_price_can').val()=='True') {
         $("input[id='shipcanada']").val($("#" + id + "_shipping_can").val());
      }else {
         $("input[id='shipcanada']").val($("#" + id + "_shipping_can").val());
          $("input[id='shipcanada']").prop('disabled', true);
          $("input[id='shipcanada']").attr('hidden', 'hidden');
          $("input[id='shipcanada']").siblings().attr('hidden', 'hidden');
          $("input[id='shipcanada']").parent().attr('hidden', 'hidden');
      } 

       if ($('#' + id+'_show_shipping_price_us').val()=='True') {
         $("input[id='shipus']").val($("#" + id + "_shipping_us").val());
      }else {
         $("input[id='shipus']").val($("#" + id + "_shipping_us").val());
          $("input[id='shipus']").prop('disabled', true);
           $("input[id='shipus']").attr('hidden', 'hidden');
            $("input[id='shipus']").siblings().attr('hidden', 'hidden');
            $("input[id='shipus']").parent().attr('hidden', 'hidden');
      } 

      if ($('#' + id+'_show_shipping_price_uk').val()=='True') {
         $("input[id='shipuk']").val($("#" + id + "_shipping_uk").val());

      }else {
         $("input[id='shipuk']").val($("#" + id + "_shipping_uk").val());
          $("input[id='shipuk']").prop('disabled', true);
            $("input[id='shipuk']").attr('hidden', 'hidden');
            $("input[id='shipuk']").siblings().attr('hidden', 'hidden');
            $("input[id='shipuk']").parent().attr('hidden', 'hidden');
      } 

      if ($('#' + id+'_show_shipping_price_aunz').val()=='True') {
         $("input[id='shipaunz']").val($("#" + id + "_shipping_aunz").val());
      }else {
         $("input[id='shipaunz']").val($("#" + id + "_shipping_aunz").val());
          $("input[id='shipaunz']").prop('disabled', true);
          $("input[id='shipaunz']").attr('hidden', 'hidden');
          $("input[id='shipaunz']").siblings().attr('hidden', 'hidden');
          $("input[id='shipaunz']").parent().attr('hidden', 'hidden');
      } 


      if ($('#' + id+'_show_shipping_price_asia').val()=='True') {
         $("input[id='shipasia']").val($("#" + id + "_shipping_asia").val());
      }else {
         $("input[id='shipasia']").val($("#" + id + "_shipping_asia").val());
          $("input[id='shipasia']").prop('disabled', true);
           $("input[id='shipasia']").attr('hidden', 'hidden');
           $("input[id='shipasia']").siblings().attr('hidden', 'hidden');
            $("input[id='shipasia']").parent().attr('hidden', 'hidden');
      } 



      if ($('#' + id+'_show_shipping_price_europe').val()=='True') {
         $("input[id='shipeurope']").val($("#" + id + "_shipping_europe").val());
      }else {
         $("input[id='shipeurope']").val($("#" + id + "_shipping_europe").val());
          $("input[id='shipeurope']").prop('disabled', true);
          $("input[id='shipeurope']").attr('hidden', 'hidden');
          $("input[id='shipeurope']").siblings().attr('hidden', 'hidden');
           $("input[id='shipeurope']").parent().attr('hidden', 'hidden');
      } 

      if ($('#' + id+'_show_shipping_price_other').val()=='True') {
         $("input[id='shipother']").val($("#" + id + "_shipping_other").val());
      }else {
         $("input[id='shipother']").val($("#" + id + "_shipping_other").val());
          $("input[id='shipother']").prop('disabled', true);
           $("input[id='shipother']").attr('hidden', 'hidden');
           $("input[id='shipother']").siblings().attr('hidden', 'hidden');
            $("input[id='shipother']").parent().attr('hidden', 'hidden');
      } 


      $("#measure").val($("#" + id + "_metrics").val());

     
      
      tagify.addTags($("#" + id + "_tags").val())
      $("#changedata").modal('show')


      $( "#editdata_confirm" ).bind('click', function() {
        
        

   if($("#artedit").valid()) {

var styles = ''
 $(".style_art_actual_submit").each(function(i, obj) {
          
          if($(this).prop('checked')) {
            styles = styles + obj.value + ",";
          }

        });



if (styles.slice(-1) == ',') {
    styles = styles.slice(0, -1);
}


$("input[id='style_art_post_data_hidden']").val(styles)

$("#artedit").submit();

}
      });

      });
    
   
  



 

