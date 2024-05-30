$(document).ready(() => {
	$('#btn_translate').click(callBackFunction);
});

function callBackFunction() {
	const languageCode = $('#language_code').val();
	const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

	$.get(url, addText);
}

function addText(data) {
	$('#hello').text(data.hello);
}
