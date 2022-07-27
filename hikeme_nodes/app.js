const express = require('express')
const app = express()

app.listen(5000, () => {
    console.log('server is listening on port 5000')
})

app.get('/trail_checkpoints', (req, res) => {
    res.json(trail_checkpoints)
})