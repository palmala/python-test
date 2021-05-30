clean:
	rm -rf .coverage .pytest_cahce htmlcov

init:
	pip install -r requirements.txt

test_basic:
	py.test tests/tests_basic.py --cov=.

test: test_basic
.PHONY: clean init test test_basic