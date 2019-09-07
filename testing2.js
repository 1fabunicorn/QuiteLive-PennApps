const {PythonShell} = require("python-shell");
let options = {
    args: [
        "sendOpReturn",

    ]
};

PythonShell.run('src/test.py', options,
    function (err, output) {
    if (err) console.log(err);
    console.log(output);
});