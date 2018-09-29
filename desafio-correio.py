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

#cargos_code = df_ba.CD_CARGO.unique()
#cargos_desc = df_ba.DS_CARGO.unique()


#separar DataFrames por cargo
df_dep_est = pd.DataFrame()
df_dep_fed = pd.DataFrame()
df_gov = pd.DataFrame()
df_v_gov = pd.DataFrame()
df_sen = pd.DataFrame()
df_pri_sup = pd.DataFrame()
df_seg_sup = pd.DataFrame()

for i, row in df_ba():
