#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

df_ba = pd.read_csv('dados/consulta_cand_2018_BA.csv', encoding='latin1', sep=';')
#df_ba.set_index('NR_CANDIDATO')
df_dict = df_ba.to_dict('index')

#traz a porcentagem
def percentage(the_column, the_data=df_dict):
    #print(df_dict)
    

percentage('NR_PROCESSO')