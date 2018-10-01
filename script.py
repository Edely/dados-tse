#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import json

df_ba = pd.read_csv('dados/consulta_cand_2018_BA.csv', encoding='latin1', sep=';')
#df_ba.set_index('NR_CANDIDATO')
df_dict = df_ba.to_dict('index')

#traz a porcentagem
def distribution(the_data, *the_columns):
    '''
    Retorna a distribuicao de candidatos pelo critério selecionado (colunas)
    '''

    total_candidatos = 0

    #acessa colunas que serao comparadas
    base = the_columns[0]
    compare_to = the_columns[1]

    values_base = []
    values_compare = []


    for key, candidato in the_data.items():
        if(candidato[base] not in values_base):
            temp_base = (candidato[base] + '.')[:-1]
            values_base.append(temp_base)
        if(candidato[compare_to] not in values_compare):            
            temp_compare = (candidato[compare_to] + '.')[:-1]
            values_compare.append(temp_compare)
        total_candidatos +=1

    print(values_base)
    print(values_compare)
    #cria dictionary das colunas
    values_compare = dict.fromkeys(values_compare,0)
    dict_columns = dict.fromkeys(values_base, values_compare)


    print(dict_columns)


distribution(df_dict, 'DS_GENERO', 'DS_GRAU_INSTRUCAO')