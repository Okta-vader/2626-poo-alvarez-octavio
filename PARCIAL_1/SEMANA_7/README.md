# Sistema de Restaurante - Semana 7

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

El presente proyecto es un sistema de gestión de restaurante desarrollado en Python como parte de la evaluación de la Semana 7 de la asignatura **Programación Orientada a Objetos**. 

El sistema permite registrar, listar y buscar **productos** y **clientes** de un restaurante mediante una interfaz interactiva de consola. El objetivo principal es demostrar la comprensión y aplicación correcta de conceptos fundamentales de la Programación Orientada a Objetos, tales como:

- Constructores tradicionales y personalizados
- Uso de decoradores `@property` y `@setter` para encapsulación
- Uso del decorador `@dataclass` para simplificar clases
- Arquitectura modular por capas
- Creación dinámica de objetos a partir de entrada del usuario
- Validación de datos y manejo de excepciones

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

### Responsabilidad de cada módulo

#### `modelos/producto.py`
Define la clase **Producto** que representa un artículo disponible en el restaurante. Características principales:

- **Constructor tradicional (`__init__`):** Inicializa los atributos privados del producto (nombre, categoría, precio, disponibilidad)
- **Atributos:** 
  - `_nombre`: Nombre del producto
  - `_categoria`: Categoría a la que pertenece
  - `_precio`: Precio unitario
  - `_disponible`: Estado de disponibilidad

- **Métodos principales:**
  - `mostrar_informacion()`: Retorna información detallada del producto
  - `__str__()`: Representación amigable en string
  - `__repr__()`: Representación oficial del objeto

#### `modelos/cliente.py`
Define la clase **Cliente** que representa a un cliente registrado en el restaurante. Características principales:

- **Decorador `@dataclass`:** Simplifica la definición de la clase generando automáticamente `__init__`, `__repr__` y otros métodos especiales
- **Atributos:** 
  - `nombre`: Nombre completo del cliente
  - `correo`: Correo electrónico
  - `id_cliente`: Identificador único del cliente

- **Métodos principales:**
  - `mostrar_informacion()`: Retorna información detallada del cliente
  - `__str__()`: Representación amigable en string

#### `servicios/restaurante.py`
Define la clase **Restaurante** que actúa como servicio central para administrar productos y clientes. Características principales:

- **Responsabilidades:**
  - Mantener listas de productos y clientes
  - Registrar nuevos productos y clientes
  - Listar todos los registros
  - Buscar registros por criterios específicos
  - Validar duplicados

- **Métodos para Productos:**
  - `registrar_producto()`: Agrega un nuevo producto
  - `listar_productos()`: Retorna la lista de productos
  - `buscar_producto()`: Busca por nombre (case-insensitive)
  - `obtener_productos_disponibles()`: Retorna solo productos disponibles

- **Métodos para Clientes:**
  - `registrar_cliente()`: Agrega un nuevo cliente
  - `listar_clientes()`: Retorna la lista de clientes
  - `buscar_cliente()`: Busca por nombre (case-insensitive)
  - `buscar_cliente_por_id()`: Busca por identificador único

#### `main.py`
Archivo principal que contiene la lógica del menú interactivo y orquesta toda la aplicación. Características principales:

- **Menú interactivo:** Presenta opciones de registro, listado y búsqueda
- **Flujo de entrada de datos:** 
  1. Solicitar información al usuario mediante `input()`
  2. Validar datos ingresados
  3. Crear objetos mediante constructores
  4. Almacenar en la clase Restaurante
  5. Mostrar resultados

- **Funciones principales:**
  - `registrar_producto()`: Interfaz para crear nuevos productos
  - `listar_productos()`: Muestra todos los productos
  - `buscar_producto()`: Busca un producto específico
  - `registrar_cliente()`: Interfaz para crear nuevos clientes
  - `listar_clientes()`: Muestra todos los clientes
  - `buscar_cliente()`: Busca un cliente específico
  - `main()`: Ejecuta el bucle principal del programa

## Uso del Constructor en la Clase Producto

La clase `Producto` implementa un **constructor tradicional** `__init__` que:

```python
def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
    self._nombre = ""
    self._categoria = ""
    self._precio = 0.0
    self._disponible = disponible
    
    # Usar setters para aplicar validaciones
    self.nombre = nombre
    self.categoria = categoria
    self.precio = precio
```

- **Inicializa atributos privados** con valores por defecto
- **Utiliza setters** para aplicar validaciones al momento de la asignación
- **Permite parámetros opcionales** (disponible tiene valor por defecto True)
- **Genera excepciones** si los datos no cumplen validaciones

**Ejemplo de uso:**
```python
# Crear un producto mediante el constructor
producto = Producto("Pizza Margherita", "Comida", 12.50, True)
```

## Uso de @property y @setter

La clase `Producto` implementa decoradores `@property` y `@setter` para cada atributo principal:

### Decorador @property
Permite acceso de lectura controlada a los atributos privados:

```python
@property
def nombre(self) -> str:
    """Retorna el nombre del producto."""
    return self._nombre
```

### Decorador @setter
Permite modificación controlada con **validaciones**:

```python
@nombre.setter
def nombre(self, valor: str) -> None:
    """Establece el nombre del producto con validación."""
    if not valor or not valor.strip():
        raise ValueError("El nombre del producto no puede estar vacío.")
    self._nombre = valor.strip()
```

### Validaciones Implementadas

1. **Nombre:** No puede estar vacío o contener solo espacios
2. **Categoría:** No puede estar vacía o contener solo espacios
3. **Precio:** Debe ser un número válido y mayor que cero

**Ejemplo de validación:**
```python
try:
    producto = Producto("", "Bebidas", 5.0)  # Error: nombre vacío
except ValueError as e:
    print(f"Error: {e}")
```

## Uso de @dataclass en la Clase Cliente

La clase `Cliente` implementa el **decorador `@dataclass`** que simplifica su definición:

```python
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
```

### Ventajas del @dataclass
- **Genera automáticamente** el método `__init__`
- **Genera automáticamente** los métodos `__repr__` y `__eq__`
- **Reduce código boilerplate** significativamente
- **Facilita la lectura** y mantenimiento del código
- **Proporciona tipado estático** con type hints

**Comparación con enfoque tradicional:**
```python
# Sin @dataclass (enfoque tradicional)
class ClienteTradicional:
    def __init__(self, nombre: str, correo: str, id_cliente: str):
        self.nombre = nombre
        self.correo = correo
        self.id_cliente = id_cliente
    
    def __repr__(self):
        return f"ClienteTradicional(nombre='{self.nombre}', ...)"

# Con @dataclass (enfoque moderno)
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
    # Todo lo demás se genera automáticamente
```

**Ejemplo de uso:**
```python
# Crear un cliente mediante el constructor generado por @dataclass
cliente = Cliente(nombre="Juan Pérez", correo="juan@email.com", id_cliente="C001")
print(cliente)  # Automatic __repr__: Cliente(nombre='Juan Pérez', ...)
```

## Descripción del Menú Interactivo

El menú interactivo del sistema presenta las siguientes opciones:

```
==================================================
        SISTEMA DE RESTAURANTE
==================================================
1. Registrar producto
2. Listar productos
3. Buscar producto
--------------------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
--------------------------------------------------
7. Salir
==================================================
```

### Flujo de Interacción

1. **Registrar Producto (Opción 1)**
   - Solicita: nombre, categoría, precio, disponibilidad
   - Crea objeto `Producto` mediante constructor
   - Almacena en la clase `Restaurante`
   - Valida datos y muestra confirmación

2. **Listar Productos (Opción 2)**
   - Muestra todos los productos registrados
   - Presenta información detallada de cada uno
   - Indica total de productos

3. **Buscar Producto (Opción 3)**
   - Solicita nombre del producto
   - Realiza búsqueda case-insensitive
   - Muestra detalles si lo encuentra

4. **Registrar Cliente (Opción 4)**
   - Solicita: nombre, correo, ID del cliente
   - Crea objeto `Cliente` mediante @dataclass
   - Almacena en la clase `Restaurante`
   - Valida que no exista cliente con mismo ID

5. **Listar Clientes (Opción 5)**
   - Muestra todos los clientes registrados
   - Presenta información detallada de cada uno
   - Indica total de clientes

6. **Buscar Cliente (Opción 6)**
   - Solicita nombre del cliente
   - Realiza búsqueda case-insensitive
   - Muestra detalles si lo encuentra

7. **Salir (Opción 7)**
   - Finaliza la ejecución del programa
   - Muestra mensaje de despedida

## Cómo Ejecutar el Programa

### Requisitos
- Python 3.7 o superior
- No se requieren librerías externas

### Pasos para ejecutar

1. Navegar a la carpeta del proyecto:
   ```bash
   cd restaurante_app
   ```

2. Ejecutar el archivo principal:
   ```bash
   python main.py
   ```

3. El programa mostrará el menú interactivo
4. Seleccionar una opción ingresando el número correspondiente
5. Seguir las instrucciones en pantalla

### Ejemplo de sesión
```
¡Bienvenido al Sistema de Restaurante!

==================================================
        SISTEMA DE RESTAURANTE
==================================================
1. Registrar producto
...
7. Salir
==================================================
Seleccione una opción: 1

--- Registrar Nuevo Producto ---
Nombre del producto: Pizza Margherita
Categoría (ej: Bebidas, Comida, Postres): Comida
Precio (ej: 5.99): 12.50
¿Disponible? (s/n, por defecto 's'): s
✓ Producto 'Pizza Margherita' registrado exitosamente.
```

## Importancias de Crear Objetos a partir de Datos Ingresados por Usuario

La presente actividad enfatiza un principio fundamental de la **Programación Orientada a Objetos**: la transformación de datos de entrada en **objetos significativos** que modelan entidades del dominio.

### ¿Por qué es importante?

1. **Encapsulación y Validación:** Al crear objetos mediante constructores, se garantiza que los datos sean válidos desde el inicio. Los setters con validaciones previenen estados inválidos.

2. **Abstracción Controlada:** Los datos ingresados se abstraen en objetos que ocultan la complejidad. El usuario no manipula strings sueltos, sino objetos `Producto` y `Cliente` coherentes.

3. **Reutilización de Código:** Una vez creado el objeto, puede ser procesado, almacenado, modificado y buscado mediante métodos bien definidos, sin repetir lógica.

4. **Mantenibilidad:** Los cambios en la estructura de datos se centralizan en la definición de clases, no dispersos por todo el programa.

5. **Modelado Real:** Los objetos en el código modelan conceptos reales (producto, cliente) con sus propiedades y comportamientos, facilitando la comprensión del programa.

### Relación con Arquitectura en Capas

Este proyecto demuestra la arquitectura en capas:

- **Capa de Modelos:** Definen la estructura de datos (Producto, Cliente)
- **Capa de Servicios:** Administran lógica de negocio (Restaurante)
- **Capa de Presentación:** Interactúan con el usuario (main.py)

Este diseño permite cambiar cualquier capa sin afectar las otras, mejorando la mantenibilidad y escalabilidad.

## Conclusión

Este proyecto evidencia la aplicación práctica de Programación Orientada a Objetos en un contexto realista. Mediante el uso de constructores, decoradores, propiedades y una arquitectura modular, se ha desarrollado un sistema que:

- ✅ Valida datos desde su creación
- ✅ Encapsula comportamiento y estado
- ✅ Separa responsabilidades en capas
- ✅ Permite interacción dinámica con el usuario
- ✅ Mantiene código limpio, legible y mantenible

La estructura modular y los principios aplicados proporcionan una base sólida para expandir el sistema con nuevas funcionalidades en el futuro.

---

**Fecha de entrega:** Semana 7 - Programación Orientada a Objetos
