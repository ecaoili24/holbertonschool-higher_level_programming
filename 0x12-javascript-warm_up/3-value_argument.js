#!/usr/bin/node
/* Prints the first arg passed to it */
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
