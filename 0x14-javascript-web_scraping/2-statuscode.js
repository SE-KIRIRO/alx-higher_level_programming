#!/usr/bin/node
// A script that display the status code of a GET request


let url = process.argv[2];
const request = require('request');

request(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
