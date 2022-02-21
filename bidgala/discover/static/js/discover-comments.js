$(document).ready(function() {
    $(document).on('click','#post-comment',function(){
        var comment = $("#comment-body").val();
        var article_id = $(this).data("id")

    
            $.ajax({
                url:'/discover/add-comment',
                type:'POST',
                data:{
                    'comment': comment,
                    'article_id': article_id,
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                },
                success:function(data){
                    console.log(data)

                    var commentEl = $('<div class="comment d-flex justify-content-center align-items-start discussion-form w-100 h-100 mb-4"><div class="profile-thumbnail mr-0"><img src=' + data.data[3] + '></div><div class="col-11 d-flex flex-column ml-0"><small class="w-100 d-flex justify-content-between"><strong><a href="/p/' + data.data[1] + '" class="text-muted">' + data.data[1] + '</a> replied now ' + '<a href="/discover/delete-comment/'+data.data[5]+'/'+ data.data[4]+'"></strong><strong><i class="fas fa-trash-alt"></i></a>' + '</strong></small><small id="comment-body-posted">' + data.data[0] +'</small></div></div>').fadeIn(500);

                    $("#comment-body").val("");
                    $("#no-replies-container").css("display", "none");
                    $("#no-replies-txt").css("display", "none");
                    
                    $('#comments-container').prepend(commentEl);
                    $("#get-comment-count").text(parseInt($("#get-comment-count").text()) + 1)
                    $( "#alert" ).attr({ class:"alert alert-success fade", role:"alert"});
                    $("#alert").html("Comment posted successfully");
                    $("#alert").fadeTo(2000, 500).slideUp(500, function(){
                        $("#alert").slideUp(500);
                    });

                    
                },
                error: function(xhr, status, error) {
                    $( "#alert" ).attr({ class:"alert alert-danger fade", role:"alert"});
                    $("#alert").html("Something went wrong");
                    $("#alert").fadeTo(2000, 500).slideUp(500, function(){
                        $("#alert").slideUp(500);
                    });
                    var err = eval("(" + xhr.responseText + ")");
                    console.log(err.Message);
                },
            });
    });
});


$(document).ready(function(){
  $('#comment-body').on('keydown', function(e) {
      if (e.keyCode == 13) {
    $("#post-comment").click()
      }
    });
});

