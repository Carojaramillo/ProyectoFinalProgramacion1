class Paciente:
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento

    def get_documento(self):
        return self.__documento

    def get_nombre(self):  # 🔧 este método faltaba
        return self.__nombre

    def mostrar_info(self):
        return f"{self.__nombre} (ID: {self.__documento})"

