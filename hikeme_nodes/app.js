const express = require('express')
const app = express()
const trail_checkpoints = require('./trail_data.js')

app.listen(5000, () => {
    console.log('server is listening on port 5000')
})

app.get('/checkpoint/:checkpoint_id' ,(req, res) => {
    const id = Number(req.params.checkpoint_id)
    const trail_checkpoint = trail_checkpoints.find(trail_checkpoints => trail_checkpoints.id === id)
    res.json(trail_checkpoint)
})