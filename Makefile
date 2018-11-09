PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py


.PHONY: html
html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)


.PHONY: html-prod
html-prod:
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

