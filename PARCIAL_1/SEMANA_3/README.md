# Sistema de Registro de Mascotas
## Comparación: Programación Tradicional vs Programación Orientada a Objetos

### 📚 Descripción General

Este proyecto desarrolla un **Sistema de Registro de Mascotas** utilizando dos paradigmas de programación diferentes:

1. **Programación Tradicional** - Código estructurado con funciones y variables
2. **Programación Orientada a Objetos (POO)** - Código organizado con clases y objetos

El objetivo es comparar ambos enfoques y comprender los conceptos fundamentales de la POO.

---

## 📁 Estructura del Proyecto

```
2626-poo-alvarez-octavio/PARCIAL_1/SEMANA_3/
├── README.md (este archivo)
├── programacion_tradicional/
│   └── tradicional.py
└── programacion_poo/
    ├── main.py
    └── mascota.py
```

---

## 1️⃣ Programa 1: Programación Tradicional

### Ubicación
```
programacion_tradicional/
└── tradicional.py
```

### Descripción
Solución que utiliza **variables y funciones** sin emplear clases ni objetos. Es el enfoque estructurado tradicional de la programación.

### Características Principales

#### Variables Utilizadas:
- **`mascotas`** - Lista global que almacena diccionarios de mascotas

#### Funciones Implementadas:
1. **`registrar_mascota()`** - Registra una nueva mascota solicitando datos por teclado
2. **`mostrar_todas_mascotas()`** - Muestra todas las mascotas registradas
3. **`mostrar_mascota_individual()`** - Exhibe la información de una mascota específica
4. **`buscar_mascota_por_nombre()`** - Busca una mascota por nombre
5. **`contar_mascotas_por_tipo()`** - Realiza estadísticas por tipo de mascota
6. **`calcular_edad_promedio()`** - Calcula la edad promedio de todas las mascotas
7. **`eliminar_mascota()`** - Elimina una mascota del registro
8. **`mostrar_menu()`** - Interfaz de menú principal
9. **`main()`** - Controla el flujo del programa

#### Datos Capturados de Cada Mascota:
- Nombre
- Tipo
- Edad
- Raza
- Color
- Peso

#### Ventajas:
✓ Simple y directo de entender  
✓ Bajo acoplamiento inicial  
✓ Ideal para programas pequeños  
✓ Fácil de depurar en programas simples  

#### Desventajas:
✗ Difícil de mantener en proyectos grandes  
✗ Código repetitivo  
✗ Poca reutilización de código  
✗ Gestión de datos desordenada  

### Ejecución
```bash
python .\programacion_tradicional\tradicional.py
```

---

## 2️⃣ Programa 2: Programación Orientada a Objetos

### Ubicación
```
programacion_poo/
├── main.py
└── mascota.py
```

### Descripción
Solución equivalente que implementa una **Clase Mascota** demostrando los conceptos fundamentales de la POO: clases, objetos, atributos, métodos y abstracción.

### Conceptos POO Demostrados

#### 1. **CLASE** 🏛️
```
class Mascota:
    - Plantilla o molde para crear objetos
    - Define la estructura y comportamiento común
    - Encapsula datos y funcionalidad relacionada
```

#### 2. **OBJETO** 🎯
```
mascota1 = Mascota("Max", "Perro", 5)
mascota2 = Mascota("Mittens", "Gato", 3)
mascota3 = Mascota("Tweety", "Pájaro", 2)
    
- Instancias específicas de la clase
- Cada objeto tiene sus propios valores de atributos
- Pueden ejecutar métodos independientemente
```

#### 3. **ATRIBUTOS** 📋
```
- nombre     → Almacena el nombre de la mascota
- especie    → Almacena la especie (perro, gato, etc.)
- edad       → Almacena la edad en años
    
- Son las características o propiedades de cada objeto
- Se inicializan en el método __init__()
- Se acceden mediante: objeto.atributo
```

#### 4. **MÉTODOS** 🔧
Funciones asociadas a una clase que operan en los atributos:

| Método | Descripción |
|--------|-------------|
| `__init__()` | Constructor - Inicializa los atributos del objeto |
| `mostrar_informacion()` | Muestra formateada la información del objeto |
| `hacer_sonido()` | Produce un sonido específico según la especie |
| `obtener_descripcion()` | Retorna una descripción de texto del objeto |
| `envejecer()` | Incrementa la edad del objeto |
| `cambiar_nombre()` | Modifica el nombre del objeto |

#### 5. **ABSTRACCIÓN** 🔒
```
El método hacer_sonido() es un ejemplo de abstracción:
- El usuario solo llama mascota.hacer_sonido()
- El método internamente:
  * Verifica la especie
  * Busca el sonido correspondiente
  * Muestra el resultado
- Los detalles de implementación están ocultos
```

#### 6. **ENCAPSULACIÓN** 📦
```
- Los datos (atributos) se encapsulan dentro de la clase
- Solo se accede a ellos a través de métodos
- Protege la integridad de los datos
- Facilita el mantenimiento
```

#### 7. **POLIMORFISMO** 🔄
```
- El método hacer_sonido() se comporta diferente
  según la especie de la mascota
- Cada especie produce su propio sonido
- Mismo método, diferentes comportamientos
```

### Estructura de Archivos

#### **mascota.py** - Definición de la Clase
```python
class Mascota:
    def __init__(self, nombre, especie, edad):
        # Inicializa atributos
        
    def mostrar_informacion(self):
        # Muestra información formateada
        
    def hacer_sonido(self):
        # Abstracción: decide el sonido según especie
        
    def obtener_descripcion(self):
        # Retorna descripción de texto
        
    def envejecer(self):
        # Incrementa edad
        
    def cambiar_nombre(self, nuevo_nombre):
        # Cambia nombre
```

#### **main.py** - Programa Principal
```python
from mascota import Mascota  # Importa la clase

def main():
    # Crea objetos (instancias)
    mascota1 = Mascota("Max", "Perro", 5)
    mascota2 = Mascota("Mittens", "Gato", 3)
    mascota3 = Mascota("Tweety", "Pájaro", 2)
    
    # Accede a atributos
    print(mascota1.nombre)
    
    # Ejecuta métodos
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    mascota1.envejecer()
```

### Ventajas de la POO
✓ Código más organizado y mantenible  
✓ Reutilización de código mediante herencia  
✓ Escalabilidad en proyectos grandes  
✓ Encapsulación protege los datos  
✓ Facilita el trabajo en equipo  
✓ Modelado real de problemas del mundo  
✓ Fácil de extender y modificar  

### Desventajas de la POO
✗ Requiere pensamiento más abstracto  
✗ Puede ser excesivo en programas muy simples  
✗ Curva de aprendizaje más pronunciada  

### Ejecución
```bash
cd programacion_poo
python main.py
```

---

## 📊 Comparación: Programación Tradicional vs POO

| Aspecto | Programación Tradicional | POO |
|---------|--------------------------|-----|
| **Organización** | Funciones independientes | Clases cohesivas |
| **Datos** | Variables globales/locales | Atributos en clases |
| **Reutilización** | Mediante funciones | Mediante clases/herencia |
| **Mantenibilidad** | Difícil en proyectos grandes | Fácil con buena estructura |
| **Escalabilidad** | Limitada | Excelente |
| **Complejidad** | Menor | Mayor |
| **Abstracción** | Limitada | Excelente |
| **Modelado** | Procedimental | Basado en entidades |

---

## 🎓 Conceptos Clave de POO

### Clase
- Plantilla o prototipo que define la estructura y comportamiento de los objetos
- Ejemplo: `class Mascota`

### Objeto
- Instancia específica de una clase
- Ejemplo: `mascota1 = Mascota("Max", "Perro", 5)`

### Atributo
- Variable que pertenece a una clase/objeto
- Ejemplo: `self.nombre`, `self.especie`, `self.edad`

### Método
- Función que pertenece a una clase
- Ejemplo: `def mostrar_informacion(self):`

### Constructor (__init__)
- Método especial que se ejecuta al crear un objeto
- Inicializa los atributos del objeto
- El parámetro `self` representa la instancia actual

### Instancia
- Objeto específico creado a partir de una clase
- Ejemplo: `mascota1`, `mascota2`, `mascota3`

### Encapsulación
- Agrupar datos (atributos) y operaciones (métodos) en una estructura
- Ocultar los detalles de implementación

### Abstracción
- Simplificar la complejidad ocultando detalles internos
- Ejemplo: `hacer_sonido()` no muestra cómo decide el sonido

### Polimorfismo
- Capacidad de un mismo método de comportarse diferente en diferentes contextos
- Ejemplo: `hacer_sonido()` produce diferentes sonidos

### Herencia
- No implementada en este proyecto pero fundamental en POO
- Permite que una clase herede de otra

---

## 💡 Ejemplos de Uso

### Programación Tradicional
```python
# Registrar mascota
mi_mascota = {
    "nombre": "Max",
    "especie": "Perro",
    "edad": 5
}
mascotas.append(mi_mascota)
```

### Programación POO
```python
# Crear objeto (instancia)
mi_mascota = Mascota("Max", "Perro", 5)

# Acceder a atributos
print(mi_mascota.nombre)

# Ejecutar métodos
mi_mascota.mostrar_informacion()
mi_mascota.hacer_sonido()
```

---

## 🔍 Elementos Solicitados en Ambos Programas

### ✓ Programa 1 (Tradicional)
- [x] Uso de variables y funciones
- [x] Sin usar clases ni objetos
- [x] Registro de mascotas por teclado
- [x] Mostrar información organizada
- [x] Funciones bien documentadas
- [x] Estructura mínima requerida
- [x] Comentarios relevantes

### ✓ Programa 2 (POO)
- [x] Clase Mascota implementada
- [x] Atributos: nombre, especie, edad
- [x] Métodos: mostrar_informacion(), hacer_sonido()
- [x] Mínimo 2 objetos creados (3 en realidad)
- [x] Ejecución de métodos
- [x] Demostración de: clase, objeto, atributos, métodos, abstracción
- [x] Separación en main.py y mascota.py
- [x] Estructura mínima requerida
- [x] Comentarios relevantes

---

## 📝 Comentarios en el Código

Ambos programas incluyen:
- Comentarios en el encabezado explicando el propósito
- Docstrings en funciones y clases
- Comentarios en líneas complejas
- Explicación de conceptos POO en main.py

---

## ✨ Resumen Final

Este proyecto cumple con los objetivos de:

1. **Programa 1 (Tradicional)**: Demostrar programación estructurada
2. **Programa 2 (POO)**: Demostrar programación orientada a objetos
3. **Comparación**: Entender las diferencias y ventajas de cada enfoque
4. **Documentación**: README.md y comentarios incluidos

Los dos enfoques son válidos, pero la POO es superior para proyectos complejos y de gran escala.

---

**Autor**: Octavio Álvarez  
**Asignatura**: Programación Orientada a Objetos  
**Fecha**: 13 de junio de 2026  
**Nivel**: 2do Semestre

