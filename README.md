# 📅 Sistema de Gestión de Citas Médicas 

## 🩺Contexto del Problema

Los usuarios de un Centro Médico requieren agendar sus citas médicas con profesionales de distintas especialidades, garantizando que se respete la disponibilidad y evitando la doble asignación. Este sistema simula una solución informática sencilla para gestionar pacientes, médicos, especialidades, horarios y el estado de cada cita (programada, completada o cancelada).

## 🎯Objetivo del Proyecto

Construir un sistema orientado a objetos que permita:

- Registrar pacientes por cédula
- Consultar médicos según especialidad
- Seleccionar una fecha y hora de atención
- Agendar la cita y modificar su estado
- Visualizar el historial de cada cita

## 🧠 Implementación de los Conceptos de Programación Orientada a Objetos (POO)
Este proyecto fue desarrollado como evidencia final del módulo de Programación I, aplicando los principales fundamentos de la programación orientada a objetos en un contexto realista (gestión de citas médicas).

Los conceptos implementados fueron:

- Clases: Se crearon clases como Paciente, Medico, Cita y CentroMedico, cada una con atributos y métodos propios que representan entidades reales del sistema
- Encapsulamiento: Se protegieron los atributos sensibles mediante atributos privados (__nombre, __documento) y se accede a ellos mediante métodos públicos (getters).
- Constructores: Se usaron métodos init para inicializar los objetos con sus propiedades desde el momento en que se crean.
- Instanciación de objetos: Se crean instancias de pacientes, médicos y citas durante la ejecución del programa en base a las elecciones del usuario.
- Métodos personalizados: Se implementaron funciones como mostrar_info(), cancelar(), completar(), que encapsulan comportamientos propios de cada objeto.
- Modularidad: Se dividió el código en varios archivos organizados en carpetas (modelo), lo cual facilita el mantenimiento, la escalabilidad y la reutilización del sistema.
- Uso de listas y estructuras anidadas para simular disponibilidad.

## 📁 Archivos Principales

- `main_especialidad_por_numero.py`: programa principal ejecutable
- `model/`: contiene todas las clases organizadas en módulos:
- `paciente.py`
- `medico.py`
- `cita.py`
- `centro_medico.py`

## 🖥️ ¿Cómo Ejecutar?

1. Asegúrese de tener Python 3 instalado.
2. Ejecute el archivo principal desde consola: main.py

## 🧭 Flujo de Uso del Sistema

1. Ingresa el número de cédula del paciente.
El sistema validará si está registrado en la base de datos simulada

2. Selecciona la Especialidad del Médico.
Verás una lista numerada de especialidades disponibles (Medicina General, Pediatría, etc.).

3. Selecciona el Médico.
Aparecerán los médicos disponibles para esa especialidad junto con sus horarios disponibles

4. Selecciona la fecha y hora de la cita.
Se mostrarán horarios disponibles no asignados previamente.

5. La cita quedará registrada como “Programada” y se eliminará ese horario del sistema.
   
6. En caso de requerirlo, podrá completar la cita, cancelarla, ver el estado actual y salir del sistema.

## 👥 Autores

Este proyecto fue desarrollado como entrega final del módulo de Programación I. Fue diseñado aplicando conceptos de POO en un contexto realista basado en la operación de un Centro Médico por los Estudiantes de Ingeniería en Analítica de Datos: Tito Gómez y Andrea Jaramillo.






