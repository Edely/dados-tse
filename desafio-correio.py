#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

""" 
Perguntas:
- Qual a proporção de candidatos por nível de escolaridade na Bahia?
- Distribuição de escolaridade entre os partidos?
- Distribuição de escolaridade por gênero
- Distribuição de escolaridade entre por raça
"""

#sexo, idade, estado civil, etc
#NR_CANDIDATO Númerodocandidatonaurna
#NR_CANDIDATO Númerodocandidatonaurna
#CD_CARGO
#3 - GOVERNADOR
#4 - VICE-GOVERNADOR
#5 - SENADOR
#6 - DEP FEDERAL
#7 - DEP ESTADUAIs
#9 - 1º SUPLENTE
#10 - 2º SUPLENTE

#df_br = pd.read_csv('dados/consulta_cand_2018_BRASIL.csv', encoding='latin1', sep=';')
df_ba = pd.read_csv('dados/consulta_cand_2018_BA.csv', encoding='latin1', sep=';')
df_ba_dict = df_ba.set_index('NR_CANDIDATO', inplace=True).T.to_dict('list')
print(df_ba_dict)


colunas = list(df_ba)

#cargos_code = df_ba.CD_CARGO.unique()
#cargos_desc = df_ba.DS_CARGO.unique()


#separar DataFrames por cargo
df_dep_est = pd.DataFrame(columns=colunas)
df_dep_fed = pd.DataFrame(columns=colunas)
df_gov = pd.DataFrame(columns=colunas)
df_v_gov = pd.DataFrame(columns=colunas)
df_sen = pd.DataFrame(columns=colunas)
df_pri_sup = pd.DataFrame(columns=colunas)
df_seg_sup = pd.DataFrame(columns=colunas)

dfs = {'df_dep_est': df_dep_est, 'df_dep_fed': df_dep_fed, 'df_gov': df_gov ,'df_v_gov': df_v_gov, 'df_sen': df_sen, 'df_pri_sup': df_pri_sup, 'df_seg_sup': df_seg_sup}


def add_row(row, colunas, dfs):
    cargo = row['CD_CARGO']
    df_row = pd.DataFrame([row], columns=colunas)

    
    if(cargo == 3):        
        dfs['df_dep_est'] = pd.concat([dfs['df_dep_est'], df_row])

    """ 
    elif(cargo == 4):
        pd.concat([df_v_gov,df_row])
    elif(cargo == 5):        
        pd.concat([df_sen,df_row])
    elif(cargo == 6):
        pd.concat(df_dep_fed,df_row)
    elif(cargo == 7):
        pd.concat(df_dep_est,df_row)
    elif(cargo == 9):
        pd.concat(df_pri_sup,df_row)
    elif(cargo == 10):
        pd.concat(df_seg_sup,df_row)
    """



for i, row in df_ba.iterrows():
    add_row(row, colunas, dfs)



print(dfs['df_dep_est'])