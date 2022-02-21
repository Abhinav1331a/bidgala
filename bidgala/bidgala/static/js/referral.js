var clipboard = new ClipboardJS('#copybtn');


  clipboard.on('success', function(e) {
      $("#copybtn").hide();
      $("#copied").removeAttr("hidden").delay(1000).hide();
      $("#copybtn").show(); 
  });

  clipboard.on('error', function(e) {
      console.error('Action:', e.action);
      console.error('Trigger:', e.trigger);
  });

  // Overrides focus for modal so clipboard can work in modal
  $.fn.modal.Constructor.prototype._enforceFocus = function() {};


  var modalClipboard = new ClipboardJS('#modal-copy');


  modalClipboard.on('success', function(e) {
      console.log(e)
  });

  modalClipboard.on('error', function(e) {
      console.error('Action:', e.action);
      console.error('Trigger:', e.trigger);
  });


 

const shareButton = $("#sharebtn")
const mobileShareButton = $("#mobile-share-options")

const title = "Sign up for Bidgala with my link"
const url = $("#copybox").attr("value");
const text = "Sign up for Bidgala with my link and get 50 credits"

shareButton.on("click", () => {
  if (navigator.share) {
    mobileShareButton.on("click", () => {
      navigator.share({
        title: `${title}`,
        url: `${url}`,
        text: `${text}`
      }).then(() => {
        console.log('Thanks for sharing');
        //trigger an alert saying thank you
      }).catch(console.error);
    })
  } else { 
    mobileShareButton.hide()
  }
})