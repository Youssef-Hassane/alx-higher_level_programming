const url = "https://swapi-api.alx-tools.com/api/films/?format=json"

/* Get data from url */
$.getJSON(url, callBackFunction);

/* Callback function to get data */
function callBackFunction(data) {
	let movieName = data.results;

	movieName.forEach(appendMovie);
}

/* Callback function to append data */
function appendMovie(movie) {
	$("#list_movies").append(`<li>${movie.title}</li>`);
}
