#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:23:41 2020

@author: santiagosalamancamartinez
"""

import pandas as pd

#Nombre del archivo
ruta_archivo_csv = str('owid-covid-data.csv')
import pandas as pd
def caso_who(ruta_archivo_csv: str) -> dict:
    
    #Validacion del tipo de archivo
    tipo = ruta_archivo_csv.split(".")
    compara = tipo[-1] != "csv"
    if compara:
        return "Extensión inválida."
    
    #Lectura del archivo csv
    try:

        dfinicio = pd.read_csv(ruta_archivo_csv)

        df = pd.DataFrame({'date': dfinicio['date'],
                           'continent': dfinicio['continent'],
                           'population': dfinicio['population'],
                           'hospital_beds_per_thousand': dfinicio['hospital_beds_per_thousand'],
                           'total_cases_per_million': dfinicio['total_cases_per_million']})
        
        
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace = True)
        
        #Calculo de camas
        df['camas'] = df['population'] * df['hospital_beds_per_thousand']/1000
        
        #Calculo de casos
        df['total_casos'] = df['population'] * df['total_cases_per_million'] /1000000
        
        #Calculo de la razon entre total de casos y total de camas
        df['razon'] = df['total_casos']/df['camas']
        
        #Agrupar por continente
        resultados = df.groupby(['date','continent'])['razon'].mean().reset_index()
        
        pivotResultados = resultados.pivot(index='date', columns='continent', values='razon')
        
        dictResultados = pivotResultados.to_dict()
        
    except:
        return "Error al leer el archivo de datos."
        
    return dictResultados

monitoreo = caso_who(ruta_archivo_csv)
