$( document ).ready(function() {
    
	$(".status_change_dd").change(function(){
		console.log($(this).attr('job_id'));
	});
});