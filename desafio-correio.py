#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

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

count = 0

def add_row(row, colunas):
    cargo = row['CD_CARGO']
    df_row = pd.DataFrame([row], columns=colunas)

    if(cargo == 3):        
        df_dep_est.append(dict(row), ignore_index=True)
    elif(cargo == 4):
        df_v_gov.append(dict(row), ignore_index=True)
    if(cargo == 5):        
        df_dep_est.append(dict(row), ignore_index=True)
    if(cargo == 4):
        df_v_gov.append(dict(row), ignore_index=True)

for i, row in df_ba.iterrows():
    count += 1
    add_row(row, colunas)
    


