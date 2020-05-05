#!/usr/bin/node
/* Prints the first arg if it can be converted */
if (!parseInt(process.argv[2])) { /* parseInt: built in that converts str to int */
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(process.argv[2]));
}
