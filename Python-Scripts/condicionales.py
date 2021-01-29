# edad = int(input('Escribe tu edad: '))
# if edad > 17:
#     print('Es mayor de edad')    
# else:
#     print('Es menor de edad')    


# numero  = int(input('Escribe un numero: '))
# if numero > 5:
#     print('Es mayor a cinco')
# elif numero == 5:
#     print('Es igual a cinco')
# else: 
#     print('Es menor a cinco')

def conversor(tipo_pesos, valor_dolar):
    pesos = input('Cuantos pesos ' + tipo_pesos +  ' quiere cambiar? ')
    pesos = float(pesos)
    dolares = pesos / float(valor_dolar)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Usted tiene ' + dolares + ' dolares')

menu = """

Bienvenido al conversor de monedas 

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opcion. """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3875)
elif opcion == '2':
        conversor('argentinos', 65)    
elif opcion == '3':
    conversor('mexicanos', 24)    
else:
    print('Ingresa una opcion valida')

