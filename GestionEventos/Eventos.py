class Eventos():
    def __init__(self,fecha,tipo_de_eventos,cantidad_de_personas,cantidad_maxima_de_personas,localidad):
        self.fecha = fecha
        self.tipo_de_eventos = tipo_de_eventos
        self.cantidad_de_personas = cantidad_de_personas
        self.cantidad_maxima_de_personas = cantidad_maxima_de_personas
        self.localidad = localidad

    def crearEventos(self):
        pass

    def contabilizadorPersonas(self):
        return (self.cantidad_maxima_de_personas - self.cantidad_de_personas)