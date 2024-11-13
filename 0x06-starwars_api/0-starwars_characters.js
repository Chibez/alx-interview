#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
    return;
  }
  
  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  characterUrls.forEach(url => {
    request(url, function (error, response, body) {
      if (error) {
        console.log('Error:', error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

