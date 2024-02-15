#!/usr/bin/node
const request = require('request');

function sendRequest (characters, i) {
  if (characters.length === i) {
    return;
  }

  request(characters[i], (error, _, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(characters, i + 1);
    }
  });
}

const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, (error, _, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    sendRequest(characters, 0);
  }
});
