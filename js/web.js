$(document).ready(function() {

	function run() {
		$('#yale').load('web.py', {'hangul': $('#hangul').val()});
	}

	$('#convert').click(function(e) {
		run();
		e.preventDefault();
	});

	$('#hangul').keyup(function(e) {
		run();
	});

	$('.option').click(function(e) {
		run();
	});

});
