class CentroMedico:
    def __init__(self):
        self.citas = []

    def agendar_cita(self, cita):
        self.citas.append(cita)

    def listar_citas(self):
        for cita in self.citas:
            print(cita.mostrar_info())
