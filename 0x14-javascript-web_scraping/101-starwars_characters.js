#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const role = JSON.parse(body).characters;
    print(role, 0);
  }
});

function print (array, i) {
  if (i >= array.length) {
    return;
  }
  request.get(array[i], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
    return print(array, i + 1);
  });
}
