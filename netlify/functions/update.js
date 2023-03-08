const {spawn} = require('child_process');
const messageParts = require("../../messageParts")

exports.handler = async (event) => {
  const { message } = JSON.parse(event.body);
  const chatid = message.chat.id;
  const { command, botName, extra } = messageParts(message.text);

  const python = spawn('python3', ['./main.py', `${command}` , chatid , command ]);
  python.on('error' , (err) =>{
    console.log(err);
  })
  python.stdout.on('data', function (data) {
   console.log('Pipe data from python script ...');
   console.log(data);
  });
  python.on('close', (code) => {
  console.log(`child process close all stdio with code ${code}`);
  });

  return { statusCode: 200 };
};