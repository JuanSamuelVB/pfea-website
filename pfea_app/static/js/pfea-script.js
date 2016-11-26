$(document).ready(function(){
	$('select').material_select();
	$('#calendar').fullCalendar();
	$('.button-collapse').sideNav();
	$('.parallax').parallax();
	$('.dropdown-button').dropdown({
		hover: true
	});
	$('.datepicker').pickadate({
		selectMonths: true,
		selectYears: 2,
		format: 'yyyy-mm-dd'
	});
});
