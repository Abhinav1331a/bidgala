$(document).ready(function() {
    $(document).on('click','#post-comment',function(){
        var comment = $("#comment-body").val();
        var post_id = $(this).data("id")        
    
            $.ajax({
                url:'/community/add-comment',
                type:'POST',
                data:{
                    'comment': comment,
                    'post_id': post_id,
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                },
                success:function(data){
                    
                    var commentEl = $('<div class="comment d-flex justify-content-center align-items-start discussion-form w-100 h-100 mb-4"><div class="profile-thumbnail mr-0"><img src=' + data.data[3] + '></div><div class="col-11 d-flex flex-column ml-0"><small><strong><a href="/p/' + data.data[1] + '" class="text-muted">' + data.data[1] + '</a> replied now ' + '<a href="/community/delete-comment/'+data.data[5]+'/'+ data.data[4]+'"><i class="fas fa-trash-alt"></i></a>' + '</strong></small><small id="comment-body-posted">' + data.data[0] +'</small></div></div>').hide().fadeIn()
                    
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

                    $('.container.comments').prepend(commentEl);
                    
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
