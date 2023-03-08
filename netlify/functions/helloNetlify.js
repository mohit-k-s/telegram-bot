// inside `project-beef/functions/hello-netlify.js
exports.handler = async (event) => {
    return {
      statusCode: 200,
      body: "Hello, Netlify!"
    }
}