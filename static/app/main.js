$(function() {

	var rowerWheals = {
		left : 0,
		right : 0
	};

	var waiting = false;

	$.get('/control')
	.then(function(data) {
		rowerWheals = data;
	});

	$('button').on('click', function(e) {
		if(waiting) return;

		var button = e.target;

		waiting = true;

		rowerWheals[button.getAttribute("data-track")] += Number(
			button.getAttribute("data-increament"));

		$.post('/control', rowerWheals)
		.then(function(data) {
			rowerWheals = data;

			waiting = false;
		});
	});
});