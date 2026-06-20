install:
	pip install -r requirements.txt

test:
	pytest

lint:
	flake8 src tests

format:
	black src tests

run:
	python src/etl/loader.py