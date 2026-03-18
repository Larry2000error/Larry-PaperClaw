PYTHON ?= python3
DATE ?=
DAYS ?= 2
STATS ?=
ARXIV_ID ?=
ISSUE ?=

.PHONY: install bootstrap doctor run rerun filter digest sync paper dry-run

install:
	$(PYTHON) -m pip install -r requirements.txt

bootstrap:
	./bootstrap.sh

doctor:
	$(PYTHON) scripts/cli.py doctor

run:
	$(PYTHON) scripts/cli.py run

rerun:
	$(PYTHON) scripts/cli.py run --date $(DATE) --no-notify

filter:
	$(PYTHON) scripts/cli.py filter --days $(DAYS) $(if $(DATE),--date $(DATE),) $(if $(STATS),--stats-out $(STATS),)

dry-run:
	$(PYTHON) scripts/cli.py filter --dry-run --days $(DAYS) $(if $(DATE),--date $(DATE),) $(if $(STATS),--stats-out $(STATS),)

digest:
	$(PYTHON) scripts/cli.py digest $(if $(DATE),--date $(DATE),) $(if $(STATS),--stats-json $(STATS),)

sync:
	$(PYTHON) scripts/cli.py sync

paper:
	$(PYTHON) scripts/cli.py paper $(ARXIV_ID) $(ISSUE)
