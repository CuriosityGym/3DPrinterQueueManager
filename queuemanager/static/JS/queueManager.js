$( document ).ready(function() {
    
	$(".status_change_dd").change(function(){
		console.log($(this).attr('job_id'));
		$(this).siblings(":button").prop('disabled', false);
	});
	
	$(".status_change_btn").click(function(){
		
		//console.log($(this).attr('job_id'));
		job_id=$(this).attr('job_id')
		formedURL="/changeJobStatus/printing/"+job_id
		$.ajax({
				url: formedURL,
				success(function() {
					console.log("done")
					console.log($(this).parent().parent());
					$(this).parent().parent().hide();
					});
				
				})
		
		
	});
	
	
	
});