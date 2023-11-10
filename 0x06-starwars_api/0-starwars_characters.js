#!/usr/bin/node

const request = require('request');

const API_URL = 'https://swapi.dev/api';

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

function getRequestPromise(url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

function getMovieCharacters(movieId) {
  const movieUrl = `${API_URL}/films/${movieId}/`;

  getRequestPromise(movieUrl)
    .then(movieData => {
      const charactersURL = movieData.characters;
      const charactersPromises = charactersURL.map(url => getRequestPromise(url));

      return Promise.all(charactersPromises);
    })
    .then(charactersData => {
      const characterNames = charactersData.map(data => data.name);
      console.log(characterNames.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

getMovieCharacters(movieId);
