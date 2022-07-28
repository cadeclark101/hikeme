const express = require('express')
var path = require('path');
const app = express()
const trail_checkpoints = require('./trail_data.js')

app.set('view engine', 'pug');
app.use("/public", express.static(path.join(__dirname, 'public')));

app.listen(5000, () => {
    console.log('Started Hikeme Node Network Simulator on 127.0.0.1:5000')
})

app.get("/hikemenodes", (req, res) => {
    res.render('index')
  });

app.get('/checkpoint/:checkpoint_id' ,(req, res) => {
    const id = Number(req.params.checkpoint_id)
    const trail_checkpoint = trail_checkpoints.find(trail_checkpoints => trail_checkpoints.id === id)
    res.json(trail_checkpoint)
})