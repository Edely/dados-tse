Este script relaciona os dados entre duas colunas, bem como os dados de apenas uma coluna. O resultado é retornado no formato json.

Como usar o script:

-f, --file-path: Nome do arquivo a ser utilizado. Se um arquivo não é informado, o script finaliza a execução.

-c , --compare-columns: Analisa duas colunas e retorna a relação entre ambas, tomando como base a primeira. Ex: ./script -f "dados/consulta_cand_2018_BA.csv" -c DS_GENERO DS_GRAU_INSTRUCAO, retorna a quantidade de pessoas por grau de instrução e gênero

-o, --one-column: Retorna o número de ocorrências de um valor em uma coluna. Ex: ./script.py -f "dados/consulta_cand_2018_BA.csv" -o DS_GENERO retorna a quantidade de candidatos por gênero