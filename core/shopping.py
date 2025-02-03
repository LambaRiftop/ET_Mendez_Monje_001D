class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, artesania):
        if artesania.codigo not in self.carrito.keys():
            self.carrito[artesania.codigo]={
                "codigo":artesania.codigo,
                "nombre":artesania.nombre,
                "precio":str(artesania.precio),
                "cantidad": 1,
                "total":artesania.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key==artesania.codigo:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = artesania.precio
                    value["total"] = value["total"] + artesania.precio

                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, artesania):
        id = artesania.codigo
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self,artesania):
        for key, value in self.carrito.items():
            if key == artesania.codigo:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = value["total"]-artesania.precio
                if value["cantidad"] < 1:
                    self.eliminar(artesania)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True
