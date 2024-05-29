def select_client(client_list):
    print("Clientes disponibles")
    for i, client_position in enumerate(client_list, start = 1):
        print(f" {i} - {client_position}")
    
    client_num_select = int(input("Ingrese un numero para eligir un cliente: "))
    client_select = client_list[client_num_select - 1]
    print(f"Has seleccionado a {client_select} ")
    print("Bienvenido")

    return client_select
