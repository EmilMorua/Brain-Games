install: # Package initialization
	poetry install

welcome_mass:
	poetry run welcome-mass

build: #Distribution assembly
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 welcome_mass

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

brain-games:
	poetry run brain-games

make lint:
	poetry run flake8 brain_games
