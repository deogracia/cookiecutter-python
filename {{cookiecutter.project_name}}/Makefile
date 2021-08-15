.PHONY: clean-pyc \
				clean-build \
				clean \
				clean-tests

help:
	@echo "Todo Help!"

clean: clean-build clean-pyc clean-tests

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-tests:
	rm -fr .nox/
	rm -f .coverage
	rm -fr .pytest_cache

clean-build:
	rm -fr build
	rm -fr dist
	rm -fr .eggs
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
