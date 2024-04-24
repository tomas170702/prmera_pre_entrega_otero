BD = {}



def registro():
    user = input("ingrese su nombre de usuario: ")   
    while user in BD:
        user = input("el usuario ya existe, ingrese otro nombre de usuario: ")
        break

    password = input("ingrese su contraseña: ")  
    confirm_pass = input("confirme su contraseña: ")
    while password != confirm_pass:
        print("las contraseñas no coinciden, intente de nuevo ")
        password = input("confirme su contraseña: ")
        break
    if user == "" or password == "":
        print("el usuario o la contraña no pueden estar vacios, ingreselas de vuelta")
    else:
        BD[user] = password
        print("el usuario se cargo completamente")




def leerdata():
    if len(BD) == 0:
        print("no hay usuarios registrados")
    else:
        for key, value in BD.items():
            print(f"nombre: {key} , contraseña : {value}")
            



def login():
    user = input("ingrese el nombre de usuario: ")
    password = input("ingrese la contraseña: ") 
    if user in BD and BD[user] == password:
        print("has iniciado sesion correctamente")
    else:
        print("intenta de nuevo")
                                            



while True:
    print("1, cargar usuario")
    print("2, mostrar usuario")
    print("3, login")
    print("4, exit")
    
    opciones = input("ingrese una opcion: ")

    if opciones == "1":
        registro()
    elif opciones == "2":
        leerdata()
    elif opciones == "3":
        login()
    elif opciones == "4":
        print("exit")
        break
    else:
        print("opcion incorrecta, intente de nuevo")
