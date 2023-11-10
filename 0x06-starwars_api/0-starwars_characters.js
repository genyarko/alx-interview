#!/usr/bin/node
const request = require('request');
const util = require('util');
const API_URL = 'https://swapi-api.hbtn.io/api';

const promisifiedRequest = util.promisify(request);

async function getCharacters(movieId) {
  try {
    const filmResponse = await promisifiedRequest(`${API_URL}/films/${movieId}/`);
    const charactersURL = JSON.parse(filmResponse.body).characters;

    const charactersName = await Promise.all(
      charactersURL.map(async (url) => {
        const characterResponse = await promisifiedRequest(url);
        return JSON.parse(characterResponse.body).name;
      })
    );

    console.log(charactersName.join('\n'));
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  getCharacters(movieId);
} else {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

