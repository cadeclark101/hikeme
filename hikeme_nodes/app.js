const express = require('express')
const app = express()
const trail_checkpoints = require('./trail_data.js')

app.listen(5000, () => {
    console.log('server is listening on port 5000')
})

app.get('/', (req, res) => {
    res.json(trail_checkpoints)
})