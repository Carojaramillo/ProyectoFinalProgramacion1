# 📅 Sistema de Gestión de Citas Médicas 

## 🩺Contexto del Problema

El centro médico para el cual fuimos contratados como Ingenieros en Analítica de Datos enfrenta desafíos significativos en la gestión eficiente de sus citas médicas. La programación manual de citas ha generado demoras, errores administrativos y una experiencia insatisfactoria para los pacientes. Ante esta situación, se nos encomendó desarrollar una solución tecnológica para que los Ejecutivos de Atención del Centro Médico puedan gestionar de manera más eficiente para gestionar pacientes, médicos, especialidades, horarios y el estado de cada cita (programada, completada o cancelada).

## 🎯Objetivo del Proyecto

Construir un sistema orientado a objetos que permita:

- Registrar pacientes por cédula.
- Consultar médicos según especialidad.
- Seleccionar una fecha y hora de atención.
- Agendar la cita y modificar su estado.
- Visualizar el historial de cada cita.

## 🧠 Implementación de los Conceptos de Programación Orientada a Objetos (POO)
Este proyecto fue desarrollado como evidencia final del módulo de Programación I, aplicando los principales fundamentos de la programación orientada a objetos en un contexto realista (gestión de citas médicas).

Los conceptos implementados fueron:

- Clases: Se crearon clases como Paciente, Medico, Cita y CentroMedico, cada una con atributos y métodos propios que representan entidades reales del sistema.
- Encapsulamiento: Se protegieron los atributos sensibles mediante atributos privados (__nombre, __documento) y se accede a ellos mediante métodos públicos (getters).
- Constructores: Se usaron métodos init para inicializar los objetos con sus propiedades desde el momento en que se crean.
- Instanciación de objetos: Se crean instancias de pacientes, médicos y citas durante la ejecución del programa en base a las elecciones del usuario.
- Métodos personalizados: Se implementaron funciones como mostrar_info(), cancelar(), completar(), que encapsulan comportamientos propios de cada objeto.
- Modularidad: Se dividió el código en varios archivos organizados en carpetas (modelo), lo cual facilita el mantenimiento, la escalabilidad y la reutilización del sistema.
- Uso de listas y estructuras anidadas para simular disponibilidad.

## 📁 Archivos Principales

- `main_especialidad_por_numero.py`: programa principal ejecutable
- `model/`: contiene todas las clases organizadas en módulos:
`paciente.py`
`medico.py`
`cita.py`
`centro_medico.py`

## 🖥️ ¿Cómo ejecutar?

1. Asegúrese de tener Python 3 instalado.
2. Ejecute el archivo principal desde consola: main.py

## 🧭 Flujo de Uso del Sistema

1. Ingrese el número de cédula del paciente: El sistema validará si está registrado en la base de datos simulada. Si su número de cédula no registra en la base de datos, el sistema indicará - "Paciente no resistrado".

2. Seleccione la Especialidad del Médico: Se relacionará una lista numerada con las especialidades disponibles (1.Medicina General, 2.Pediatría, 3. Dermatología, 4. Neurocirugía).

3. Selecciona el Médico: Se listarán los médicos para esa especialidad junto con sus horarios disponibles.

4. Selecciona la fecha y hora de la cita.: Se mostrarán los horarios disponibles.

5. La cita quedará asignada y el sistema indicará - Estado:“Programada”. ✅ "Cita agendada existosamente"
   
6. Una vez programada la cita, usted tendra las siguientes opciones: 1. Completar cita (asistió a la consulta y recibió la atención médica), 2. Cancelar Cita (Anular o liberar la cita programada previamente), 3. Ver estado actual (Indica si la cita está Programada, Completada o Cancelada", 4. Salir (Cerrar la sesión actual del usuario). 

## 👥 Autores

Este proyecto fue desarrollado como entrega final del módulo de Programación I por los estudiantes de Ingeniería en Analítica de Datos:​ Tito Gómez y Andrea Jaramillo. 






