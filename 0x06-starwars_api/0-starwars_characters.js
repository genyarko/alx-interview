#!/usr/bin/node
const request = require('request-promise-native');
const API_URL = 'https://swapi-api.hbtn.io/api';

async function getCharacterNames(filmId) {
  try {
    const filmData = await request(`${API_URL}/films/${filmId}/`);
    const charactersURL = JSON.parse(filmData).characters;
    const characterNamesPromises = charactersURL.map(async url => {
      const characterData = await request(url);
      return JSON.parse(characterData).name;
    });
    const characterNames = await Promise.all(characterNamesPromises);
    console.log(characterNames.join('\n'));
  } catch (err) {
    console.error(err);
  }
}

if (process.argv.length > 2) {
  getCharacterNames(process.argv[2]);
}
