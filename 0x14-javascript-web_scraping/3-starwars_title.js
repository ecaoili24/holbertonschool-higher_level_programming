#!/usr/bin/node
/*
   Script that prints the title of a Star Wars movie
   where episode number matches a given int
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
