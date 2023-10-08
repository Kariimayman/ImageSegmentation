const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/photo',
    createProxyMiddleware({
      target: 'http://127.0.0.1:5000',
    })
  );
};