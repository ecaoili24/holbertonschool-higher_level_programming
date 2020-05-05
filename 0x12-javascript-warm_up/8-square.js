#!/usr/bin/node
/* Prints a square */
const size = process.argv[2];

if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else if (size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
