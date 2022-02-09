// 1.search contact
// 2.load 10 message when selecting a new account
// 3.scroll up load more MESSAGES
// 4.ajax call to load more
// 5.ajax call to send MESSAGES, send to server, send id's of messages already have
// 6.

var timestamp;
var profile_img_other_user;
var socket = null;

var stop_scroll = false;
const monthNames = ["January", "February", "March", "April", "May", "June",
  						"July", "August", "September", "October", "November", "December"];

var isMobile = false; //initiate as false
// device detection
if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent)
    || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0,4))) {
    isMobile = true;
}  					

if(isMobile) {
	$('#scrollUp').toggleClass('hide')
}	
// 1.search contact

	// $('.messages').scrollTop($('.messages')[0].scrollHeight);
	var $input = $('#searchContact');
	$(document).on('keyup', $input, function() {

		var $val = $input.val().trim().toLowerCase(),
				$select = $('.contact'),
				$selectBadge = $('.badge');
		// Check if the input isn't empty
		if ($val != '') {
			$select.addClass('hide');
			$selectBadge.addClass('hide');
			$select.find('span.badge').addClass('hide');
			var $result = $select.filter(function() {
				return $(this).find('div.name').find('div').text().replace(/\s+/g, '').toLowerCase().indexOf($val) !== -1;
			});
			$result.removeClass('hide');
 			$result.siblings('span.badge').removeClass('hide');
		} else {
			$select.removeClass('hide');
			$selectBadge.removeClass('hide');
		}
	});


	$('.message-input').on('keydown', function(e) {
		if (e.keyCode == 13) {
			$(".submit").click()
		}
	});

	//# sourceURL=pen.js


// 2.load 10 message when selecting a new account
$("li.contact").click(function(e) {
	function adjustScreenSize(widthScreen) {
		if(widthScreen.matches){
  			$("#content").toggleClass("open");
  	}
	}
	var widthScreen = window.matchMedia("(max-width: 767px)");
	adjustScreenSize(widthScreen);
	widthScreen.addListener(adjustScreenSize);
  stop_scroll = false;
	// if(isMobile){
	// 		$("#content").toggleClass("open");
	// }


	if (socket != null) {
		socket.close();
	}

	if ($(this).parent().children(".chat-notif")) {
		var unreadLength = parseInt(window.localStorage.getItem('unread-count') - 1);
		if (unreadLength < 0) {
			window.localStorage.setItem('unread-count', 0);
		} else {
			window.localStorage.setItem('unread-count', unreadLength);
		}
	}


	$(this).siblings('span.badge').remove();

	var unreadLength = $('.chat-notif').length;

	if (unreadLength === 0) {
		console.log(unreadLength)
		$(".notif-badge").remove();
		$(".notif-badge-account").remove();
	}

	$('li.contact').removeClass('hide');
	$('li.contact.active').removeClass('active');
	$(this).addClass('active');
	$(this).prependTo($(this).parent());
	$(this).parent('u').parent('div').scrollTop();
		 $('#msg-cover').addClass("hide");
		 $('#setOtherUsername').val($(this).parent().attr('id').substring(7))
		 var loc = window.location

var formData = $("#form")
var msgInput = $("#id_message")
var chatHolder = $("#chat-items")
var wsStart = 'ws://'
var me = $("#myUsername").val()
if (loc.protocol == 'https:') {
	wsStart = 'wss://'
}

var endpoint = wsStart + loc.host + '/ws/' + $('#setOtherUsername').val()


if (!endpoint.endsWith('/')) {
	endpoint = endpoint + '/'
}
otheruser_thread_details = $('#setOtherUsername').val()//loc.pathname.split('/')[2]

socket = new ReconnectingWebSocket(endpoint)
//var socket = new WebSocket(endpoint)

socket.onmessage = function(e) {

	var chatDataMsg = JSON.parse(e.data)
	console.log(JSON.parse(e.data))
	if($("#current_user_id").val() != chatDataMsg.id)
	//alert(JSON.stringify(chatDataMsg));
	$('<li class="replies"><img src="'+profile_img_other_user+'" alt=""/><p>' + chatDataMsg.message+'</p></li>').appendTo($('.messages ul'));
	var id = $('.contact.active').parent().attr('id').substring(7)

	$('#message-preview-' + id).html(chatDataMsg.message);
		if(chatDataMsg.echo_to_sender!=me) {
			var ack = {
			'type' : 'ack',
			'msg_ack_id' : chatDataMsg.send_ack_id,
			'user' : me,
		}
			socket.send(JSON.stringify(ack))


		}


}
socket.onopen = function(e) {
	 console.log("open", e)


	 $('.submit').on('click', function() {
		console.log("clicking!");
		message = $(".message-input input").val();
		if($.trim(message) == '') {
			return false;
		}
		var finalData = {
			'type' : 'message',
			'message' : message,
			'user' : me,
		}


		var local_date = new Date()
		var month = local_date.getMonth()
		var day = local_date.getDate()

		$("#chat-date-" + $('#setOtherUsername').val()).html(monthNames[month] + ' ' + day)


		socket.send(JSON.stringify(finalData))
		socket_notify.send(JSON.stringify({'thread_id' : otheruser_thread_details}))

		$('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));
		$('.message-input input').val(null);
		var id = $('.contact.active').parent().attr('id').substring(7)
		$('#message-preview-' + id).html(message);
		$(".messages").animate({ scrollTop: $('.messages').prop("scrollHeight")}, 1000);



		});
	}


		$(document).ready(function(){
			$('#message-content').keydown (function(e){
				if(e.key === 'Enter' || e.keyCode === 13){
					$('.submit').click();
				}
			});
		});


	socket.onerror = function(e) {
		console.log("error", e)
	}
	socket.onclose = function(e) {
		console.log("close", e)
	}

    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "/messages/message-page-order",
        data: {
            'user_id': $(this).parent().attr('id').substring(7), // < note use of 'this' here
            'timestamp': "",
						'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(result) {
						console.log(result);
            displayMsg(result);
        },
        // error: function(result) {
				// 		console.log(result);
        //     alert('error');
        // }
    });
});

function displayMsg(e){
	var loc = window.location

	var protocol = loc.protocol
	var host = loc.host

	var profile_url_link = protocol + '//' + host + '/p/' + $('#notify-' + $('#setOtherUsername').val()).data('username');

	var contact = document.querySelectorAll('.contact-profile > div')[0];
	contact.innerHTML = "";
	$('#msg-display').empty();
	profile_img_other_user = e.other_user_info.profile_img;
	contact.insertAdjacentHTML('beforeend',"<img src='"+ profile_img_other_user +"' alt='' /><a class='ml-2' href='" + profile_url_link + "'>"+ e.other_user_info.name +"</a>");
	if(e.messages.length > 0){
	timestamp = e.messages[0].timestamp;

	console.log("timestamp: "+ timestamp);


	// e.profile_img//url for img
	var msgList = document.getElementById("msg-display");

	e.messages.forEach(function(msg) {
		  var date = new Date(msg.timestamp);
			if(msg.primary){
				msgList.insertAdjacentHTML('beforeend', "<li class='sent'><p>"+ msg.text+"<br><small>"+date.toLocaleDateString()+" "+ date.toLocaleTimeString() +"</small></p></li>");
			}else{
				msgList.insertAdjacentHTML('beforeend', "<li class='replies'><img src='"+ profile_img_other_user +"' alt='' /><p>"+ msg.text+"<br><small>"+date.toLocaleDateString()+" "+ date.toLocaleTimeString()+"</small></p></li>");
			}
      });
}
		$(".messages").animate({ scrollTop: $('.messages').prop("scrollHeight")}, 1000);
}

//3.scroll up load more MESSAGES
jQuery(document).ready(function($) {
$('#messages').scroll(function(){
    if ($('#messages').scrollTop() == 0 && (!stop_scroll)){
		    $.ajax({
		        type: "POST",
		        url: "/messages/message-page-order",
		        data: {
		            'user_id': $('.contact.active').parent().attr('id').substring(7), // < note use of 'this' here
		            'timestamp': timestamp,
								'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
		        },
		        success: function(result) {
								console.log(result);
					if(result.messages.length > 0) {
		            loadMoreMsg(result);
		        }
		        else {
		        	stop_scroll = true;
		        }
		        },
		    });

	}
});
});

function loadMoreMsg(e){
	// e.profile_img//url for img
	var msgList = document.getElementById("msg-display");
	var firstMsg = $('#msg-display li:first');
	var curOffset = firstMsg.offset().top - $(document).scrollTop();
	if(e.messages.length > 0){
	timestamp = e.messages[0].timestamp;

	console.log("timestamp: "+ timestamp);
	for (var i = e.messages.length; i-- > 0; ){
		var msg = e.messages[i];
		var date = new Date(msg.timestamp);
		var local_date = new Date(date.getTime() - date.getTimezoneOffset()*60*1000);
		var month = local_date.getMonth()
		var day = local_date.getDay()


		$("#chat-date-" + $('#setOtherUsername').val()).html(monthNames[month] + ' ' + day)
		if(msg.primary){
			msgList.insertAdjacentHTML('afterbegin', "<li class='sent'><p>"+ msg.text+"<br><small>"+date.toLocaleDateString()+" "+date.toLocaleTimeString()+"</small></p></li>");
		}else{
			msgList.insertAdjacentHTML('afterbegin', "<li class='replies'><img src='"+ e.other_user_info.profile_img +"' alt='' /><p>"+ msg.text+"<br><small>"+date.toLocaleDateString()+" "+date.toLocaleTimeString()+"</small></p></li>");
		}

	}
}
// $(".messages").animate({ scrollTop: 120}, 1000);
$(".messages").scrollTop(firstMsg.offset().top-curOffset);
}

window.onload = function(){

	 var loc = window.location
	 trigger_click_id = loc.pathname.replace('/messages/', '').replace('/', '');
	 $('#li-' + trigger_click_id).click();

	$(".contact").each(function() {
		var id = $(this).attr('id').replace('li-', '')
		var server_time = $("#chat-date-" + id).html()

		if(server_time.length > 0){

			var server_date = new Date(server_time.replace(/ /g,"T"))
			var local_date = new Date(server_date.getTime() - server_date.getTimezoneOffset()*60*1000);

			var month = local_date.getMonth()
			var day = local_date.getDate()

			
			if(parseInt(day) == 0) {
				day = 1;
			}
			
			
			$("#chat-date-" + id).html(monthNames[month] + ' ' + day)
		}

	})

}

var keys = {37: 1, 38: 1, 39: 1, 40: 1};

function preventDefault(e) {
  e.preventDefault();
}


function preventDefaultForScrollKeys(e) {
  if (keys[e.keyCode]) {
    preventDefault(e);
    return false;
  }
}

// modern Chrome requires { passive: false } when adding event
var supportsPassive = false;
try {
  window.addEventListener("test", null, Object.defineProperty({}, 'passive', {
    get: function () { supportsPassive = true; }
  }));
} catch(e) {}

var wheelOpt = supportsPassive ? { passive: false } : false;
var wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';



function disableScroll() {
  window.addEventListener('DOMMouseScroll', preventDefault, false); // older FF
  window.addEventListener(wheelEvent, preventDefault, wheelOpt); // modern desktop
  window.addEventListener('touchmove', preventDefault, wheelOpt); // mobile
  window.addEventListener('keydown', preventDefaultForScrollKeys, false);
}

// call this to Enable
function enableScroll() {
  window.removeEventListener('DOMMouseScroll', preventDefault, false);
  window.removeEventListener(wheelEvent, preventDefault, wheelOpt);
  window.removeEventListener('touchmove', preventDefault, wheelOpt);
  window.removeEventListener('keydown', preventDefaultForScrollKeys, false);
}

//4.mobile VERSION
$(document).ready(function() {
		// var windowWidth = $(window).width();
	  $('a.back-to-contact').on('click', function() {
			function adjustScreenSize(widthScreen) {
				if(widthScreen.matches){
					$('li.contact.active').removeClass('active');
				 	$("#content").removeClass("open");
				}
			}
			var widthScreen = window.matchMedia("(max-width: 767px)");
			adjustScreenSize(widthScreen);
			widthScreen.addListener(adjustScreenSize);
		});

});;


$(window).on('load', function() {
		var unreadLength = $('.chat-notif').length;
		window.localStorage.setItem('unread-count', unreadLength);

});

