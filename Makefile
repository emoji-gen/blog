PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
PUBLICDIR=$(BASEDIR)/public
OUTPUTDIR=$(BASEDIR)/public/blog
CONFFILE=$(BASEDIR)/pelicanconf.py


.PHONY: default
default: theme-prod content-prod


.PHONY: dev
dev:
	yarn
	cd theme && yarn
	node_modules/.bin/nf start


.PHONY: theme
theme:
	cd theme && yarn start


.PHONY: theme-prod
theme-prod:
	cd theme && yarn run build


.PHONY: content
content:
	PYTHONUNBUFFERED=no $(PELICAN) $(INPUTDIR) --output $(OUTPUTDIR) --settings $(CONFFILE) -r $(PELICANOPTS)


.PHONY: content-prod
content-prod:
	PYTHON_ENV=production $(PELICAN) $(INPUTDIR) --output $(OUTPUTDIR) --settings $(CONFFILE) $(PELICANOPTS)


.PHONY: clean
	rm -rf $(OUTPUTDIR)


.PHONY: serve
serve:
	mkdir -p $(PUBLICDIR)
ifdef PORT
	@echo Serving on http://0.0.0.0:$(PORT)/blog/ ...
	cd $(PUBLICDIR) && $(PELICAN) --listen --settings $(CONFFILE) --port $(PORT)
else
	@echo Serving on http://0.0.0.0:8000/blog/ ...
	cd $(PUBLICDIR) && $(PELICAN) --listen --settings $(CONFFILE)
endif

