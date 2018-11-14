PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
PUBLICDIR=$(BASEDIR)/output
OUTPUTDIR=$(BASEDIR)/output/blog
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
	PYTHONUNBUFFERED=no $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) -r $(PELICANOPTS)


.PHONY: content-prod
content-prod:
	PYTHON_ENV=production $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)


.PHONY: clean
	rm -rf $(OUTPUTDIR)


.PHONY: serve
serve:
ifdef PORT
	@echo Serving on http://0.0.0.0:$(PORT)/blog/ ...
	cd $(PUBLICDIR) && $(PY) -m pelican.server $(PORT)
else
	@echo Serving on http://0.0.0.0:8000/blog/ ...
	cd $(PUBLICDIR) && $(PY) -m pelican.server 8000
endif

