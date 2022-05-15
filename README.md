# Trabalho a matéria INE5426 - Construção de Compiladores no Semestre 2022.1

## Como executar

  Utilizando o Makefile pode-se rodar o comando `make` seguido pelo nome de um dos arquivos na pasta [examples](examples), sendo eles ```baseConversions, primeNumbers, strings```
  
  **Exemplo:** `make strings`
 
 **Nota:** O comando para a utilização do python3 deve ser 'python' para executar o Makefile da maneira correta
 
 Caso seja necessário também pode-se executar o programa com o código `python3 main.py filename` onde _filename_ se refere ao nome do arquivo com a extensão ```.lcc```
 
  **Exemplo:** `python3 main.py examples/strings.lcc`


## Analisador Léxico

  O código do analisador léxico se encontra no arquivo [lexic_analyser.py](lexic_analyser.py) 
  

## Ferramentas utilizadas

  Foi feita a utilização da ferramenta _PLY (Python Lex-Yacc)_ e a biblioteca se encontram no diretório [ply](ply)
  
