# Assert python is at least 3.8.10
PYTHON_VERSION_MIN=3.8.10
PYTHON_VERSION_USED=3.9.7

# Execute any of the following tasks to run an example
exemplo1: 
	python main.py examples/tests/exemplo1.lcc

exemplo2:
	python main.py examples/tests/exemplo2.lcc

exemplo3:
	python main.py examples/tests/exemplo3.lcc

baseConversions:
	python main.py examples/baseConversions.lcc

primeNumbers:
	python main.py examples/primeNumbers.lcc

strings:
	python main.py examples/strings.lcc
