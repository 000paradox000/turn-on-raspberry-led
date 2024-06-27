# =============================================================================
# Local

lint-local:
	pre-commit run --all-files
	pre-commit run --all-files

lint-update-local:
	pre-commit autoupdate

install-requirements-local:
	pip install --upgrade pip
	pip install -r requirements/local.txt

run-local:
	python main.py

# =============================================================================
# PI

install-requirements-pi:
	pip install --upgrade pip
	pip install -r requirements/pi.txt

run-pi:
	python main.py

test-pi:
	python -m pytest -ra -vv

coverage-pi:
	coverage run -m pytest -ra -vv
	coverage report -m
