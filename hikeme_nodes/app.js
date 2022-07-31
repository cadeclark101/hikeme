const express = require('express')
var path = require('path');
const app = express();
const trail_data = require('./static/js/trail_data.js');

app.set('view engine', 'pug');
app.use("/static", express.static('./static/'));
app.use("/public", express.static(path.join(__dirname, 'public')));

app.listen(5000, () => {
    console.log('Started Hikeme Node Network Simulator on 127.0.0.1:5000')
})

app.get("/hikemenodes", (req, res) => {
    res.render('index');
});
