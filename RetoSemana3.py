#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:49:35 2020

@author: santiagosalamancamartinez
"""

"RETO SEMANA 3"

"Pruebas realizadas"

distancia1 = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

distancia2 = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}


ruta1 = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']
ruta2 = ['H', 'B', 'E', 'A', 'C', 'D', 'H']


"""Se obtiene la pareja con la menor demora, luego de evaluar
todas las posibilidades de la ruta establecida"""

def ruteo(distancia:dict, ruta:list ) -> dict:   
    
    distancias = distancia.items()
    
    #Validacion de los datos
    for viaje in distancias:
        
        duracion = viaje[1]        
        pareja_igual = viaje[0][0] == viaje[0][1]

        if  (pareja_igual and duracion != 0) or duracion < 0:
            return "Por favor revisar los datos de entrada."
    
    #Listas que almacenan las rutas evaluadas
    ruta_parcial = ruta.copy()
    ruta_optima = ruta.copy()
    
    #INICIO DE LAS COMBINACIONES
    
    #WHILE QUE CONTROLA LA POSICION EN LA QUE INICIAN LAS COMBINACIONES
    cambio_minimo = True
    recorrido_optimo_anterior = 0
    inicio = 1
    recorrido_optimo = 0
    
    while cambio_minimo:   
            
        #ESTE CICLO GENERA CADA UNO DE LOS PARES COMBINADOS
        for i in range(inicio, len(ruta_parcial)-2):
            iteracion1 = i + 1

            for iteracion in range(iteracion1, len(ruta_parcial) - 1):

                #Proceso del cambio de posicion    
                ruta_parcial_modificada = ruta_parcial.copy()
                
                ruta_parcial_modificada[iteracion] = ruta_parcial[i]
                ruta_parcial_modificada[i] = ruta_parcial[iteracion]
                
                recorrido_parcial = 0
                recorrido_parcial_modificado = 0
                
                for j in range(0, len(ruta_parcial)-1):
                    
                    #Calculo de la distancia en el recorrido_parcial
                    recorrido_parcial += distancia.get((ruta_parcial[j],ruta_parcial[ j + 1]))
                    
                    #Calculo de la distancia en el recorrido_parcial_modificado
                    recorrido_parcial_modificado += distancia.get((ruta_parcial_modificada[j],                  ruta_parcial_modificada[j + 1 ]))
                    
                if recorrido_optimo == 0:
                    recorrido_optimo = recorrido_parcial
            
                if recorrido_parcial_modificado < recorrido_optimo:
                    recorrido_optimo = recorrido_parcial_modificado
                    ruta_optima = ruta_parcial_modificada                
                
        ruta_parcial = ruta_optima     
        if recorrido_optimo_anterior == recorrido_optimo:
            inicio += 1
            if inicio > len(ruta):
                cambio_minimo = False
        recorrido_optimo_anterior = recorrido_optimo
    
    ruta_optima = '-'.join(ruta_optima)
    
    return {'ruta': ruta_optima, 'distancia': recorrido_optimo}
   
            
print(ruteo(distancia1, ruta1))
print(ruteo(distancia2, ruta2))
