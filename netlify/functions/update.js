const {spawn, exec} = require('child_process');
const {PythonShell} = require('python-shell')

exports.handler = async (event) => {
  const { message } = JSON.parse(event.body);
  const chatid = message.chat.id;
  const command = message.text;

  let options = {
    mode: 'text',
    pythonPath: '/opt/bin/python3',
    scriptPath: '.',
    args: [`${command}` , chatid , command]
};

  console.log(process.env.PATH);

  PythonShell.run('netlify/functions/main.py'  , options) ;

  // const python = spawn('python3', ['netlify/functions/main.py', `${command}` , chatid , command]);
  // python.on('error' , (err) =>{
  //   console.log(err);
  // })
  // python.on('close', (code) => {
  // console.log(`child process close all stdio with code ${code}`);
  // });

  return { statusCode: 200 , body : 'Sent' };
};