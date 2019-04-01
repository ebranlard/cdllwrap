
all: test

test:
	python -m unittest discover

install:
	python -m pip install -e .

dep:
	python -m pip install -r requirements.txt

