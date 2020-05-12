#!/usr/bin/node
// Script that concats two files
if (process.argv.length !== 5) {
  console.error('Incorrect num of arguments');
} else {
  const fs = require('fs');
  const targetFile = process.argv[4];
  let str = '';
  str = str.concat(fs.readFileSync(process.argv[2]), fs.readFileSync(process.argv[3]));
  fs.writeFile(targetFile, str, (err) => {
    if (err) console.log(err);
  });
}
