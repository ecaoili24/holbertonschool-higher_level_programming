#!/usr/bin/node
/*
  Imports a dict of occurrences by user id
  and computes a dict of user ids by occurrence
*/
const dict = require('./101-data').dict;

const obj = {};
for (const [key, val] of Object.entries(dict)) {
  if (!(val in obj)) {
    obj[val] = [key];
  } else {
    obj[val].push(key);
  }
}
console.log(obj);
