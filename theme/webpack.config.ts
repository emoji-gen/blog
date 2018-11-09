'use strict'

import { join } from 'path'

import * as webpack from 'webpack'
import * as MiniCssExtractPlugin from 'mini-css-extract-plugin'
import * as OptimizeCSSAssetsPlugin from 'optimize-css-assets-webpack-plugin'
import * as EventHooksPlugin from 'event-hooks-webpack-plugin'

const isDev = process.argv.indexOf('--watch') > -1
const mode = isDev ? 'development' : 'production'

const siteUrl = isDev ? '/blog' : 'https://emoji-gen.ninja/blog'
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
    filename: 'dist/main.js',
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
              data: `
                $site-url: ${siteUrl};
                $theme-url: ${themeUrl};
              `,
              includePaths: [ join(__dirname, 'src') ],
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
    alias: {
      'purecss': 'purecss/build/pure-min.css',
    },
  },

  // Optimization and Plugins
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  optimization: {
    minimizer: [
      new OptimizeCSSAssetsPlugin({}),
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'static/style.css',
    }),
    new EventHooksPlugin({
      run() { console.log('Mode: ' + mode) },
      watchRun() { console.log('Mode: ' + mode) },
    }),
  ],

  // Watch and WatchOptions
  //~~~~~~~~~~~~~~~~~~~~~~~~~
  watchOptions: {
    poll: true,
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
