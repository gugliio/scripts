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


menu = """

Bienvenido al conversor de monedas 

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opcion. """

opcion = input(menu)
if opcion == '1':
    pesos = input('Cuantos pesos colombianos quiere cambiar? ')
    pesos = float(pesos)
    valor_dolar  = 3875
    dolares = pesos / float(valor_dolar)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Usted tiene ' + dolares + ' dolares')
    pass
elif opcion == '2':
    pesos = input('Cuantos pesos argentinos quiere cambiar? ')
    pesos = float(pesos)
    valor_dolar  = 65
    dolares = pesos / float(valor_dolar)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Usted tiene ' + dolares + ' dolares')
elif opcion == '3':
    pesos = input('Cuantos pesos mexicanos quiere cambiar? ')
    pesos = float(pesos)
    valor_dolar  = 24
    dolares = pesos / float(valor_dolar)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Usted tiene ' + dolares + ' dolares')
else:
    print('Ingresa una opcion valida')

