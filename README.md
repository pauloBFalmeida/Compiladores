# Trabalho da matéria INE5426 - Construção de Compiladores - Semestre 2022.1

## Como executar

  Utilizando o Makefile pode-se rodar o comando `make` seguido pelo tipo de análise, ```syntactic``` ou ```lexical```, que se deseja realizar e o nome de um dos arquivos na pasta [examples](examples) precedido de um *underscore*, sendo eles ```baseConversions, primeNumbers, strings```
  
  **Exemplo:** `make syntactic_strings`
 
 **Nota:** O comando para a utilização do python3 deve ser 'python' para executar o Makefile da maneira correta
 
 Caso seja necessário também pode-se executar o programa com o código `python3 main.py <filename> <analysis>` onde _filename_ se refere ao nome do arquivo com a extensão ```.ccc``` e _analysis_ se refere ao tipo de análise que se deseja realizar.
 
  **Exemplo:** `python3 main.py examples/strings.ccc syntactic`


## Analisador Léxico

  O código do analisador léxico se encontra no arquivo [lexical_analyzer.py](compiler/lexical_analyzer.py).
  
## Analisador Sintático

  O código do analisador sintático se encontra no arquivo [sintactic_analyzer.py](compiler/syntactic_analyzer.py).
  


## Ferramentas utilizadas

  Foi feita a utilização da ferramenta _PLY (Python Lex-Yacc)_. Como algumas alterações foram realizadas, o código fonte da biblioteca se encontra no diretório [compiler/ply](compiler/ply/).
  
