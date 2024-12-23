VENV := .venv
PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python
PYTEST := pytest -v
DEPS := requirements.txt

DEFAULT_ARCH := amd64

.PHONY: all test clean
all: $(VENV)
	$(PYTHON) app.py $(or $(arch),$(DEFAULT_ARCH))

test: $(VENV)
	$(PYTEST) test_app.py 

clean:
	@test -d $(VENV) && rm -rf $(VENV) || true

%:
	@make --silent all arch=$@

$(VENV):
	@test -d $(VENV) || python -m venv $(VENV)
	@test -f $(DEPS) && $(PIP) install -r $(DEPS)
