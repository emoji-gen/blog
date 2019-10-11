'use strict'

import * as fs from 'fs'
import { join } from 'path'

import * as webpack from 'webpack'
import { CleanWebpackPlugin } from 'clean-webpack-plugin'
import * as EventHooksPlugin from 'event-hooks-webpack-plugin'
import * as MiniCssExtractPlugin from 'mini-css-extract-plugin'
import * as OptimizeCSSAssetsPlugin from 'optimize-css-assets-webpack-plugin'
import * as UglifyJsPlugin from 'uglifyjs-webpack-plugin'


// Detect mode
//~~~~~~~~~~~~~~~
const isDev = process.argv.indexOf('--watch') > -1
const mode = isDev ? 'development' : 'production'

// Set SASS variables
//~~~~~~~~~~~~~~~~~~~~~~
const confPath = join(__dirname, '..', 'pelicanconf.py')
const conf = fs.readFileSync(confPath, { encoding: 'utf-8' })
const prodSiteUrl =
  conf.split('\n')
    .map(v => {
      const matches = v.match(/SITEURL\s*=\s*\'(.*\/\/.*)\'/)
      return matches ? matches[1] : null
    })
    .filter(v => !!v)

const siteUrl = isDev ? '/blog' : prodSiteUrl
const themeUrl = siteUrl + '/theme'


const configuration: webpack.Configuration = {
  mode,

  // Entry and Context
  //~~~~~~~~~~~~~~~~~~~~
  entry: './src/main.ts',
  context: __dirname,

  // Output
  //~~~~~~~~~~
  output: {
    path: __dirname,
    filename: 'dist/script.js',
  },

  // Module
  //~~~~~~~~~
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: { url: false },
          },
          {
            loader: 'postcss-loader',
          },
          {
            loader: 'sass-loader',
            options: {
              prependData: `
                $site-url: '${siteUrl}';
                $theme-url: '${themeUrl}';
              `,
              sassOptions: {
                includePaths: [ join(__dirname, 'src') ],
              },
            },
          },
        ],
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: { url: false },
          },
        ],
      },
    ],
  },

  // Resolve
  //~~~~~~~~~~~
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx'],
  },

  // Optimization and Plugins
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  optimization: {
    minimizer: [
      new UglifyJsPlugin(),
      new OptimizeCSSAssetsPlugin(),
    ],
  },
  plugins: [
    new CleanWebpackPlugin({
      cleanOnceBeforeBuildPatterns: [ 'dist/*.css', 'dist/*.js' ],
      verbose: false,
    }),
    new EventHooksPlugin({
      run() { console.log('Mode: ' + mode) },
      watchRun() { console.log('Mode: ' + mode) },
    }),
    new MiniCssExtractPlugin({
      filename: 'dist/style.css',
    }),
  ],

  // Watch and WatchOptions
  //~~~~~~~~~~~~~~~~~~~~~~~~~
  watchOptions: {
    poll: true,
    ignored: [ /node_modules/ ],
  },

  // Performance
  //~~~~~~~~~~~~~~~
  performance: {
    hints: false,
  },

  // Stats
  //~~~~~~~~
  stats: {
    entrypoints: true,
    children: false,
    colors: true,
    modules: false,
  },

}

module.exports = configuration
