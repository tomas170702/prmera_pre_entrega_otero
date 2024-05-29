class Clients():

    def __init__(self, name, email, adress):
        self.name = name
        self.email = email
        self.adress = adress
        self.cart = [ ]

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{self.name} ha agregado un {product} a su carrito")


    def delete_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"ha eliminado {product} de su carrito")
        else:
            print(f"no hay ningun/a {product} en este carrito")


    def show_cart(self):
        if self.cart:
            print(f"este es el carrito de {self.name}")     
            for product in self.cart:
                print(product)
        else:
            print(f"no hay productos en el carrito de {self.name}")


    def __srt__(self):
        return f"{self.name}"
    



            


        
    

