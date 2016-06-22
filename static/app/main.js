$(function() {

	var rowerWheals = {
		left : 0,
		right : 0,
		delay : 0
	};

	var waiting = false;

	$.get('/control')
	.then(controllCallback);

	$('button[data-track]').on('click', function(e) {
		if(waiting) return;

		var button = e.target;

		waiting = true;

		rowerWheals[button.getAttribute("data-track")] += Number(
			button.getAttribute("data-increament"));

		$.post('/control', rowerWheals)
		.then(controllCallback);
	});

	$('.go').on('click', getCommandSender({left: 1, right: 1}));

	$('.stop').on('click', getCommandSender({left: 0, right: 0}));

	$('.back').on('click', getCommandSender({left: -1, right: -1}));

	$('.turnRight').on('click', getCommandSender({
		duration: 1000,
		delta: 1,
		track: "right"
	}, '/maneuver'));

	$('.turnLeft').on('click', getCommandSender({
		duration: 1000,
		delta: 1,
		track: "left"
	}, '/maneuver'));

	function controllCallback(data) {
		rowerWheals = data;

		waiting = false;
	}

	function getCommandSender(command, action) {
		action = action || '/control';

		return function() {
			waiting = true;

			$.post(action, command)
			.then(controllCallback);
		}
	}
});