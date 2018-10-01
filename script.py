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
            values_base.append(candidato[base])
        if(candidato[compare_to] not in values_compare):
            values_compare.append(candidato[compare_to])
        total_candidatos +=1

    print(candidato[base])
    print(candidato[compare_to])
    #cria dictionary das colunas
    values_compare = dict.fromkeys(values_compare,0)
    dict_columns = dict.fromkeys(values_base, values_compare)

    # dict_columns = json.dumps(dict_columns)
    # the_data = json.dumps(the_data)
    #print(dict_columns)

    #dict_values = dict(zip(values_base, values_compare))

    #print(dict_values)
    #print(values_base)
    #print(values_compare)
    #print(total_candidatos)

    count = 0
    for k, v in the_data.items():
        #dict_columns[v[base]][v[compare_to]] += 1
        #print(dict_columns)
        print('\n')
        #print(v)
        #print(dict_columns[v[base]])
        #print(dict_columns[v[base]][v[compare_to]])
        if(v[compare_to] in dict_columns[v[base]]):
            
            print(count)
            print(v[base])
            print(v[compare_to])
            print(dict_columns[v[base]])
            #print(dict_columns)
            dict_columns[v[base]][v[compare_to]] += 1
            print(dict_columns[v[base]])
            #print(dict_columns)
            

        #dict_columns[v[base][v[compare_to]]] += 1

        # print(dict_columns[v[base][v[compare_to]]])
        # print("====")
        # print(dict_columns)
        #print(dict_columns[v[base]])
        #print(dict_columns[v[base]][v[compare_to]])

        # for column, value in dict_columns.items():

        #     print(value)

        '''for key, value in v.items():
            print(key + ': ' + str(value))
            print('\n')
            if value in dict_columns:
                print(dict_columns[])
        '''
        print('\n')
        #    dict_columns[v[base]][v[compare_to]]

        #print(dict_columns)
        #print(dict_columns[v])

        

        #print(dict_columns[v[base]][v[compare_to]])
        if(count == 10):
            break
        count += 1
            
            
            

    # for k, v in the_data.items():
    #     for column in the_columns:
    #     


distribution(df_dict, 'DS_GENERO', 'DS_GRAU_INSTRUCAO')