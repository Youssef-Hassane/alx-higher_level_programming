
const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

/* Get data from url */
$.getJSON(url, callBackFunction);

function callBackFunction(data) {
	const textString = data.hello;
	$("#hello").text(textString);
}


