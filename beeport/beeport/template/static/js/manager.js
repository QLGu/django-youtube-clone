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
	$('#addlist').click(function(){
		$.get('/add-multi-list/', {video_id: $(this).attr('name')}, function(data){
			
		});
	})
	$('#addtag').click(function(){
		$.get('/add-multi-tag/', {video_id: $(this).attr('name')}, function(data){
			
		});
	})
	$('#changecat').click(function(){
		$.get('/change-multi-cat/', {video_id: $(this).attr('name')}, function(data){
			
		});
	})
	$('#delmulti').click(function(){
		$.get('/delete-multi/', {video_id: $(this).attr('name')}, function(data){
			
		});
	})
	$('#multipublic').click(function(){
		$.get('/make-multi-public/', {video_id: $(this).attr('name')}, function(data){
			
		});
	})
	$('#multiurl').click(function(){
		$.get('/make-multi-owner-public/', {video_id: $(this).attr('name')}, function(data){
			
		});
	})
	$('#multiprivate').click(function(){
		$.get('/make-multi-private/', {video_id: $(this).attr('name')}, function(data){
			
		});
	})
});