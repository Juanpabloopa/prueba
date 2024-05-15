'''administracion de stock'''


import os 
sotock={'1':['escoba:5'],
       '2':['huevos:25'],
        '3':['leche:9'],
        '4':['hainas:0']}
menup =['ver sttock de producto','añadir nuevo producto','adjuntar stock','eliminar productos','salir']

while True:
    for ind,opt in enumerate(menup):
        print(f'{ind+1}{opt}')  
        ans= input ('¿Que quieres hacer?')
        if ans == '1':
            os.system
            for ind , opt in sotock.items():
                print(f'{ind+1}\n{opt}')
        elif  ans == '2':
            os.system
            while True:


                for llave,valor in sotock.items:
                    print('')
                    stock= max()+1
                    merca=input ('que deseas agregar')
                    if not merca.isspace('',' '):
                        print('error. solo debe ser con caracteres alfabeticos')
                        continue
                    canti=input('ingrese la cantidad que vas a ingresar')
                    if not canti.isspace('',' '):
                        continue

        elif ans == '3':
            pass
        elif ans == '4':
            os.system
        elif ans == '5':
            os.system
            exit('adios')
        else: 
            os .system
            print('la opcion ingresada no es valida')
            
