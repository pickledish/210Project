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
			data: {reviewText: textField},
			dataType: "html",
			success: function(html){
				$("#reviewContainer").html(html);
			}
		});
	});
});