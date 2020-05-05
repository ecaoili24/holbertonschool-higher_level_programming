#!/usr/bin/node
/* Prints x times 'C is fun' */
if (!process.argv[2]) {
  console.log('Missing number of occurences');
} else if (process.argv[2] > 0) {
  for (let x = process.argv[2]; x; --x) {
    console.log('C is fun');
  }
}
