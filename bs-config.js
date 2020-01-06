
/*
 |--------------------------------------------------------------------------
 | Browser-sync config file
 |--------------------------------------------------------------------------
 |
 | For up-to-date information about the options:
 |   http://www.browsersync.io/docs/options/
 |
 | There are more options than you see here, these are just the ones that are
 | set internally. See the website for more info.
 |
 |
 */
const { join } = require('path')
const rewriteModule = require('http-rewrite-middleware')

module.exports = {
  'ui': false,
  'files': [
    join(__dirname, 'public'),
  ],
  'watchEvents': [
    'change'
  ],
  'watch': false,
  'ignore': [],
  'single': false,
  'watchOptions': {
    'ignoreInitial': true
  },
  'server': false,
  'proxy': 'localhost:8000',
  'port': 3000,
  'middleware': [
    rewriteModule.getMiddleware([
      {
        from: '^/favicon.ico',
        to: '/theme/favicon.ico',
      },
    ]),
  ],
  'serveStatic': [],
  'ghostMode': false,
  'logLevel': 'info',
  'logPrefix': 'Browsersync',
  'logConnections': false,
  'logFileChanges': true,
  'logSnippet': true,
  'rewriteRules': [],
  'open': false,
  'browser': 'default',
  'cors': false,
  'xip': false,
  'hostnameSuffix': false,
  'reloadOnRestart': false,
  'notify': true,
  'scrollProportionally': true,
  'scrollThrottle': 0,
  'scrollRestoreTechnique': 'window.name',
  'scrollElements': [],
  'scrollElementMapping': [],
  'reloadDelay': 0,
  'reloadDebounce': 500,
  'reloadThrottle': 0,
  'plugins': [],
  'injectChanges': true,
  'startPath': null,
  'minify': false,
  'host': null,
  'localOnly': false,
  'codeSync': true,
  'timestamps': true,
  'clientEvents': [
  ],
  'socket': {
    'socketIoOptions': {
      'log': false
    },
    'socketIoClientConfig': {
      'reconnectionAttempts': 50
    },
    'path': '/browser-sync/socket.io',
    'clientPath': '/browser-sync',
    'namespace': '/browser-sync',
    'clients': {
      'heartbeatTimeout': 5000
    }
  },
  'tagNames': {
    'less': 'link',
    'scss': 'link',
    'css': 'link',
    'jpg': 'img',
    'jpeg': 'img',
    'png': 'img',
    'svg': 'img',
    'gif': 'img',
    'js': 'script'
  },
  'injectNotification': false
}
