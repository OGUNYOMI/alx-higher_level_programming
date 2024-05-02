#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error("Error fetching movie data:", error);
    return;
  }
  
  try {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    
    Promise.all(characters.map(getCharacterName))
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error("Error fetching character data:", error);
      });
    
  } catch (parseError) {
    console.error("Error parsing movie data:", parseError);
  }
});

function getCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        try {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        } catch (parseError) {
          reject(parseError);
        }
      }
    });
  });
}
