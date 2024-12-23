VENV := .venv
PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python
DEPS := requirements.txt

ARCH := amd64

$(VENV):
	@test -d $(VENV) || python -m venv $(VENV)
	@test -f $(DEPS) && $(PIP) install -r $(DEPS)

run: $(VENV)
	$(PYTHON) app.py $(ARCH)
