# Sistema de Gestión de Citas Médicas 

## Contexto del problema

En un centro médico , los usuarios requieren agendar citas médicas con profesionales de distintas especialidades, garantizando que se respete la disponibilidad y evitando la doble asignación. Este sistema simula una solución informática sencilla para gestionar pacientes, médicos, especialidades, horarios y el estado de cada cita (programada, completada o cancelada).

## Objetivo del proyecto

Construir un sistema orientado a objetos que permita:

- Registrar pacientes por cédula
- Consultar médicos según especialidad
- Seleccionar una fecha y hora de atención
- Agendar la cita y modificar su estado
- Visualizar el historial de cada cita

## Conceptos de programación orientada a objetos implementados

- ✅ Clases: `Paciente`, `Medico`, `Cita`, `CentroMedico`
- ✅ Encapsulamiento: atributos privados y métodos `get_`
- ✅ Constructores: inicialización de objetos con sus datos clave
- ✅ Métodos personalizados: `mostrar_info()`, `completar()`, `cancelar()`, etc.
- ✅ Instanciación de objetos a partir de selección en consola
- ✅ Uso de listas y estructuras anidadas para simular disponibilidad

## Archivos principales

- `main_especialidad_por_numero.py`: programa principal ejecutable
- `model/`: contiene todas las clases organizadas en módulos:
  - `paciente.py`
  - `medico.py`
  - `cita.py`
  - `centro_medico.py`

## Cómo ejecutar

1. Asegúrese de tener Python 3 instalado.
2. Ejecute el archivo principal desde consola:

```bash
python main_especialidad_por_numero.py
```

## Autor

Este proyecto fue desarrollado como entrega final del módulo de Programación I. Fue diseñado aplicando conceptos de POO en un contexto realista basado en la operación de un Centro Medico.


