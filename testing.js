const {PythonShell} = require("python-shell");
const { exec } = require('child_process');




exec('src/dash-cli getrawtransaction', (err, stdout, stderr) => {
  if (err) {
    //some err occurred
    console.error(err)
  } else {
   // the *entire* stdout and stderr (buffered)
   console.log(`stdout: ${stdout}`);
   console.log(`stderr: ${stderr}`);
  }
});
let options = {
    args: [
        "sendOpReturn",
        "hello"
    ]
};

PythonShell.run('src/opReturn.py', options,
    function (err, output) {
    if (err) console.log(err);
    console.log(output);
});