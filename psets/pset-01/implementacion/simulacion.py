from datetime import datetime, timedelta
from modelo import Estudiante, Capitan, Cancha, Reserva

def ejecutar_simulacion():
    print("=== INICIO DE SIMULACIÓN RESERVAU ===\n")

    estudiante = Estudiante("E01", "Mateo")
    capitan = Capitan("C01", "Carlos")
    cancha = Cancha("K1", "Cancha Sintética 1")

    hora_reserva = datetime.now() + timedelta(days=1)
    hora_reserva = hora_reserva.replace(hour=15, minute=0)

    print(f"1. {capitan.nombre} (Capitán) solicita reservar {cancha.nombre} a las {hora_reserva.strftime('%H:%M')}.")
    print("2. El sistema verifica disponibilidad.")
    
    if capitan.evaluar_prioridad(hora_reserva):
        print("3. El sistema aplica regla: Tiene prioridad oficial antes de las 6:00 p.m.")
    
    reserva_1 = Reserva("R01", capitan, cancha, hora_reserva)
    print("4. El sistema crea la reserva.")
    print(f"5. El sistema confirma la reserva {reserva_1.id_reserva} como '{reserva_1.estado}'.\n")

    hora_actual_normal = hora_reserva - timedelta(hours=5)
    print(f"1. {capitan.nombre} solicita cancelar la reserva {reserva_1.id_reserva}.")
    print("2. El sistema evalúa el tiempo restante para el inicio de la reserva.")
    reserva_1.cancelar(hora_actual_normal)
    print(f"3. Tiempo suficiente. El sistema procesa la acción.")
    print(f"4. Estado final de la reserva: '{reserva_1.estado}'.\n")

    reserva_2 = Reserva("R02", estudiante, cancha, hora_reserva)
    hora_actual_tardia = hora_reserva - timedelta(minutes=45)
    
    print(f"1. {estudiante.nombre} (Estudiante) solicita cancelar la reserva {reserva_2.id_reserva}.")
    print("2. El sistema evalúa el tiempo restante para el inicio de la reserva.")
    reserva_2.cancelar(hora_actual_tardia)
    print("3. Faltan menos de 2 horas. El sistema aplica regla de negocio automatizada.")
    print(f"4. Estado final de la reserva: '{reserva_2.estado}'.\n")

    print("=== FIN DE LA SIMULACIÓN ===")

if __name__ == "__main__":
    ejecutar_simulacion()