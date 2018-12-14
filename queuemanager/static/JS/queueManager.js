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
		
		var dataToBeSent={};
		var csrftoken = getCookie('csrftoken');
		var customHeaders={}
		customHeaders["X-CSRFToken"]=csrftoken;
		switch(actionType){
		case "completed":
			printingTimeConsumed=getPrintTimeByPrompt();
			console.log(printingTimeConsumed);
			formedURL="/changeJobStatus/"+actionType+"/"+job_id
			dataToBeSent.printTime=printingTimeConsumed
		case "failed":
			formedURL="/changeJobStatus/"+actionType+"/"+job_id
			
		default:
			//Do nothing
		}	
		var myanchor = $(this);
		
		$.ajax({
				url: formedURL,
				data:dataToBeSent,
				method:"POST",
				headers:customHeaders,
				success:function(data, status, jqXHR) {
					console.log("done")		
					$(myanchor).parent().parent().remove();		
					}
				
				})
		
		
	});
	
	
	
});

function getPrintTimeByPrompt() {
    var text;
    var printTime = prompt("How many minutes did this print take?", "60");
    return printTime
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
