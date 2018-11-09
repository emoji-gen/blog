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

$ make       # build
$ make serve # run dev server
```

## Deployment

```
$ make build-prod # build for production
$ make deploy     # deployment
```

## License
MIT &copy; Emoji Generator
