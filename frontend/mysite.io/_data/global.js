let axios = require('axios');
require('dotenv').config();

function fetchSiteData(path) {
    return axios.get(process.env.API + path)
        .then(function (response) {
            console.log(response.data);
            return response.data;
        })
        .catch(function(error) {
            console.log(error)
            return {'error': 'see logs'}
        })

}

module.exports = {
   my_var: process.env.test2 || 'no var',
   site_data: fetchSiteData('sheet1'),
   currentDate: function() {
    // You can have a JavaScript function here!
    return (new Date()).toLocaleString();
  }
};