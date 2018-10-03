#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from slugify import slugify
import json, argparse, sys, os

#traz a porcentagem
def compare_columns(the_data, the_columns):
    '''
    Retorna a relacao entre as duas primeiras colunas inseridas
    '''

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


    values_compare = dict.fromkeys(values_compare,0)
    dict_columns = {column: values_compare.copy() for column in values_base}

    count = 0
    for k, v in the_data.items():
        dict_columns[str(v[base])][str(v[compare_to])] += 1
    save_json(dict_columns, the_columns)

def quant_column(the_data, one_column):
    '''
    Retorna o número de ocorrencias em uma coluna
    '''
    chave = one_column[0]

    dict_one = {}
    for k, v in the_data.items():
        dict_one[v[chave]] = dict_one.get(v[chave], 0) + 1
    save_json(dict_one, one_column)
        
def save_json(dict_json, the_columns):
    '''
    Salva o dictionary inserido em formato json
    '''
    
    folder = os.path.dirname(__file__)+"/dados_exportados/"
    if(not os.path.isdir(folder)):
        os.mkdir(folder)

    name_columns = UF+"_"
    i = 0

    for column in the_columns:
        if(i != 0):
            name_columns += "_"
        name_columns += column
        i += 1
    name = slugify(name_columns)

    file_json = open(folder+name+".json", 'w+', encoding='utf')
    dict_export = json.dumps(dict_json, ensure_ascii=False)
    file_json.write(dict_export)
    file_json.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file-path', help="Lê arquivo csv.")
    parser.add_argument('-c', '--compare-columns', nargs='+', help="Cria uma relação entre duas colunas", default="")
    parser.add_argument('-o', '--one-column', nargs='+', help="Analiza número de ocorrências em uma coluna", default="")
    
    args = parser.parse_args()
    
    if(not args.file_path):
        print("Arquivo csv não foi informado. Terminando script.")
        sys.exit(0)
    else:
        base_name = os.path.basename(args.file_path.split('.')[0])
        global UF
        if('perfil' not in base_name):
            UF = base_name[19:]
        else:
            UF = 'perfil_eleitorado'
        df = pd.read_csv(args.file_path, encoding='latin1', sep=';')
        df_dict = df.to_dict('index')

    if(args.compare_columns):
        colunas = args.compare_columns
        compare_columns(df_dict, colunas)
        sys.exit()

    if(args.one_column):
        coluna = args.one_column
        quant_column(df_dict, coluna)
        sys.exit()
    