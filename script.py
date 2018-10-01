#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

df_ba = pd.read_csv('dados/consulta_cand_2018_BA.csv', encoding='latin1', sep=';')
#df_ba.set_index('NR_CANDIDATO')
df_dict = df_ba.to_dict('index')

#traz a porcentagem
def distribution(the_data, *the_columns):
    '''
    Retorna a distribuicao de candidatos pelo critério selecionado (colunas)
    '''

    total_candidatos = 0

    base = the_columns[0]
    compare_to = the_columns[1]


    values_base = set()
    values_compare = set()

    for key, candidato in the_data.items():
        values_base.add(candidato[base])
        values_compare.add(candidato[compare_to])
        total_candidatos +=1

    #print(values_base)
    #print(values_compare)
    #print(total_candidatos)

    for k, v in the_data.items():
        for column in the_columns:
            
            #print('\n')
            #print(v['NM_CANDIDATO']+ ' ' + v[base] + ' ' + v[compare_to] +'\n')


distribution(df_dict, 'DS_GRAU_INSTRUCAO', 'DS_GENERO')