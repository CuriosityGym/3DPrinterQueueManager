$( document ).ready(function() {
    
	$(".status_change_dd").change(function(){
		console.log($(this).attr('job_id'));
		$(this).siblings(":button").prop('disabled', false);
	});
	
	$(".status_change_btn").click(function(){
		
		//console.log($(this).attr('job_id'));
		job_id=$(this).attr('job_id')		
		var myanchor = $(this);
		formedURL="/changeJobStatus/printing/"+job_id
		$.ajax({
				url: formedURL,
				success:function(data, status, jqXHR) {
					//console.log("done")
					file_path_url=$(myanchor).attr('file_url')
				    //console.log(myanchor.parent().parent());
					myanchor.parent().parent().hide();					
					window.open(file_path_url);
					$("body").trigger("refreshPrinted");
					}
				
				})
		
		
	});
	
	$("body").on( "refreshPrinted", function() {
		formedURL="/getPrintingList"
			$.ajax({
				url: formedURL,
				success:function(data, status, jqXHR) {
					console.log(data)
					$(".printingrow").remove();
					$(".printingTableBody").append(data);
					}
				
				})
		});
		
		$(".img_link").click(function(){
		
		//console.log($(this).attr('job_id'));
		job_id=$(this).attr('job_id').trim()
		actionType=$(this).attr('action_type').trim();		
		var myanchor = $(this);
		formedURL="/changeJobStatus/"+actionType+"/"+job_id
		$.ajax({
				url: formedURL,
				success:function(data, status, jqXHR) {
					console.log("done")					
					}
				
				})
		
		
	});
	
	
	
});