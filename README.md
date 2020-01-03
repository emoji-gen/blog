## Blog
[![CircleCI](https://circleci.com/gh/emoji-gen/blog/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/blog/tree/master)
[![dependencies Status](https://david-dm.org/emoji-gen/blog/status.svg?path=theme)](https://david-dm.org/emoji-gen/blog?path=theme)
[![devDependencies Status](https://david-dm.org/emoji-gen/blog/dev-status.svg?path=theme)](https://david-dm.org/emoji-gen/blog?path=theme&type=dev)
[![devDependencies Status](https://david-dm.org/emoji-gen/blog/dev-status.svg)](https://david-dm.org/emoji-gen/blog?type=dev)
[![Greenkeeper badge](https://badges.greenkeeper.io/emoji-gen/blog.svg)](https://greenkeeper.io/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/998b4d56553b4d49a086326e54f812af)](https://app.codacy.com/app/pinemz/blog?utm_source=github.com&utm_medium=referral&utm_content=emoji-gen/blog&utm_campaign=Badge_Grade_Settings)
[![codebeat badge](https://codebeat.co/badges/351d5ac7-cc7b-4f98-b08d-f96072f7c9a0)](https://codebeat.co/projects/github-com-emoji-gen-blog-master)
[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=green)](https://opensource.org/licenses/MIT)
[![Beerpay](https://beerpay.io/emoji-gen/blog/badge.svg?style=flat)](https://beerpay.io/emoji-gen/blog)

:memo: The Ultimate Tech Blog by Emoji Generator

![](pr/resized.jpg)<br>
<sup><sup>&copy; Alexander Batuev/123RF.COM</sup></sup>
<br>
<br>

## Requirements

- Python `$(cat .python-version)`
- [Poetry](https://python-poetry.org/)
  - If you dont't have it, try `$ pip install poetry`
- Node `$(cat .node-version)`
- [Yarn](https://yarnpkg.com/)
  - If you dont't have it, try `$ npm install -g yarn`

## Libraries

- [Pelican](https://github.com/getpelican/pelican) - Static site generator written by Python
- [Normalize.css](https://necolas.github.io/normalize.css/)

## Getting started

```bash
# Setup Python
$ poetry install

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

### Deployment

```bash
$ yarn global add firebase-tools

$ make            # Build for production
$ firebase deploy # Deployment
```

## License
MIT &copy; [Emoji Generator](https://emoji-gen.ninja/)
