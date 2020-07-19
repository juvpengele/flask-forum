const dev = process.env.NODE_ENV === "dev";
const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const buildDirectory = path.resolve(__dirname);

const config = {
    mode: dev ? 'development' : 'production',
    entry: "./assets/js/index.js",
    output: {
        path: buildDirectory + '/public/js',
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
            {
                test: /\.scss$/,
                loader: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            publicPath: './assets/css',
                            hmr: dev
                        },
                    },
                    'css-loader',
                    'sass-loader'
                ]
            },
            {
                test: /\.css$/,
                loader: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            publicPath: './assets/css',
                        },
                    },
                    'css-loader'
                ]
            }
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.common.js',
        }
    },
    plugins: [
        new VueLoaderPlugin(),
        new MiniCssExtractPlugin({
            filename: '../css/[name].css',
        })
    ]
};

module.exports = config;