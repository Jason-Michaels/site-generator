let axios = require('axios');
require('dotenv').config();

module.exports = async function() {
    let path = 'sheet1'
    return axios.get(process.env.api-url + path)
        .then(function (response) {
            console.log(response.data);
            return response.data;
        })
        .catch(function(error) {
            console.log(error)
            return {'error': 'see logs'}
        })
}