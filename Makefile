VENV := .venv
PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python
PYTEST := pytest -v
DEPS := requirements.txt

.PHONY: all test clean
all: $(VENV)
	$(PYTHON) app.py $(arch)

test: $(VENV)
	$(PYTEST) test_app.py 

clean:
	@test -d $(VENV) && rm -rf $(VENV) || true

%:
	@$(MAKE) --silent all arch=$@

$(VENV):
	@test -d $(VENV) || python -m venv $(VENV)
	@test -f $(DEPS) && $(PIP) install -r $(DEPS)
