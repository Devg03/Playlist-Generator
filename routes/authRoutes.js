const express = require('express');
const router = express.Router();
const fetch = require('node-fetch');
const querystring = require('querystring');
const randomstring = require('randomstring');

// this can be used as a seperate module
const encodeFormData = (data) => {
  return Object.keys(data)
    .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(data[key]))
    .join('&');
}

module.exports = router;

router.get("/login", async(req, res) => {
    const state = randomstring.generate(16)

    const scope = 
    'user-read-private'
    'user-read-email';

    res.redirect('https://accounts.spotify.com/authorize?' +
    querystring.stringify({
      response_type: 'code',
      client_id: process.env.CLIENT_ID,
      scope: scope,
      redirect_uri: process.env.REDIRECT_URI,
      state: state
    }));
})
