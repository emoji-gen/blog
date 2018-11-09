## blog

## Requirements

- Python `$(cat .python-version)`
- Node `$(cat .node-version)`

## Libraries

- [Pelican](https://github.com/getpelican/pelican)

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
$ make        # Build for production
$ make deploy # Deployment
```

## License
MIT &copy; Emoji Generator
