#!/usr/bin/node
/*
  Returns the reversed version of a list
*/
exports.esrever = function (list) {
  const array = [];
  for (let i = list.length - 1; i >= 0; i--) {
    array.push(list[i]);
  }
  return array;
};
