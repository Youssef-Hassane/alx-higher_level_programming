const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

function callBackFn(data) {
	$('#character').text(data.name);
};

$.getJSON(url, callBackFn);
