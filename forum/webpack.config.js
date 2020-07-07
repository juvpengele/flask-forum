module.exports = {
    mode: 'development',
    entry: "./assets/js/index.js",
    output: {
        path: __dirname + '/public/js',
        filename: '[name].js'
    }
};