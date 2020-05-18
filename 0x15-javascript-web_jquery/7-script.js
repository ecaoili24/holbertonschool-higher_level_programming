$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function
	(data, status) {
    if (status === 'success') {
      $('#character').text(data.name);
    }
  });
});
