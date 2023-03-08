const {spawn} = require('child_process');
var exec = require('child_process').exec


exports.handler = async (event) => {
  let pv = ''
  exec("which python3", (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    pv = stdout ;
    console.log(`stdout: ${stdout}`);
});
  const { message } = JSON.parse(event.body);
  const chatid = message.chat.id;
  const command = message.text;
  const python = spawn('/usr/bin/python3', ['netlify/functions/main.py', `${command}` , chatid , command]);
  python.on('error' , (err) =>{
    console.log(err);
  })
  python.stdout.on('data', function (data) {
   console.log(data.toString('utf-8'));
  });

  python.on('close', (code) => {
  console.log(`child process close all stdio with code ${code}`);
  });

  return { statusCode: 200 , body : `Sent and pv = ${pv}  ` };
};