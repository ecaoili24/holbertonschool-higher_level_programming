#!/usr/bin/node
// Script that computes the # of tasks completed by user id
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const completeTask = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (task.userId in completeTask) {
        completeTask[task.userId] += 1;
      } else {
        completeTask[task.userId] = 1;
      }
    }
  }
  console.log(completeTask);
});
