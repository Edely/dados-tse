#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from slugify import slugify
import json

df_ba = pd.read_csv('dados/consulta_cand_2018_BA.csv', encoding='latin1', sep=';')
#df_ba.set_index('NR_CANDIDATO')
df_dict = df_ba.to_dict('index')

#traz a porcentagem
def compare_columns(the_data, *the_columns):
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
            temp_base = (str(candidato[base]) + '.')[:-1]
            values_base.append(temp_base)
        if(candidato[compare_to] not in values_compare):            
            temp_compare = (str(candidato[compare_to]) + '.')[:-1]
            values_compare.append(temp_compare)
        total_candidatos +=1


    values_compare = dict.fromkeys(values_compare,0)
    dict_columns = {column: values_compare.copy() for column in values_base}

    count = 0
    for k, v in the_data.items():
        dict_columns[str(v[base])][str(v[compare_to])] += 1
    print_json(dict_columns, the_columns)

def print_json(dict_json, the_columns):
    name = slugify(the_columns[0] +'-'+the_columns[1])
    
    file_json = open(name+".json", 'w+')
    
    dict_export = json.dumps(dict_json, ensure_ascii=False)
    file_json.write(dict_export)
    #print(dict_export)
    file_json.close()

#compare_columns(df_dict, 'DS_GENERO', 'DS_GRAU_INSTRUCAO')
#compare_columns(df_dict, 'DS_GENERO', 'DS_COR_RACA')
#compare_columns(df_dict, 'SG_PARTIDO', 'DS_GENERO')
#compare_columns(df_dict, 'SG_PARTIDO', 'DS_GRAU_INSTRUCAO')
#compare_columns(df_dict, 'DS_GRAU_INSTRUCAO', 'DS_COR_RACA')

compare_columns(df_dict, 'DS_GENERO', 'CD_GENERO')