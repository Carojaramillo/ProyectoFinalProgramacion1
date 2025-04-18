class Medico:
    def __init__(self, nombre, especialidad):
        self.__nombre = nombre
        self.__especialidad = especialidad

    def get_nombre(self):
        return self.__nombre

    def get_especialidad(self):
        return self.__especialidad

    def mostrar_info(self):
        return f"Dr. {self.__nombre} - {self.__especialidad}"
