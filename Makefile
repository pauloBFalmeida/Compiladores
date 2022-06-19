# Assert python is at least 3.8.10
PYTHON_VERSION_MIN=3.8.10
PYTHON_VERSION_USED=3.9.7

# Execute any of the following tasks to run an example
bananaTest: 
	python main.py bananaTest ep2

baseConversions:
	python main.py examples/baseConversions.lcc ep2

primeNumbers:
	python main.py examples/primeNumbers.lcc ep2

strings:
	python main.py examples/strings.lcc ep2

# Use `make run <name of task>` to run that specific task
run:
	$(task)

# Use `make runall` to run all tasks
runall:
	bananaTest
	baseConversions
	primeNumbers
	strings