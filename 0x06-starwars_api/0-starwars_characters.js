#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, { json: true }, (err, resp, body) => {
  if (err) {
    console.error('Error occurred:', err);
    return;
  }

  if (resp.statusCode === 200) {
    const characterUrls = body.characters;

    // Use Promise.all to fetch all characters in order
    const characterPromises = characterUrls.map((character) => {
      return new Promise((resolve, reject) => {
        request.get(character, { json: true }, (er, res, bdy) => {
          if (er) {
            reject(er);
          } else if (res.statusCode === 200) {
            resolve(bdy.name);
          } else {
            reject(new Error(`Failed to fetch character. Status code: ${res.statusCode}`));
          }
        });
      });
    });

    // Wait for all character requests to complete and print in order
    Promise.all(characterPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((error) => {
        console.error('Error fetching character data:', error);
      });
  } else {
    console.error('Request failed. Status code:', resp.statusCode);
  }
});
