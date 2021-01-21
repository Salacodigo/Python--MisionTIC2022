#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:29:01 2020

@author: santiagosalamancamartinez
"""
'''VARIABLES UTILIZADAS

            id_prestamo -> str
            casado -> str
            dependientes -> int/str
            educacion -> str
            independiente -> str
    (i_d)   ingreso_deudor -> float
    (i_c)   ingreso_codeudor -> float
    (c_p)   cantidad_prestamo -> float
    (p_p)   plazo_prestamo -> int
            historia_credito -> int
            tipo_propiedad -> str


'''

dict1 = {'id_prestamo' : "RETOS2_001", 
         'casado' : "Si",
         'dependientes' : 1,
         'educacion' : "Graduado",
         'independiente' : "Si",
         'ingreso_deudor': 4692,
         'ingreso_codeudor': 0,
         'cantidad_prestamo': 106,
         'plazo_prestamo': 360,
         'historia_credito': 1,
         'tipo_propiedad': "Rural",
         }

dict2 = {'id_prestamo' : "RETOS2_002", 
         'casado' : "No",
         'dependientes' : "3+",
         'educacion' : "No Graduado",
         'independiente' : "No",
         'ingreso_deudor': 1830,
         'ingreso_codeudor': 0,
         'cantidad_prestamo': 100,
         'plazo_prestamo': 360,
         'historia_credito': 0,
         'tipo_propiedad': "Urbano",
         }

dict3 = {'id_prestamo' : "RETOS2_003", 
         'casado' : "No",
         'dependientes' : 0,
         'educacion' : "No Graduado",
         'independiente' : "No",
         'ingreso_deudor': 3748,
         'ingreso_codeudor': 1668,
         'cantidad_prestamo': 110,
         'plazo_prestamo': 360,
         'historia_credito': 1,
         'tipo_propiedad': "Semiurbano",
         }
dict4 = {'id_prestamo': 'RETOS2_012', 
         'casado': 'Si', 
         'dependientes': 1, 
         'educacion': 'Graduado',
         'independiente': 'Si',
         'ingreso_deudor': 11500,
         'ingreso_codeudor': 0, 
         'cantidad_prestamo': 286, 
         'plazo_prestamo': 360, 
         'historia_credito': 0, 
         'tipo_propiedad': 'Urbano'}

dict5 = {'id_prestamo': 'RETOS2_011', 
         'casado': 'No', 
         'dependientes': "3+", 
         'educacion': 'Graduado',
         'independiente': 'No',
         'ingreso_deudor': 3083,
         'ingreso_codeudor': 0, 
         'cantidad_prestamo': 255, 
         'plazo_prestamo': 360, 
         'historia_credito': 1, 
         'tipo_propiedad': 'Rural'}


def prestamo(informacion: dict) -> dict:
      
    
        i_d = float(informacion['ingreso_deudor'])
        i_c = float(informacion['ingreso_codeudor'])
        c_p = float(informacion['cantidad_prestamo'])
        #p_p = int(informacion['plazo_prestamo'])
        
        #id_prestamo = informacion['id_prestamo']
        casado = informacion['casado']
        
        try:
            dependientes = int(informacion['dependientes'][0])
        except:
            dependientes = int(informacion['dependientes'])
            
        educacion = str(informacion['educacion'])
        independiente = str(informacion['independiente'])
        historia_credito = int(informacion['historia_credito'])
        tipo_propiedad  = str(informacion['tipo_propiedad'])
        
         
        
        SeAprueba = False
        
        if historia_credito == 1:
            bi_c = i_c > 0
            bi_d = (i_d/9) > c_p
            
            if bi_c and bi_d:
                SeAprueba = True
            
            else:        
                bdep = dependientes > 2  
                bind = independiente == "Si"
                
                if bdep and bind:
                   bi_c = (i_c/12) > c_p
        
                   if bi_c:
                       SeAprueba = True
                   else:
                       SeAprueba = False
               
                else:
        
                    if c_p <200:
                        SeAprueba = True
                    else:
                        SeAprueba = False
                    
        else:
            if independiente == "Si":
                bcas = casado == "Si"
                bdep = dependientes > 1
                
                if not (bcas and bdep):
                    bi_d = (i_d/10) > c_p
                    bi_c = (i_c/10) > c_p
                    
                    if bi_d or bi_c:
        
                        if c_p < 180:
                            SeAprueba = True
                        else:
                            SeAprueba = False
                    
                    else:
                        SeAprueba = False
                        
                else:
                    SeAprueba = False
        
            else:
                bprop = tipo_propiedad == "Semiurbano"
                bdep = dependientes < 2
                
                if (not bprop) and bdep:
                    
                    if educacion == "Graduado":
                        bi_d = (i_d/11) > c_p
                        bi_c = (i_c/11) > c_p
                        
        
                        if bi_d and bi_c:
                            SeAprueba = True
                        
                        else:
                            SeAprueba = False
                    
                    else:
                        SeAprueba = False
                
                else:
                    SeAprueba = False
        
        resultado = {'id_prestamo' : informacion['id_prestamo'], 'aprobado' : SeAprueba}

        return (resultado)

a = prestamo(dict1)
b = prestamo(dict2)
c = prestamo(dict3)
d = prestamo(dict4)
e = prestamo(dict5)
                    
print(a)
print(b)
print(c)
print(d)
print(e)
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        