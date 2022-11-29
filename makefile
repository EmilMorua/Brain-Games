install: # Package initialization
	poetry install

brain-games: # Start games
	poetry run brain-games

build: #Distribution assembly
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 welcome_mass

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain_gcd
