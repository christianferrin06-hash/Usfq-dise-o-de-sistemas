from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class EstrategiaPrioridad(ABC):
    @abstractmethod
    def tiene_prioridad(self, fecha_hora: datetime) -> bool:
        pass

class SinPrioridadStrategy(EstrategiaPrioridad):
    def tiene_prioridad(self, fecha_hora: datetime) -> bool:
        return False

class PrioridadOficialStrategy(EstrategiaPrioridad):
    def tiene_prioridad(self, fecha_hora: datetime) -> bool:
        return fecha_hora.hour < 18

class Usuario:
    def __init__(self, id_usuario: str, nombre: str, estrategia_prioridad: EstrategiaPrioridad):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.estrategia_prioridad = estrategia_prioridad

    def evaluar_prioridad(self, fecha_hora: datetime) -> bool:
        return self.estrategia_prioridad.tiene_prioridad(fecha_hora)

class Estudiante(Usuario):
    def __init__(self, id_usuario: str, nombre: str):
        super().__init__(id_usuario, nombre, SinPrioridadStrategy())

class Capitan(Usuario):
    def __init__(self, id_usuario: str, nombre: str):
        super().__init__(id_usuario, nombre, PrioridadOficialStrategy())

class Cancha:
    def __init__(self, id_cancha: str, nombre: str):
        self.id_cancha = id_cancha
        self.nombre = nombre
        self.disponible = True

class Reserva:
    def __init__(self, id_reserva: str, usuario: Usuario, cancha: Cancha, fecha_hora_inicio: datetime):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.cancha = cancha
        self.fecha_hora_inicio = fecha_hora_inicio
        self.estado = "CONFIRMADA"

    def cancelar(self, fecha_hora_actual: datetime):
        diferencia = self.fecha_hora_inicio - fecha_hora_actual
        if diferencia < timedelta(hours=2):
            self.estado = "NO_SHOW"
        else:
            self.estado = "CANCELADA"