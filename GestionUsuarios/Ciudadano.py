from GestionEventos.Evento import Evento
from GestionEventos.Solicitud import Solicitud


class Ciudadano():
    def __init__(self,CUIL,telefono,solicitudesRechazadas,estaBloqueado):
        self.CUIL = CUIL
        self.telefono = telefono
        self.solicitudesRechazadas = solicitudesRechazadas
        self.estaBloqueado = estaBloqueado
    def booleanNumericoEstaBloqueado(self):
        if self.estaBloqueado == True:
            return 1
        else:
            return 0
    def crearEvento(self,nombre,ano,mes,dia,hora,minuto,tipo_de_evento,cantidad_maxima_de_personas,vectorX,vectorY):
        newEvento = Evento(nombre,ano,mes,dia,hora,minuto,tipo_de_evento,cantidad_maxima_de_personas,vectorX,vectorY)
        return newEvento
    def getCUIL(self):
        return self.CUIL
    def ciudadanoAEscribir(self):
        return [str(self.CUIL) , str(self.telefono), str(self.solicitudesRechazadas) , str(self.booleanNumericoEstaBloqueado())]
    def aceptarSolicitud(self):
        pass
    def rechazarSolicitud(self):
        pass
    def enviarSolicitud(self, Ciudadano, CUILAEnviar, evento):
        if evento.estaLleno == True:
            print("el evento no tiene mas capacidad disponible")
        else:
            CuilSender = Ciudadano.CUIL
            EventName = evento.nombre
            newSolicitud = Solicitud(CuilSender, CUILAEnviar, EventName)
            return newSolicitud