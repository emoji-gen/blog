## Blog
[![CircleCI](https://circleci.com/gh/emoji-gen/blog/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/blog/tree/master)
[![Requirements Status](https://requires.io/github/emoji-gen/blog/requirements.svg?branch=master)](https://requires.io/github/emoji-gen/blog/requirements/?branch=master)
[![dependencies Status](https://david-dm.org/emoji-gen/blog/status.svg?path=theme)](https://david-dm.org/emoji-gen/blog?path=theme)
[![devDependencies Status](https://david-dm.org/emoji-gen/blog/dev-status.svg?path=theme)](https://david-dm.org/emoji-gen/blog?path=theme&type=dev)
[![devDependencies Status](https://david-dm.org/emoji-gen/blog/dev-status.svg)](https://david-dm.org/emoji-gen/blog?type=dev)
[![Greenkeeper badge](https://badges.greenkeeper.io/emoji-gen/blog.svg)](https://greenkeeper.io/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/998b4d56553b4d49a086326e54f812af)](https://app.codacy.com/app/pinemz/blog?utm_source=github.com&utm_medium=referral&utm_content=emoji-gen/blog&utm_campaign=Badge_Grade_Settings)
![License](https://img.shields.io/github/license/emoji-gen/docker-node-py2.svg)
[![Beerpay](https://beerpay.io/emoji-gen/blog/badge.svg?style=flat)](https://beerpay.io/emoji-gen/blog)

:memo: The Ultimate Tech Blog by Emoji Generator
<br>
<br>

## Requirements

- Python `$(cat .python-version)`
- Node `$(cat .node-version)`
- Yarn

## Libraries

- [Pelican](https://github.com/getpelican/pelican)
- [Normalize.css](https://necolas.github.io/normalize.css/)

## Getting started

```bash
# Setup Python
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt

# Setup Node
$ yarn
$ cd theme && yarn

# Setup submodules
$ git submodule update --init --recursive

# Development
$ make dev
```

## Development
### Pygments

```bash
$ pygmentize -S trac -f html -a .highlight > theme/src/generated/pygments.css
```

## Deployment

```bash
$ yarn global add firebase-tools

$ make            # Build for production
$ firebase deploy # Deployment
```

## License
MIT &copy; [Emoji Generator](https://emoji-gen.ninja/)
