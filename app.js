const express = require('express');
const {PythonShell} = require("python-shell");
let exec = require('child_process').exec;
const exphbs = require('express-handlebars');

const app = express();


app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

function execute(command, callback){
    exec(command, function(error, stdout, stderr){ callback(stdout); });
}


let a = function(callback){
    execute('src/dash-cli getrawtransaction '  + tx, function(name){
        execute("git config --global user.email", function(email){
            callback({ name: name.replace("\n", ""), email: email.replace("\n", "") });
        });
    });
};

app.get('/tx/:transaction', (req, res) => {
    console.log(getRawTx(req.params.transaction));
    //console.log(getRawTx(req.params.transaction));
    //res.send(getRawTx(req.params.transaction))
});

app.get('info', (req, res) => {
    res.render('info');
});

const port = process.env.PORT || 5000;

app.listen(port, () => {
    console.log(`Server listening @ ${port}`);
    console.log(`Exit app with SIGTERM (^C)`);
});
