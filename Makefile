VENV = env
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip


all:
	clear
	python3 a_maze_ing.py config.txt


install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) a_maze_ing.py config.txt


debug:
	python3 -m pdb a_maze_ing.py config.txt


clean:

	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache

lint:
	flake8 . && mypy . --warn-return-any \
	--warn-unused-ignores --ignore-missing-imports \
	--disallow-untyped-defs --check-untyped-defs

.PHONY = all install run debug clean lint