$(document).ready(function(){
	$('select').material_select();
	$('#calendar').fullCalendar({
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,listYear'
		},
		googleCalendarApiKey: 'AIzaSyCID6HksHlVeF0MHr1Mw9lEjGNx-rr9Pbw',
		events: {
			googleCalendarId: '0l8dfn8l0c50p38sqc427nfvlk@group.calendar.google.com'
		}
	});
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
