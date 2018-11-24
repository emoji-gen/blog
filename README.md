## blog

## Requirements

- Python `$(cat .python-version)`
- Node `$(cat .node-version)`
- Yarn

## Libraries

- [Pelican](https://github.com/getpelican/pelican)
- [Pure](https://purecss.io/)

## Getting started

```bash
# Setup Python
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt

# Setup Node
$ yarn
$ cd theme && yarn

# Development
$ make dev
```

## Deployment

```bash
$ yarn global add firebase-tools

$ make            # Build for production
$ firebase deploy # Deployment
```

### Pygments

```bash
$ pygmentize -S trac -f html -a .highlight > theme/src/generated/pygments.css
```

## License
MIT &copy; [Emoji Generator](https://emoji-gen.ninja/)
