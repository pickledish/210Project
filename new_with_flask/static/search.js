$(document).ready(function($) {
	$.ajax({
		type: "GET",
		url: "/ajaxsearch/",
		dataType: "html",
		success: function(html){
			$("#resultContainer").html(html);
		}
	});
	$('#search').on('click', function(event) {

		event.preventDefault();
		document.getElementById("resultContainer").textContent = "Thanks one sec . . .";

		var textField = document.getElementById("search_text").value;

		$.ajax({
			type: "POST",
			url: "/ajaxsearch/",
			data: {searchText: textField,
						 sender: "search"},
			dataType: "html",
			success: function(html){
				$("#resultContainer").html(html);
			}
		});
	});

});
