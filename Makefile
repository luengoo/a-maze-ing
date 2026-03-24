all:
	python3 -m flake8
	python3 a_maze_ing.py config.txt

install:
	pip install -r requirements.txt

run:
	python3 maze_algorithm.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

clean:

	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache

lint:
	python3 -m flake8 && mypy . --warn-return-any
	--warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs
	--check-untyped-defs

.PHONY = all install run debug clean lint