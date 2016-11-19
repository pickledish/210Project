$(document).ready(function($) {
	$.ajax({
		type: "GET",
		url: "/ajaxCEG/",
		dataType: "html",
		success: function(html){
			$("#reviewContainer").html(html);
		}
	});
	$('#submit').on('click', function(event) {

		event.preventDefault();
		document.getElementById("reviewContainer").textContent = "Thanks one sec . . .";

		var textField = document.getElementById("reaction").value;

		$.ajax({
			type: "POST",
			url: "/ajaxCEG/",
			data: {reviewText: textField,
						 sender: "submit"},
			dataType: "html",
			success: function(html){
				$("#reviewContainer").html(html);
			}
		});
	});

	// $('#delete').on('click',function(event){
	// 	event.preventDefault();
	// 	var timeValue = event.target.attributes.getNamedItem('data-name').value;
	//
	// 	$.ajax({
	// 		type: "POST",
	// 		url: "/ajaxCEG/",
	// 		data: {reactionTime: timeValue,
	// 				 	 sender: "delete"},
	// 		dataType: "html",
	// 		success: function(html){
	// 			$("#reviewContainer").html(html);
	// 		}
	// 	});
	// });

});
