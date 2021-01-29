# def imprimir_mensajes():
#     print('Mensaje especial ')
#     print('Uso de funciones')
    

# imprimir_mensajes()
# imprimir_mensajes()
# imprimir_mensajes()


def conversacion(mensaje):
    print('Hola')
    print('como estas')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opcion (1,2,3): '))
if opcion == 1:
    conversacion('elegiste la opcion 1')
elif opcion == 2:
    conversacion('elegiste la opcion 2')
elif opcion == 3:
    conversacion('elegiste la opcion 3')
else: 
    print('Escribe la opcion correcta')