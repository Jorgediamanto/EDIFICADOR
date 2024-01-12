from ejercicio1 import *
import csv
import os.path





def main():

    iniciar_sesion_o_registrar() 
    
    factory = PizzaFactory()
    director = PizzaDirector(factory)

    # Crea la primera pizza utilizando la fábrica abstracta
    director.crear_pizza()
    pizza1 = director.builder.pizza

    # Crea la segunda pizza utilizando la fábrica abstracta
    director = PizzaDirector(PizzaFactory())
    director.crear_pizza()
    pizza2 = director.builder.pizza

    print("¡Tu primera pizza está lista!")
    print("Detalles de la pizza:")
    print("Tamano:", pizza1[0])
    print("Masa:", pizza1[1])
    print("Ingredientes:", pizza1[2])
    print("Salsa:", pizza1[3])
    print("Tecnica de coccion:", pizza1[4])
    print("Presentacion:", pizza1[5])
    
    print("\n¡Tu segunda pizza está lista!")
    print("Detalles de la pizza:")
    print("Tamano:", pizza2[0])
    print("Masa:", pizza2[1])
    print("Ingredientes:", pizza2[2])
    print("Salsa:", pizza2[3])
    print("Tecnica de coccion:", pizza2[4])
    print("Presentacion:", pizza2[5])

    # Asegúrate de que pedido_builder está definido antes de usarlo
    pedido_builder = PedidoPizzaCSVBuilder()

    if not os.path.isfile('pedidos_pizza.csv'):
        pedido_builder.crear_csv()
    
    # Añade la primera pizza al pedido (ajusta según tus necesidades)
    pedido_builder.añadir_pedido("cliente1", pizza1)
    
    try:
        bebidas = {
            "Aguita refrescante": "Aguita refrescante",
            "Flameado de Moe": "Flameado de Moe",
            "Cerveza": "Cerveza",
            "Nada": "Nada"
        }
        
        print("Elige tu bebida:")
        seleccion_bebida = obtener_seleccion(bebidas)
        
        postres = {
            "Banana split": "Banana split",
            "Dorayaki": "Dorayaki",
            "Batipasas": "Batipasas",
            "Nada": "Nada"
        }
        
        print("Elige tu postre:")
        seleccion_postre = obtener_seleccion(postres)
        
        entrantes = {
            "Nachos guerrero": "Nachos guerrero",
            "Enchilada": "Enchilada",
            "Taco": "Taco",
            "Nada": "Nada"
        }
        
        print("Elige tu entrante:")
        seleccion_entrante = obtener_seleccion(entrantes)
        
        nueva_fila = ['elemento1', 'elemento2', 'elemento3', 'elemento4']

        nombre_archivo = 'complementos.csv'
        with open(nombre_archivo, mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(nueva_fila)

    except ValueError as e:
        print("Error: Ingresa un número válido.")
    
    lista_selecciones = [seleccion_bebida, seleccion_postre, seleccion_entrante]
    cantidad_nada = lista_selecciones.count('Nada')
    preciocomplementos= (3-cantidad_nada)*4
    print("El precio de los complementos es: ", preciocomplementos, "€")
    print("El precio de la pizza es de: ", 8, "€")
    preciototal=preciocomplementos+8
    if preciototal == 20:
        print("Al haber pedido entrante, pizza, bebida y postre formando un menú individual de tarifa reducida, el nuevo precio es de 15 euros")
        preciototal=15
    print("El precio total es de: ", preciototal, "€")




if __name__ == "__main__":
    main()