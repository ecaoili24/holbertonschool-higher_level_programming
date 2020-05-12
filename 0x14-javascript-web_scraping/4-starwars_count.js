#!/usr/bin/node
/*
   Script that prints the # of movies where
   the character "Wedge Antilles" is present
*/
const request = require('request');
let count = 0;

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const film of JSON.parse(body).results) {
      for (const role of film.characters) {
        if (role.includes('18')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
