const express = require('express');
import {PythonShell} from 'python-shell';
const exphbs = require('express-handlebars');

const app = express();

app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');
app.get('/', (req, res) => {
    res.render('index');
});

app.get('info', (req, res) => {
    res.render('info');
});

const port = process.env.PORT || 5000;

app.listen(port, () => {
    console.log(`Server listening @ ${port}`);
    console.log(`Exit app with SIGTERM (^C)`);
});
