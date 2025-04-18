class Cita:
    def __init__(self, paciente, medico, fecha):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.estado = "Programada"

    def cancelar(self):
        self.estado = "Cancelada"

    def completar(self):
        self.estado = "Completada"

    def mostrar_info(self):
        return (f"Cita con {self.medico.get_nombre()} para el paciente {self.paciente.get_nombre()} "
                f"el {self.fecha} - Estado: {self.estado}")
