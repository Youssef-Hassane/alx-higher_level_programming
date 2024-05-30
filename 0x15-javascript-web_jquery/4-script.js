$("#toggle_header").click(() => {
	$("header").toggleClass("red green");
})

// Another way to do it:
// $('#toggle_header').click(function () {
// 	const header = $('header');
// 	if (header.hasClass('red')) {
// 		header.removeClass('red').addClass('green');
// 	} else {
// 		header.removeClass('green').addClass('red');
// 	}
// });
