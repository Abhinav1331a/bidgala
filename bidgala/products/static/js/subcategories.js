$(document).ready(function () {
  // $("select[name='category']").on("change",function(){
  $(document).delegate("#category", "change", function () {
    var token = $("input[name='csrfmiddlewaretoken']").val();
    var option = $("#category").val();

    if (option.length > 0) {
      $("#subcategory").find("option").remove();

      $.ajax({
        url: "/getSubCategory",
        type: "POST",
        data: {
          csrfmiddlewaretoken: token,
          category: option,
        },
        headers: {
          "X-CSRF-Token": token,
        },

        success: function (result) {
          
          $("#fordynamicsubcategory").html(
            '<select id="subcategory" name="subcategory" form="artuploadform"><option  disabled="disabled" selected="true">Subject</option></select>'
          );
          $("#subcategory").addClass("form-control");

          for (let [key, value] of Object.entries(result.data)) {
            $("#subcategory").append(
              $("<option></option>").attr("value", key).text(value)
            );
          }
        },

        error: function (XMLHttpRequest, textStatus, errorThrown) {
          $("#showMessage")
            .append(
              "<div class='alert alert-danger'>Something went wrong :-(</div>"
            )
            .delay(4000)
            .fadeOut(function () {
              $(this).empty();
              $(this).removeAttr("style");
            });
        },
      });
    }
  });
});
