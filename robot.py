class Robot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.monedas = 0
        self.direccion = "UP"
        self.mapa = None

    def mover(self):
        if self.direccion == "UP":
            self.y -= 1
        elif self.direccion == "RIGHT":
            self.x += 1
        elif self.direccion == "DOWN":
            self.y += 1
        else:
            self.x -= 1

        # Limitar al robot para que no se salga
        if self.x < 0:
            self.x = 0

        if self.x >= self.mapa.ancho:
            self.x = self.mapa.ancho - 1

        if self.y < 0:
            self.y = 0

        if self.y >= self.mapa.altura:
            self.y = self.mapa.altura - 1

    def rotar(self):
        if self.direccion == "UP":
            self.direccion = "RIGHT"
        elif self.direccion == "RIGHT":
            self.direccion = "DOWN"
        elif self.direccion == "DOWN":
            self.direccion = "LEFT"
        else:
            self.direccion = "UP"

    def dibujar(self):
        if self.direccion == "UP":
            return "A"
        elif self.direccion == "RIGHT":
            return ">"
        elif self.direccion == "DOWN":
            return "V"
        else:
            return "<"

    def asingar_mapa(self, mapa):
        self.mapa = mapa

    def recoger(self):
        if self.mapa.contar_monedas_en(self.x, self.y) > 0:
            self.monedas += 1
            self.mapa.remover_moneda_en(x, y)
