## blog

## Requirements

- Python `$(cat .python-version)`

## Libraries

- [Pelican](https://github.com/getpelican/pelican)

## Getting started

```
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt

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
