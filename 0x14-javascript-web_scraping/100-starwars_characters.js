#!/usr/bin/node
// Script that prings all characters of a Star Wars movie
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`,
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    for (const role of JSON.parse(body).characters) {
      request(role, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  });
