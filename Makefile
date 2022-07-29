# Assert python is at least 3.8.10
PYTHON_VERSION_MIN=3.8.10
PYTHON_VERSION_USED=3.9.7


# Execute any of the following tasks to run a Lexical Analyzer example
lexical_bananaTest: 
	python main.py examples/bananaTest.ccc lexical

lexical_baseConversions:
	python main.py examples/baseConversions.ccc lexical

lexical_primeNumbers:
	python main.py examples/primeNumbers.ccc lexical

lexical_strings:
	python main.py examples/strings.ccc lexical


# Execute any of the following tasks to run a Syntactic Analyzer example
syntactic_bananaTest: 
	python main.py examples/bananaTest.ccc syntactic

syntactic_baseConversions:
	python main.py examples/baseConversions.ccc syntactic

syntactic_primeNumbers:
	python main.py examples/primeNumbers.ccc syntactic

syntactic_strings:
	python main.py examples/strings.ccc syntactic


# Execute any of the following tasks to run a Semantic Analyzer example
semantic_bananaTest: 
	python main.py examples/bananaTest.ccc semantic

semantic_baseConversions:
	python main.py examples/baseConversions.ccc semantic

semantic_primeNumbers:
	python main.py examples/primeNumbers.ccc semantic

semantic_strings:
	python main.py examples/strings.ccc semantic