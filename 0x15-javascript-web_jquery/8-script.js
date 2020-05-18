$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function
      (data, status) {
    if (status === 'success') {
      const movies = data.results;
      for (const movies of data.results) {
        $('UL#list_movies').append(`<li>$(movie.title}</>`);
      }
    }
  });
});
