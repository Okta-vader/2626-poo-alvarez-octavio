# Explicación detallada de `TAREA_S_2.py`

Este documento explica, paso a paso y en un lenguaje para principiantes, cada parte del archivo `TAREA_S_2.py`. El objetivo es ayudarte a comprender los conceptos básicos de la Programación Orientada a Objetos (POO) usando este ejemplo simple: una clase `Student` que modela a un estudiante.

---

Checklist de lo que contiene este archivo:
- Descripción general del propósito del script
- Explicación de las importaciones y anotaciones de tipos
- Desglose de la clase `Student`: atributos, constructor (`__init__`), métodos y convenciones
- Explicación del uso de `@classmethod` y `__str__`
- Explicación de la función `_demo` y del bloque `if __name__ == "__main__"` para ejecutar como script
- Ejemplos prácticos y ejercicios sugeridos

---

1) Encabezado y docstring

En las primeras líneas del archivo Python hay una cadena de documentación (docstring) que describe brevemente el propósito del archivo. Una docstring al inicio de un módulo sirve para explicar qué hace y es útil cuando alguien más (o tú en el futuro) lee el código.

2) Importaciones

```python
from typing import Dict, Any
```

Esta línea importa tipos que ayudan a documentar y comprobar el código: `Dict` y `Any`. No son obligatorios para que el programa funcione, pero ayudan a entender qué tipos de datos espera cada función o método (anotaciones de tipo).

3) Definición de la clase `Student`

```python
class Student:
    """Representa a un estudiante.

    Atributos:
        nombre (str): Nombre completo del estudiante.
        edad (int): Edad en años.
        matricula (str): Número de matrícula o identificación.
        carrera (str): Carrera o especialidad.
        promedio (float): Promedio académico.
    """
```

Una clase es una plantilla para crear objetos (instancias). Aquí `Student` es el tipo de dato que agrupa la información y comportamientos relacionados con un estudiante.

4) El método constructor: `__init__`

```python
def __init__(self, nombre: str, edad: int, matricula: str, carrera: str, promedio: float):
    # Validaciones simples
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if promedio < 0:
        raise ValueError("El promedio no puede ser negativo")

    self.nombre = nombre
    self.edad = edad
    self.matricula = matricula
    self.carrera = carrera
    self.promedio = float(promedio)
```

`__init__` se ejecuta cuando creas un nuevo `Student(...)`. El parámetro `self` es la referencia a la propia instancia que se está creando. Dentro del constructor se guardan los valores en atributos de la instancia (`self.nombre`, `self.edad`, ...). También hay validaciones simples para evitar valores negativos.

Conceptos clave:
- `self` es obligatorio como primer parámetro en los métodos de instancia.
- Las validaciones evitan crear objetos en un estado inválido (por ejemplo, edad negativa).

5) Método `mostrar_informacion`

```python
def mostrar_informacion(self) -> None:
    """Imprime la información del estudiante de forma legible."""
    print(f"Nombre    : {self.nombre}")
    print(f"Edad      : {self.edad}")
    print(f"Matrícula : {self.matricula}")
    print(f"Carrera   : {self.carrera}")
    print(f"Promedio  : {self.promedio}")
```

Este es un método de instancia que muestra en pantalla los atributos del estudiante. Los métodos de instancia actúan sobre datos de una instancia específica.

6) Método `actualizar_promedio`

```python
def actualizar_promedio(self, nuevo_promedio: float) -> None:
    """Actualiza el promedio del estudiante con validación simple."""
    if nuevo_promedio < 0:
        raise ValueError("El promedio no puede ser negativo")
    self.promedio = float(nuevo_promedio)
```

Permite cambiar el promedio de la instancia. Nótese que también valida que el nuevo promedio no sea negativo.

7) Método `es_aprobado`

```python
def es_aprobado(self, passing_mark: float = 60.0) -> bool:
    """Retorna True si el estudiante alcanza la nota de aprobación."""
    return self.promedio >= passing_mark
```

Devuelve `True` si el promedio es mayor o igual que la nota mínima de aprobación. `passing_mark` tiene un valor por defecto (60.0), pero se puede cambiar si tu escala es diferente (por ejemplo 11.0 en escala 0-20).

8) Serialización: `to_dict` y constructor alterno `from_dict`

```text
def to_dict(self) -> Dict[str, Any]:
    return {
        "nombre": self.nombre,
        "edad": self.edad,
        "matricula": self.matricula,
        "carrera": self.carrera,
        "promedio": self.promedio,
    }

@classmethod
def from_dict(cls, data: Dict[str, Any]) -> "Student":
    return cls(
        nombre=data.get("nombre", ""),
        edad=int(data.get("edad", 0)),
        matricula=data.get("matricula", ""),
        carrera=data.get("carrera", ""),
        promedio=float(data.get("promedio", 0.0)),
    )
```

`to_dict` convierte el objeto a un diccionario, lo cual es útil para guardar datos o preparar una estructura JSON. `from_dict` es un método de clase que crea una nueva instancia usando datos de un diccionario. `cls` es una referencia a la clase (como `Student`) y permite crear la instancia con `cls(...)`.

9) Representación en texto: `__str__`

```python
def __str__(self) -> str:
    return f"{self.nombre} ({self.matricula}) - {self.carrera} - Prom: {self.promedio}"
```

`__str__` define la representación legible del objeto cuando se usa `print(obj)` o `str(obj)`. Es útil para depurar o mostrar resúmenes.

10) Bloque de demostración: `_demo` y `if __name__ == "__main__"`

La función `_demo` crea dos estudiantes, muestra información, verifica si aprobaron y actualiza el promedio de uno.

```text
def _demo():
    s1 = Student("Ana Pérez", 20, "2026-001", "Ingeniería", 78.5)
    s2 = Student("Luis Gómez", 22, "2026-002", "Derecho", 58.0)
    ...

if __name__ == "__main__":
    _demo()
```

El bloque `if __name__ == "__main__"` asegura que la demostración solo se ejecute cuando el archivo se ejecute directamente (`python TAREA_S_2.py`) y no cuando se importe desde otro módulo.

11) Cómo ejecutar el script

Desde PowerShell (en Windows), sitúate en la carpeta `PARCIAL_1/SEMANA_2` y ejecuta:

```powershell
python .\TAREA_S_2.py
```

o con la ruta completa:

```powershell
python "D:\PERSONAL_OA\UNIVERSIDAD\2do SEMESTRE\PROGRAMACION ORIENTADA A OBJETOS\PYTHON\2626-poo-alvarez-octavio\PARCIAL_1\SEMANA_2\TAREA_S_2.py"
```

12) Conceptos de POO aprendidos con este ejemplo
- Clase y objeto (instancia)
- Atributos de instancia
- Métodos de instancia
- Constructor (`__init__`)
- Métodos especiales (`__str__`)
- Métodos de clase (`@classmethod`) para constructores alternos
- Encapsulación básica y validaciones

13) Ejercicios recomendados para practicar
- Añade un atributo `estado` que indique si el estudiante está "activo" o "inactivo" y un método para cambiar ese estado.
- Implementa comparación entre estudiantes por promedio (`__lt__` para usar `<`).
- Guarda una lista de estudiantes en un archivo JSON usando `to_dict` y prueba `from_dict` para cargar.

14) Preguntas frecuentes (FAQ)
- ¿Por qué usamos `float(promedio)`? → Para asegurar que el atributo `promedio` sea un número con punto decimal, incluso si se pasa un entero.
- ¿Por qué validar en `__init__`? → Para evitar que se creen objetos en un estado inválido; así el resto del código puede confiar en que los atributos cumplen ciertas reglas.

---

Si quieres, puedo:
- Añadir más ejemplos comentados dentro del mismo archivo Python.
- Crear pequeños tests o un script adicional que cree varios estudiantes y los guarde en JSON.

Dime qué prefieres y lo agrego.


