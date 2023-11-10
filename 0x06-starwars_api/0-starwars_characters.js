#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi.dev/api';

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

request(`${API_URL}/films/${movieId}/`, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(`Error: Unable to fetch data for Movie ID ${movieId}`);
    process.exit(1);
  }

  const charactersURL = JSON.parse(body).characters;
  const charactersPromises = charactersURL.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (err, _, charactersReqBody) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(charactersReqBody).name);
        }
      });
    });
  });

  Promise.all(charactersPromises)
    .then(names => console.log(names.join('\n')))
    .catch(err => console.error(err));
});

