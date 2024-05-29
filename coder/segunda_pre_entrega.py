from paquetes.clase_clientes import Clients
from paquetes.seleccion_de_clientes import select_client

client_list = [
    Clients("tomas", "tomasotero@gmail.com", "Av siempreviva 742"),
    Clients("mariano", "marian@coder.com", "paso y rocha al 115"),
    Clients("toni el gordo", "mafia@hotmial.com", "callefalsa 123")
]


client_select = select_client(client_list)

while True:
    print("----MENU----")
    print("Elija una opcion")
    print("1- Agregar producto al carrito")
    print("2- Eliminar un producto del carrito")
    print("3- Mostrar carrito")
    print("4- cambiar de cliente")
    print("5- Salir")

    option = input("ingrese una opcion: ")

    if option == "1":
        product = input("ingrese el producto para agregar al carrito: ").strip().capitalize()
        if product == "":
            print("Debe ingrasar un producto!")
        else:
            client_select.add_to_cart(product)
    elif option == "2":
        product = input("ingrese el producto para eliminar del carrito: ").strip().capitalize()
        if product == "":
            print("No ingreso ningun producto para eliminar")
        else:
            client_select.delete_from_cart(product)
    elif option == "3":
        client_select.show_cart()
    elif option == "4":
       client_select = select_client(client_list)
    elif option == "5":
        print("adiooos, gracias por comprar!")
        break
    else:
        print("Esa opcion no es correcta")



