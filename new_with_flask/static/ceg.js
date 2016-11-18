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
	$('#delete').on('click',function(event)){
		event.preventDefault();
		var reaction = document.getElementById("info");
		var reactor = reaction.dataset.name
		var reactime = reaction.dataset.time
		$.ajax({
			type: "POST",
			url: "/ajaxCEG/",
			data: {reactorName: reactor,
						 reactionTime: reactime,
					 	 sender: "delete"},
			dataType: "html",
			success: function(html){
				$("#reviewContainer").html(html);
			}
		})
	}
});
