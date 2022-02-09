$(document).on('click','.like-bt-click',function(){

      var post_id = $(this).data("id")
      current_element = $(this)
      
          $.ajax({
                  url:'/community/add-like',
                  type:'POST',
                  data:{
                      'post_id': post_id,
                      'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                  },
                  success:function(data){  

                      if(data.result == 'increment') {     
                      $(".like-button .like-btn"+data.postid).attr("id", "unlike-btn")
                      $(".like-count"+data.postid).html(parseInt($(".like-count"+data.postid).html(), 10)+1)
                      $(this).data('status', 'like')
                      current_element.empty().html('<i class="fa fa-thumbs-up" aria-hidden="true"></i>')
                      $("#count-" + post_id).removeClass("down").addClass("active")
                      
                      } else {
                          $(".like-button .like-btn"+data.postid).attr("id", "like-btn")
                          $(".like-count"+data.postid).html(parseInt($(".like-count"+data.postid).html(), 10)-1)
                          $(this).data('status', 'unlike')
                  
                          current_element.empty().html('<i class="fa fa-thumbs-o-up" aria-hidden="true"></i>')
                          $("#count-" + post_id).removeClass("active").addClass("down")
                      }
                  },
                  error: function(xhr, status, error) {
                      var err = eval("(" + xhr.responseText + ")");
                      console.log(err.Message);
                  },
              });

      
  });