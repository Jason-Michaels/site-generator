require('dotenv').config();

module.exports = {
   my_var: process.env.test2 || 'no var',
   currentDate: function() {
    // You can have a JavaScript function here!
    return (new Date()).toLocaleString();
  }
};