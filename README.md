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

$ make       # Build HTML
$ make serve # Run dev server
```

## Deployment

```
$ make html-prod # Build HTML for production
$ make deploy    # Deployment
```

## License
MIT &copy; Emoji Generator
