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

    #cria dictionary das colunas
    values_compare = dict.fromkeys(values_compare,0)
    #dict_columns = dict.fromkeys(values_base, values_compare)
    """ for k, v in values_compare.items():
        print(k)
        print(id(k))
        print('\n') """
    
    dict_columns = {column: values_compare.copy() for column in values_base}
    #print(dict_columns)
    # print(values_base)
    for k, v in dict_columns.items():
        print(k)
        print(id(k))
        print(v)
        print(id(v))
        for a, b in v.items():
            print(a)
            print(id(a))
            print(b)
            print(id(b))
        print('\n')

    # brands = ['val1', 'val2', 'val3']
    # infoBrands = {brand: {'nbOffers': 0, 'nbBestOffers': 0, 'higherPrice': []} for brand in brands}
    """ 
    print(id(dict_columns))
    for k, v in dict_columns.items():
        print(v)
        print(k)
        print(id(v))
        print('\n')
    """
    count = 0
    for k, v in the_data.items():
        #print('\n')
        #print(count)
        # print(v[base])
        # print(v[compare_to])
        
        # print(id(dict_columns[v[base]]))
        # print(dict_columns[v[base]])
        #dict_columns[v[base]][v[compare_to]] += 1
        #print(dict_columns)
        #print(id(dict_columns[v[base]]))
        #print('\n')
        if(count == 10):
            break
        count += 1
    #print(dict_columns)

distribution(df_dict, 'DS_GENERO', 'DS_GRAU_INSTRUCAO')