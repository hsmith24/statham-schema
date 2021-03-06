.PHONY: build clean install test lint unit type integration docs publish

RUN_CLEAN_TEST:=bash run_test.sh -c
CHECK_VIRTUALENV:=python -c "import sys;assert sys.prefix != sys.base_prefix"


help: ## Prints this help/overview message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-17s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: ## Cleans all testing metadata and .pyc files.
	$(RUN_CLEAN_TEST)
	make -C docs clean

install: ## Installs all dependencies
	$(CHECK_VIRTUALENV) || (echo "Not inside a virtualenv, aborting."; exit 1)
	pip install -r requirements.txt -r requirements-test.txt

test: install ## Runs all tests
	$(RUN_CLEAN_TEST) -a

lint: install ## Runs linter on source code and tests.
	$(RUN_CLEAN_TEST) -l

unit: install ## Runs all unit tests with coverage test.
	$(RUN_CLEAN_TEST) -u

type: install ## Runs type checker. Does not update requirements or rules.
	$(RUN_CLEAN_TEST) -t

integration: ## Runs some long running tests against external JSON Schemas.
	INTEGRATION=true pytest -v -s tests/test_schema_store.py

build: test ## Creates a new build for publishing. Deletes previous builds.
	pip install -U setuptools wheel
	python setup.py sdist bdist_wheel

docs: clean ## Builds the documentation.
	make -C docs html

publish: test ## Tags release, builds and publishes to pypi
	python release.py
	pip install -U setuptools wheel twine
	python setup.py sdist bdist_wheel
	twine upload dist/*