const { Spot } = require('@binance/connector')
require('dotenv').config();

const apiKey = process.env.API_KEY
const apiSecret = process.env.SECRET_KEY
const client = new Spot(apiKey, apiSecret, { baseURL: 'https://api3.binance.com'})

// Get account information
client.account()
    .then(response => client.logger.log(response.data))
    .catch(error => client.logger.error(error.message))

client.futuresLoanInterestHistory()
    .then(response => client.logger.log(response.data))
    .catch(error => client.logger.error(error.message))