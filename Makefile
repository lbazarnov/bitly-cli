install:
	poetry install

brain-games:
	poetry run bitly-cli

build:
	poetry build

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 bitly_cli