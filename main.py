from model.paciente import Paciente 
from model.medico import Medico
from model.cita import Cita
from model.centro_medico import CentroMedico

# Simulación de base de datos de pacientes
PACIENTES_REGISTRADOS = {
    "1001234567": "Laura Restrepo",
    "1009876543": "Carlos Mendoza",
    "16933419": "Tito Gomez",
    "1130673463": "Andrea Jaramillo"
}

# Simulación de médicos por especialidad y su disponibilidad
MEDICOS_ESPECIALIDAD = {
    "Medicina General": {
        "Adriana Torres": ["2025-05-01 08:00", "2025-05-01 09:00"],
        "Carlos Ruiz": ["2025-05-01 10:00"]
    },
    "Pediatría": {
        "Sonia Morales": ["2025-05-01 08:30"]
    },
    "Dermatología": {
        "Fernando Gómez": ["2025-05-01 11:00", "2025-05-01 12:00"],
        "Diana Quintero": ["2025-05-01 09:30"]
    },
    "Neurocirugía": {
        "Natalia Castellanos": ["2025-05-05 11:00", "2025-05-05 12:00"],
        "Viviana Cardona": ["2025-05-01 09:30"]
    }
}

def seleccionar_paciente():
    cedula = input("Ingrese la cédula del paciente: ")
    if cedula in PACIENTES_REGISTRADOS:
        nombre = PACIENTES_REGISTRADOS[cedula]
        print(f"Paciente encontrado: {nombre}")
        return Paciente(nombre, cedula)
    else:
        print("Paciente no registrado.")
        return None

def seleccionar_medico_y_fecha():
    print("\\nEspecialidades disponibles:")
    especialidades = list(MEDICOS_ESPECIALIDAD.keys())
    for idx, esp in enumerate(especialidades, start=1):
        print(f"{idx}. {esp}")

    try:
        seleccion_esp = int(input("Seleccione una especialidad (número): "))
        if seleccion_esp < 1 or seleccion_esp > len(especialidades):
            print("Número fuera de rango.")
            return None, None, None
    except ValueError:
        print("Entrada inválida.")
        return None, None, None

    esp = especialidades[seleccion_esp - 1]
    medicos = MEDICOS_ESPECIALIDAD[esp]
    print(f"\\nMédicos disponibles en {esp}:")

    for i, (nombre, horarios) in enumerate(medicos.items(), start=1):
        print(f"{i}. {nombre} - Horarios disponibles: {', '.join(horarios)}")

    try:
        seleccion = int(input("Seleccione un médico (número): "))
        medico_nombre = list(medicos.keys())[seleccion - 1]
        fechas = medicos[medico_nombre]
    except (IndexError, ValueError):
        print("Selección inválida.")
        return None, None, None

    print(f"Fechas disponibles para {medico_nombre}:")
    for j, fecha in enumerate(fechas, start=1):
        print(f"{j}. {fecha}")
    try:
        seleccion_fecha = int(input("Seleccione una fecha (número): "))
        fecha_final = fechas[seleccion_fecha - 1]
    except (IndexError, ValueError):
        print("Selección de fecha inválida.")
        return None, None, None

    return Medico(medico_nombre, esp), fecha_final, (esp, medico_nombre, fecha_final)

def main():
    centro = CentroMedico()
    print("=== Agendamiento de cita médica ===")

    paciente = seleccionar_paciente()
    if not paciente:
        return

    medico, fecha, datos_seleccion = seleccionar_medico_y_fecha()
    if not medico:
        return

    cita = Cita(paciente, medico, fecha)
    centro.agendar_cita(cita)

    # Eliminar fecha seleccionada para evitar doble asignación
    MEDICOS_ESPECIALIDAD[datos_seleccion[0]][datos_seleccion[1]].remove(datos_seleccion[2])

    print("\\n✅ Cita agendada exitosamente:")
    print(cita.mostrar_info())

    # Menú de gestión de cita
    while True:
        print("\\n=== Menú de gestión de cita ===")
        print("1. Completar cita")
        print("2. Cancelar cita")
        print("3. Ver estado actual")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cita.completar()
            print("✅ Cita marcada como COMPLETADA.")
        elif opcion == "2":
            cita.cancelar()
            print("❌ Cita marcada como CANCELADA.")
        elif opcion == "3":
            print("📄 Estado actual:")
            print(cita.mostrar_info())
        elif opcion == "4":
            print("👋 Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()