# 🚗 Sistema de Gestión de Garaje 🚘

Aplicación de escritorio desarrollada con **Python y Tkinter** que permite registrar y gestionar vehículos dentro de un garaje.

El sistema aplica **Programación Orientada a Objetos (POO)** y una **arquitectura modular por capas**, separando los modelos de datos, la lógica del sistema, la interfaz gráfica y el archivo principal.

---

# 🎯 Objetivo del Proyecto

Desarrollar una aplicación de escritorio GUI que permita:

- Registrar y agregar vehículos dentro de un garaje
- Visualizar los vehículos registrados en una tabla
- Eliminar vehículos cuando sea necesario
- Limpiar campos del formulario de registro
- Aplicar buenas prácticas de POO para un código comprensible y organizado
- Aplicar correctamente la arquitectura modular
- Usar adecuadamente los componentes de Tkinter

---

## 🗂️ Estructura del proyecto

```
2526-POO-B-S13--Sigcha-Joselyn/garaje_app/
│
├── modelos/
│   ├── __init__.py
│   └── vehiculo.py            # Capa de datos: entidad del sistema
├── servicios/
│   ├── __init__.py
│   └── garaje_servicio.py     # Capa de lógica
└── ui/
│   ├── __init__.py
│   └── app_tkinter.py         # Interfaz gráfica
│
├── main.py                    # Punto de entrada
└── README.md                  # Documentación del proyecto

```
### 📦 Modelos

Contienen las entidades del sistema.

- `Vehiculo`
- Define los atributos del vehículo
- Implementa **encapsulación con atributos privados**

### ⚙️ Servicios

Contienen la **lógica del sistema**.

- Registro de vehículos
- Validación de datos
- Eliminación de vehículos
- Gestión de la colección (diccionario) de vehículos

### 🖥️ Interfaz Gráfica

Implementada con **Tkinter**.

Permite al usuario:

- Ingresar información del vehículo
- Registrar o agregar vehículos
- Visualizar la lista en una tabla
- Eliminar registros
- Limpiar el formulario

---

## ⚙️ Funcionalidades del sistema

- ✅ Registrar vehículos con placa, marca y propietario
- ✅ Validación de campos vacíos y placas duplicadas
- ✅ Visualización de los vehículos en una tabla
- ✅ Eliminar vehículo seleccionado
- ✅ Limpiar los campos del formulario

---

## 🧠 Buenas prácticas aplicadas

- **Encapsulación**: uso de atributos privados con (`__atributo`) 
- **Properties**: getters y setters usando `@property` y `@setter`
- **Separación de responsabilidades**: modelo / servicio / UI completamente desacoplados
- **Validaciones**: en setters del modelo y en la capa de servicio
- **Docstrings**: en todas las clases y métodos
- **Type hints**: anotaciones de tipos en todos los métodos para mejorar la legibilidad del código

---

## 📋 Requisitos

- Python 3.10 o superior
- Tkinter (incluido con Python por defecto)

## 🚀 Cómo Ejecutar el Programa

1. **Obtener el enlace del repositorio.**
2. **Abrir un IDE:** PyCharm o Visual Studio Code.
3. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   ```
4. **Ejecutar:**
   ```bash
   python main.py
   ```
5. Se abrirá la interfaz gráfica del sistema de gestión de garaje.

---

## 🏁 Conclusión

Este proyecto permitió aplicar los conceptos fundamentales de Programación Orientada a Objetos en Python, junto con el desarrollo de interfaces gráficas utilizando Tkinter.

La arquitectura modular facilitó la organización del código, permitiendo separar claramente:

 - la representación de los datos

 - la lógica del sistema

 - y la interacción con el usuario

Esto hace que el sistema sea más mantenible, escalable y fácil de comprender.