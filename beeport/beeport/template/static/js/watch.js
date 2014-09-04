$(document).ready(function() {
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';'); 
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1)); break;
				} 
			}
		}
		return cookieValue; 
	}
	var csrftoken = getCookie('csrftoken');	
	$('#like').click(function(){
		$.get('/like/', {video_id: $(this).attr('name')}, function(data){
			$('#like_count').html(data);
			$('#like').text('Unlike');
		});
	})
	$('#follow').click(function(){
		$.get('/follow/', {slug: $(this).attr('name')}, function(data){
		
		});
	})
	$('#comment').click(function(){
		$.ajax({
			type: "POST",
			url: "/comment/",
			data: {'slug': $(this).attr('name'),'text': $('#textcom').val(), 'csrfmiddlewaretoken': csrftoken},
			dataType: "text",
			success: function(response) {
				alert('You commented this')
				data : {}
			},
			error: function(rs, e) {
				alert(rs.responseText);
			}
		}); 
	})

});