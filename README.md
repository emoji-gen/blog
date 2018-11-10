## blog

## Requirements

- Python `$(cat .python-version)`
- Node `$(cat .node-version)`

## Libraries

- [Pelican](https://github.com/getpelican/pelican)
- [Pure](https://purecss.io/)

## Getting started

```
# Setup Python
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt

# Setup Node
$ cd theme && yarn

# Build
$ make theme   # Build theme with auto-reload
$ make content # Build content with auto-reload
$ make serve   # Run dev server
```

## Deployment

```
$ npm install -g firebase-tools

$ make            # Build for production
$ firebase deploy # Deployment
```

## License
MIT &copy; [Emoji Generator](https://emoji-gen.ninja/)
