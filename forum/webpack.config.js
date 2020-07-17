const dev = process.env.NODE_ENV === "dev";
const VueLoaderPlugin = require('vue-loader/lib/plugin');

const config = {
    mode: 'development',
    entry: "./assets/js/index.js",
    output: {
        path: __dirname + '/public/js',
        filename: '[name].js'
    },
    watch: dev,
    devtool: dev ? "cheap-module-eval-source-map": "source-map",
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.m?js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                }
            },
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
        }
    },
    plugins: [
        new VueLoaderPlugin()
    ]
};

module.exports = config;