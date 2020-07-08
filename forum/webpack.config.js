module.exports = {
    mode: 'development',
    entry: "./assets/js/index.js",
    output: {
        path: __dirname + '/public/js',
        filename: '[name].js'
    },
    module: {
        rules: [
            {
                test: /\.m?js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                }
            }
        ]
    }
};