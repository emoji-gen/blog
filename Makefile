PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py


.PHONY: default
default: theme-prod html-prod


.PHONY: theme
theme:
	cd theme && yarn start


.PHONY: theme-prod
theme-prod:
	cd theme && yarn run build


.PHONY: content
content:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) -r $(PELICANOPTS)


.PHONY: content-prod
content-prod:
	PYTHON_ENV=production $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)


.PHONY: clean
	rm -rf $(OUTPUTDIR)


.PHONY: serve
serve:
ifdef PORT
	@echo Serving on port $(PORT) ...
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	@echo Serving on port 8000 ...
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

