## Blog
[![CircleCI](https://circleci.com/gh/emoji-gen/blog/tree/master.svg?style=shield)](https://circleci.com/gh/emoji-gen/blog/tree/master)
[![License](https://img.shields.io/static/v1?label=License&message=MIT&color=green)](https://opensource.org/licenses/MIT)

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
