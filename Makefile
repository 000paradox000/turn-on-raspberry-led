lint:
	pre-commit run --all-files
	pre-commit run --all-files

lint-update:
	pre-commit autoupdate

install-requirements:
	pip install -r requirements.txt

run:
	python main.py

test:
	python -m pytest -ra -vv
