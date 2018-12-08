$( document ).ready(function() {
    
	$(".status_change_dd").change(function(){
		console.log($(this).attr('job_id'));
		$(this).siblings(":button").prop('disabled', false);
	});
	
	$(".status_change_btn").click(function(){
		
		console.log($(this).attr('job_id'));
	});
	
	
});