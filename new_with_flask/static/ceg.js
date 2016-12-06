$(document).ready(function($) {
	var chordname = document.getElementById("chordname");
	var realchord = chordname.attributes.getNamedItem("data-chord").value;
	$.ajax({
		type: "GET",
		url: "/ajaxCEG/",
		data:{
			chord: realchord,
			sender: "indexsearch"
		},
		dataType: "html",
		success: function(html){
			$("#reviewContainer").html(html);
		}
	});

	$('#submit').on('click', function(event) {

		event.preventDefault();
		document.getElementById("reviewContainer").textContent = "Thanks one sec . . .";

		var textField = document.getElementById("reaction").value;
		var chordname = document.getElementById("chordname");
		var rchord = chordname.attributes.getNamedItem("data-chord").value;

		$.ajax({
			type: "POST",
			url: "/ajaxCEG/",
			data: {reviewText: textField,
					   chord: rchord,
						 sender: "submit"},
			dataType: "html",
			success: function(html){
				$("#reaction").val("");
				$("#reviewContainer").html(html);
			}
		});
	});

});
