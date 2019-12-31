PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
PUBLICDIR=$(BASEDIR)/public
OUTPUTDIR=$(BASEDIR)/public
CONFFILE=$(BASEDIR)/pelicanconf.py


.PHONY: default
default: theme-prod content-prod


.PHONY: dev
dev:
	yarn
	cd theme && yarn
	node_modules/.bin/nf start


.PHONY: theme
theme: yarn-install
	cd theme && yarn start


.PHONY: theme-prod
theme-prod: yarn-install
	cd theme && yarn run build


.PHONY: content
content: poetry-install
	PYTHONUNBUFFERED=no poetry run $(PELICAN) $(INPUTDIR) --output $(OUTPUTDIR) --settings $(CONFFILE) -r $(PELICANOPTS)


.PHONY: content-prod
content-prod: poetry-install
	PYTHON_ENV=production poetry run $(PELICAN) $(INPUTDIR) --output $(OUTPUTDIR) --settings $(CONFFILE) $(PELICANOPTS)


.PHONY: poetry-install
poetry-install:
	poetry install


.PHONY: yarn-install
yarn-install:
	yarn install


.PHONY: clean
	rm -rf $(OUTPUTDIR)


.PHONY: serve
serve:
	mkdir -p $(PUBLICDIR)
ifdef PORT
	@echo Serving on http://0.0.0.0:$(PORT)/ ...
	cd $(PUBLICDIR) && $(PY) -m http.server $(PORT)
else
	@echo Serving on http://0.0.0.0:8000/ ...
	cd $(PUBLICDIR) && $(PY) -m http.server 8000
endif

