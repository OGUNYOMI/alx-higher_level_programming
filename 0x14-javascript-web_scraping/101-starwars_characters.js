#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  try {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    
    const characterRequests = characters.map(character => {
      return new Promise((resolve, reject) => {
        request.get(character, (error, response, body) => {
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
    });
    
    Promise.all(characterRequests)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
    
  } catch (parseError) {
    console.error(parseError);
  }
});
