# How to Run the Code

## Using Python
- To run the code, use the command: `python words_count.py`

## Using Docker
- You can execute it within a Docker container by running `docker compose up`

## Using venv
- Create a virtual environment with the command `python -m venv env`.
- Activate the virtual environment using source `env/bin/activate`.
- Use the command `pip install -r requirements.txt`
- To run tests with pytest, use the command `pytest`. 

Currently, tests can only be run using the venv solution.

# Following Steps
## Code
- Manage edge cases like capitalization and punctuation.
- Add a test library like pytest and create more tests.
- Install libraries to ensure code quality (such as mypy and ruff)
