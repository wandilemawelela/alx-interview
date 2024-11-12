#!/usr/bin/node

const axios = require('axios');

async function getMovieCharacters (movieId) {
  const filmsUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const filmResponse = await axios.get(filmsUrl);
    const characterUrls = filmResponse.data.characters;

    for (const url of characterUrls) {
      const characterResponse = await axios.get(url);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
