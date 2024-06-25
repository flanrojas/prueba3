import os
os.system ("cls")


nombre =""
tipo_auto=""


def nuevo_registro ():
    
    while True:
        try:
            nombre=input("ingrese su nombre")
        except:
            nombre =""
            print("nombre invalido")
        if nombre != "":
            print("nombre valido")
            break
        else:
            print("nombre invalido")
    while True:
        try:
            marca=input("ingrese marca de auto entre min 5  , max 15 caracteres")
        except:
            marca=""
            print("ingrese algo valido")
        if marca !="":
            print("marca valida")
            break
        else:
            print("marca invalida")
    while True:
        print("ingrese tipo de automovil")
        print("1-moto")
        print("2-camion")
        print("3-camioneta")
        print("4-auto")
        
        
        try:
            tipo_auto=int(input("ingrese tipo de auto:"))
        except:
            tipo_auto = 0
            print("invalido")
            
            if tipo_auto == 1:
                print("moto")
            elif tipo_auto == 2:
                print("camion")
            elif tipo_auto == 3:
                print("camioneta")
            elif tipo_auto == 4:
                print("auto")
                break
            else:
                print("invalido")
    while True:
        try:
            fecha_registro=(input("ingrese fecha de registro"))
            
        except:
            fecha_registro=""
        if fecha_registro != "":
            print("valido")
            break
        else:
            print("invalido")
    while True:
        try:
            run=input("ingrese run:")
        except:
            run=""
            print("invalido")
        if run != "":
            print("valido")
            break
        else:
            print("invalido")#>may
    while True:
        try:
            patente=input("ingrese patente valida(excepto Ñ, M,N)min 4 dig ")
        except:
            patente=""
        if patente !="":
            print("valido")
            break
        else:
            print("invalido")
    while True:
        try:
            precio=input("ingrese  precio  (mayor a cinco millones):")
        except :
            precio=""
        if precio !="":
            print("valido")
            break
        else:
            print("invalido")
    while True:
        try:
            multa=int(input("ingrese multa"))
        except:
            multa=-1
            print("invalido")
        if multa >-1:
            print("valido")
            break
        else:
            print("ingrese algo")


    diccionario_registro={
        "nombre":nombre,
        "marca":marca,
        "tipoauto":tipo_auto,
        "fecharegistro":fecha_registro,
        "run":run,
        "precio":precio,
        "patenteauto":patente,
        "contaminacion":1500,
        "anotacion":1500,
        "multas":multa,
        }
    return diccionario_registro 
def busqueda_patente(patente,lista_patente):
    resultados=[]
    for patente in lista_patente:
        if patente["panteteauto"]==patente:
            resultados.append(patente)
    if resultados :
        print(f"informacion de automovil para:{diccionario_registro['nombre']},marca:{diccionario_registro['marca']},tipo:{diccionario_registro['tipo_auto]},{diccionario_registro['fecha_registro']},{diccionario_registro['run']},{diccionario_registro[precio]},{diccionario_registro[patente]},")



def imprimir_hoja(certificado)   

    
        
        
    




                
            




        


    


        





        


    
    
