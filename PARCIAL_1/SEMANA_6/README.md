# Restaurante App - Sistema de Gestión de Productos POO

## Información del Estudiante
**Nombre:** Octavio Álvarez  
**Semana:** Semana 6 - Programación Orientada a Objetos  
**Asignatura:** Programación Orientada a Objetos (POO)  
**Institución:** Universidad Estatal Amazónica

---

## Descripción del Sistema

**Restaurante App** es un sistema de gestión de productos para un restaurante que aplica los principios fundamentales de la Programación Orientada a Objetos. El sistema permite administrar platillos y bebidas con diferentes características específicas, demostrando cómo la herencia, encapsulación y polimorfismo mejoran la organización y reutilización del código.

### Objetivo
Desarrollar una aplicación modular que evidencie la aplicación práctica de conceptos POO mediante una jerarquía de clases lógica y bien estructurada.

---

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py           # Inicializador del módulo
│   ├── producto.py           # Clase padre Producto
│   ├── platillo.py           # Clase hija Platillo
│   └── bebida.py             # Clase hija Bebida
├── servicios/
│   ├── __init__.py           # Inicializador del módulo
│   └── restaurante.py        # Clase de servicio Restaurante
└── main.py                   # Punto de entrada del programa
```

---

## Relación de Herencia

### Jerarquía de Clases

```
        Producto (Clase Padre)
           /        \
          /          \
    Platillo      Bebida
    (Clase Hija)  (Clase Hija)
```

### Explicación de la Herencia

- **Producto**: Clase padre que contiene los atributos y métodos comunes a cualquier producto del restaurante:
  - `nombre`: Identificador del producto
  - `__precio`: Precio del producto (encapsulado)
  - `disponibilidad`: Estado de disponibilidad

- **Platillo**: Clase hija que hereda de Producto y agrega atributos específicos de comidas:
  - `tipo_platillo`: Categoría (Entrada, Plato Fuerte, Postre)
  - `tiempo_preparacion`: Tiempo en minutos
  - `calorias`: Valor nutricional

- **Bebida**: Clase hija que hereda de Producto y agrega atributos específicos de bebidas:
  - `volumen_ml`: Cantidad en mililitros
  - `tipo_bebida`: Clasificación (Gaseosa, Café, Jugo, etc.)
  - `temperatura`: Forma de servicio (Fría, Caliente, etc.)

---

## Encapsulación

### Atributo Encapsulado

El atributo **`__precio`** está encapsulado en la clase `Producto` mediante el uso de convención de nombres Python (doble guión bajo `__`).

### Protección de Datos

- El precio no puede accederse directamente desde fuera de la clase
- Se valida que el precio sea siempre un valor positivo mayor a cero
- Se proporciona acceso controlado a través de métodos:

```python
def obtener_precio(self):
    """Obtiene el precio del producto."""
    return self.__precio

def cambiar_precio(self, nuevo_precio):
    """Cambia el precio con validación."""
    self.__precio = self._validar_precio(nuevo_precio)

def _validar_precio(self, precio):
    """Valida que el precio sea válido."""
    if precio <= 0:
        raise ValueError("El precio debe ser mayor a cero")
    return precio
```

### Beneficios

- **Seguridad**: Evita que se asignen valores inválidos
- **Validación**: Controla que el precio sea siempre coherente
- **Mantenibilidad**: Cambios futuros en la lógica de precios sin afectar el código externo
- **Integridad**: Protege la consistencia del objeto

---

## Polimorfismo

### Método Sobrescrito

El método `mostrar_informacion()` es sobrescrito en las clases hijas para proporcionar una representación específica de cada tipo de producto.

### Implementación

**En Producto (Clase Padre):**
```python
def mostrar_informacion(self):
    """Muestra información general del producto."""
    estado = "Disponible" if self.disponibilidad else "No disponible"
    return f"Producto: {self.nombre}\nPrecio: ${self.__precio:.2f}\nEstado: {estado}"
```

**En Platillo (Clase Hija):**
```python
def mostrar_informacion(self):
    """Muestra información específica del platillo."""
    # Formato personalizado con detalles de tiempo y calorías
    return f"PLATILLO\nNombre: {self.nombre}\n..."
```

**En Bebida (Clase Hija):**
```python
def mostrar_informacion(self):
    """Muestra información específica de la bebida."""
    # Formato personalizado con detalles de volumen y temperatura
    return f"BEBIDA\nNombre: {self.nombre}\n..."
```

### Demostración de Polimorfismo

En la clase `Restaurante`, el método `mostrar_menu_completo()` recorre una lista de productos y ejecuta `mostrar_informacion()`:

```python
def mostrar_menu_completo(self):
    """Polimorfismo: cada producto muestra su información de forma específica."""
    for i, producto in enumerate(self.productos, 1):
        print(f"{i}. {producto.mostrar_informacion()}\n")
```

**Resultado**: Cada objeto ejecuta su propia versión del método según su tipo:
- Si es un `Platillo`, muestra información con formato de platillo
- Si es una `Bebida`, muestra información con formato de bebida

---

## Uso de super()

La palabra clave `super()` se utiliza en las clases hijas para reutilizar el constructor y métodos de la clase padre:

**En Platillo:**
```python
def __init__(self, nombre, precio, tipo_platillo, tiempo_preparacion, calorias, disponibilidad=True):
    super().__init__(nombre, precio, disponibilidad)  # Inicializa atributos de Producto
    self.tipo_platillo = tipo_platillo
    self.tiempo_preparacion = tiempo_preparacion
    self.calorias = calorias
```

**Beneficios:**
- Evita duplicación de código
- Mantiene la validación de la clase padre
- Facilita cambios futuros en la clase padre

---

## Clase de Servicio: Restaurante

La clase `Restaurante` actúa como un contenedor y administrador de productos:

### Responsabilidades

1. **Gestión de Productos**
   - `agregar_producto()`: Añade productos a la lista
   - `listar_productos_disponibles()`: Filtra productos disponibles

2. **Búsqueda y Consulta**
   - `buscar_producto_por_nombre()`: Localiza un producto específico
   - `obtener_precio_promedio()`: Calcula estadísticas

3. **Presentación**
   - `mostrar_menu_completo()`: Exhibe todos los productos de forma organizada

---

## Ejecución del Programa

### Requisitos
- Python 3.6 o superior
- Sin dependencias externas

### Cómo Ejecutar

```bash
# Navegar a la carpeta del proyecto
cd restaurante_app

# Ejecutar el programa
python main.py
```

### Salida Esperada

El programa:
1. Crea una instancia del restaurante
2. Genera 3 platillos y 3 bebidas con diferentes características
3. Agrega todos los productos al restaurante
4. Muestra el menú completo (demostrando polimorfismo)
5. Valida la encapsulación intentando cambiar precios
6. Intenta cambiar un precio a un valor inválido (captura el error)
7. Lista estadísticas y búsquedas de productos

---

## Conceptos POO Aplicados

### 1. Herencia
✅ Platillo y Bebida heredan de Producto  
✅ Uso de `super()` para reutilizar constructores  
✅ Las clases hijas heredan todos los atributos y métodos de la clase padre

### 2. Encapsulación
✅ Atributo `__precio` encapsulado en Producto  
✅ Métodos de acceso: `obtener_precio()`  
✅ Métodos de modificación: `cambiar_precio()`  
✅ Validación de datos mediante `_validar_precio()`

### 3. Polimorfismo
✅ Método `mostrar_informacion()` sobrescrito en Platillo y Bebida  
✅ Mismo método ejecuta diferente comportamiento según el tipo  
✅ Demostrado al iterar la lista de productos en `mostrar_menu_completo()`

### 4. Abstracción
✅ Clase Restaurante abstrae la gestión de productos  
✅ Métodos claros y específicos para operaciones comunes

---

## Convenciones de Nombres

El proyecto sigue las convenciones de Python (PEP 8):

- **Clases**: `NombreClase` (PascalCase)
  - `Producto`, `Platillo`, `Bebida`, `Restaurante`

- **Métodos y variables**: `nombre_metodo` (snake_case)
  - `obtener_precio()`, `cambiar_precio()`, `mostrar_informacion()`

- **Constantes**: `NOMBRE_CONSTANTE` (UPPER_CASE)
  - No aplica en este proyecto

- **Atributos privados**: `_atributo` o `__atributo`
  - `__precio` (privado)
  - `_validar_precio()` (protegido)

---

## Reflexión: Importancia de POO en Proyectos Python Modulares

### ¿Por Qué Usar POO?

1. **Reutilización de Código**
   - La herencia permite compartir funcionalidad común entre clases
   - Evita duplicación y mantiene el código DRY (Don't Repeat Yourself)

2. **Mantenibilidad**
   - El código está organizado lógicamente en clases y módulos
   - Cambios en la clase padre se propagan automáticamente a las hijas
   - Facilita la depuración y las mejoras futuras

3. **Seguridad**
   - La encapsulación protege la integridad de los datos
   - Controla cómo se acceden y modifican los atributos
   - Previene errores por asignación de valores inválidos

4. **Escalabilidad**
   - Agregar nuevos tipos de productos es simple: solo crear nuevas clases hijas
   - El sistema puede crecer sin modificar código existente
   - Aplicable a cualquier número de productos

5. **Flexibilidad**
   - El polimorfismo permite trabajar con objetos de diferentes tipos de forma uniforme
   - El mismo código puede funcionar con objetos nuevos sin cambios

### En el Contexto de Restaurante App

En este proyecto:
- Agregar un nuevo tipo de producto (ej: `Postre`, `Entrada`) es trivial
- El atributo `__precio` nunca tendrá valores inválidos
- El menú se presenta de forma clara y específica para cada tipo
- El código es comprensible, mantenible y profesional

### Conclusión

La Programación Orientada a Objetos es fundamental para desarrollar aplicaciones Python robustas, escalables y mantenibles. Aunque este proyecto es educativo, demuestra cómo estos principios se aplican en sistemas reales.

---

## Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| `modelos/producto.py` | Clase padre Producto con encapsulación |
| `modelos/platillo.py` | Clase hija Platillo con atributos específicos |
| `modelos/bebida.py` | Clase hija Bebida con atributos específicos |
| `servicios/restaurante.py` | Clase de servicio para administración de productos |
| `main.py` | Punto de entrada: demostración del sistema |
| `README.md` | Este archivo de documentación |

---

## Licencia
Este proyecto es educativo y forma parte de la asignatura de Programación Orientada a Objetos.

---

**Fecha de creación:** Semana 6  
**Estado:** Completado ✓
