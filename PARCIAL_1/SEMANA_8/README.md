# Sistema de Restaurante - Semana 8

## Información del Estudiante
**Nombre Completo:** Octavio Manuel Alvarez Cedeño

## Descripción del Sistema

El presente proyecto es una versión mejorada del sistema de gestión de restaurante desarrollado en Python como parte de la evaluación de la Semana 8 de la asignatura **Programación Orientada a Objetos**.

Este proyecto evidencia la aplicación de los **principios SOLID**, especialmente:

- **S (Responsabilidad Única):** Cada clase tiene una responsabilidad claramente definida
- **O (Abierto/Cerrado):** El sistema está abierto para extensión mediante nuevas clases
- **L (Sustitución de Liskov):** Las clases hijas pueden usarse donde se espera la clase padre

El sistema permite registrar y listar **productos**, **bebidas** (como variación de productos) y **clientes** mediante una interfaz interactiva de consola. La clave de este diseño es que los productos y las bebidas se almacenan en una **lista común**, demostrando así el poder del polimorfismo.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

### Responsabilidad de cada módulo

#### `modelos/producto.py`
Define la clase **Producto** que representa un artículo general del restaurante. Características principales:

- **Atributos:** codigo, nombre, categoria, precio
- **Métodos principales:**
  - `mostrar_informacion()`: Retorna información del producto
  - Validaciones en el constructor para datos coherentes
  - Implementa `__eq__` y `__hash__` para comparabilidad

#### `modelos/bebida.py`
Define la clase **Bebida** que hereda de **Producto** e incorpora información específica de bebidas.

**Características principales:**
- **Herencia:** Bebida es una clase hija de Producto
- **Atributos adicionales:** tamaño, tipo_envase
- **Sobreescritura de métodos:** 
  - `mostrar_informacion()`: Presenta información detallada de la bebida
  - `__str__()`: Representación customizada
- **Sustitución de Liskov:** Una Bebida puede utilizarse en cualquier contexto donde se espera un Producto

#### `modelos/cliente.py`
Define la clase **Cliente** que representa a un cliente registrado en el restaurante.

**Características principales:**
- **Atributos:** identificacion, nombre, correo
- **Métodos:** mostrar_informacion(), validaciones en constructor
- **Responsabilidad única:** Solo maneja información del cliente

#### `servicios/restaurante.py`
Define la clase **Restaurante** que actúa como servicio central.

**Características principales:**
- **Responsabilidad:** Administrar colecciones de productos y clientes
- **Lista común de productos:** Almacena tanto Productos como Bebidas juntos
- **Polimorfismo en acción:** Itera sobre productos sin necesidad de validar tipo
- **Métodos principales:**
  - `registrar_producto()`: Agrega cualquier tipo de Producto
  - `listar_productos()`: Retorna todos los productos (polimórficos)
  - Métodos análogos para clientes

#### `main.py`
Archivo principal que orquesta la aplicación.

**Responsabilidades:**
- Mostrar el menú interactivo
- Solicitar datos del usuario
- Crear objetos (Producto, Bebida, Cliente)
- Llamar a métodos del servicio Restaurante
- No administrar directamente las listas internas

## Conceptos SOLID Aplicados

### S — Responsabilidad Única
Cada clase tiene una responsabilidad claramente definida:

```
Producto    → Representa un artículo básico del restaurante
Bebida      → Extiende Producto con información de bebidas
Cliente     → Maneja información del cliente
Restaurante → Administra colecciones y operaciones
main.py     → Coordina interacción con el usuario
```

### O — Abierto/Cerrado
El sistema está **abierto para extensión** sin necesidad de modificar código existente:

```python
# Podemos crear nuevas clases que hereden de Producto
class Postre(Producto):
    def __init__(self, codigo, nombre, categoria, precio, temperatura):
        super().__init__(codigo, nombre, categoria, precio)
        self.temperatura = temperatura
    
    def mostrar_informacion(self):
        # Información personalizada del postre
        pass

# Sin cambiar Restaurante, podemos registrar postres:
postre = Postre("P001", "Flan", "Postres", 5.99, "Frio")
restaurante.registrar_producto(postre)
```

### L — Sustitución de Liskov
Un objeto Bebida puede utilizarse en cualquier contexto donde se espere un Producto:

```python
# Ambos funcionan de la misma forma en el servicio
producto = Producto("P001", "Pizza", "Comida", 15.00)
bebida = Bebida("B001", "Coca Cola", "Bebidas", 2.50, "Mediano", "Botella")

restaurante.registrar_producto(producto)
restaurante.registrar_producto(bebida)

# Cuando se listan, cada uno muestra su información según su propia implementación
for item in restaurante.listar_productos():
    print(item.mostrar_informacion())  # Polimorfismo en acción
```

## Herencia y Polimorfismo

### Diagrama de Herencia
```
    Producto (clase base)
       ↑
       |
      Bebida (clase hija - extiende Producto)
```

### Demostración de Polimorfismo
El verdadero poder del diseño se aprecia en el método `listar_productos()`:

```python
def listar_productos(self, restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()
    
    for producto in productos:
        # SIN necesidad de validar tipo:
        # if isinstance(producto, Bebida):
        # if isinstance(producto, Producto):
        
        # Simplemente llamamos el método comun
        print(producto.mostrar_informacion())
        
        # Cada objeto sabe cómo mostrarse a sí mismo
        # Producto mostrará sus datos
        # Bebida mostrará sus datos (tamaño, envase, etc.)
```

Este patrón elimina la necesidad de condicionales repetidos y es **muy escalable**.

## Menú Interactivo

```
==================================================
        SISTEMA DE RESTAURANTE
==================================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
--------------------------------------------------
4. Listar productos
5. Listar clientes
--------------------------------------------------
6. Salir
==================================================
```

### Opciones Disponibles

1. **Registrar Producto (Opción 1)**
   - Solicita: código, nombre, categoría, precio
   - Valida que no exista código duplicado
   - Crea objeto mediante constructor de Producto

2. **Registrar Bebida (Opción 2)**
   - Solicita: código, nombre, categoría, precio, tamaño, tipo de envase
   - Hereda validaciones de Producto
   - Crea objeto mediante constructor de Bebida
   - Se almacena en la misma lista de productos

3. **Registrar Cliente (Opción 3)**
   - Solicita: identificación, nombre, correo
   - Valida que no exista identificación duplicada
   - Crea objeto mediante constructor de Cliente

4. **Listar Productos (Opción 4)**
   - Muestra todos los productos y bebidas
   - Demuestra polimorfismo
   - Cada item usa su propio mostrar_informacion()

5. **Listar Clientes (Opción 5)**
   - Muestra todos los clientes registrados
   - Presenta información detallada

6. **Salir (Opción 6)**
   - Finaliza la aplicación

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

### Ejemplo de sesión

```
[BIENVENIDA] Bienvenido al Sistema de Restaurante!

==================================================
        SISTEMA DE RESTAURANTE
==================================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
--------------------------------------------------
4. Listar productos
5. Listar clientes
--------------------------------------------------
6. Salir
==================================================
Seleccione una opcion: 1

--- Registrar Nuevo Producto ---
Codigo del producto: P001
Nombre del producto: Pizza Margherita
Categoria (ej: Comida, Acompañamientos): Comida
Precio (ej: 10.50): 15.99
[OK] Producto 'Pizza Margherita' registrado exitosamente.

Seleccione una opcion: 2

--- Registrar Nueva Bebida ---
Codigo de la bebida: B001
Nombre de la bebida: Coca Cola
Categoria (ej: Bebidas Frias, Bebidas Calientes): Bebidas Frias
Precio (ej: 3.50): 2.50
Tamaño (ej: Pequeño, Mediano, Grande): Mediano
Tipo de envase (ej: Botella, Lata, Vaso): Botella
[OK] Bebida 'Coca Cola' registrada exitosamente.
```

## Validaciones Implementadas

### Para Producto
- ✓ Código no puede estar vacío
- ✓ Nombre no puede estar vacío
- ✓ Categoría no puede estar vacía
- ✓ Precio debe ser mayor a cero
- ✓ Códigos no pueden duplicarse

### Para Bebida
- ✓ Hereda todas las validaciones de Producto
- ✓ Tamaño no puede estar vacío
- ✓ Tipo de envase no puede estar vacío

### Para Cliente
- ✓ Identificación no puede estar vacía
- ✓ Nombre no puede estar vacío
- ✓ Correo no puede estar vacío
- ✓ Identificaciones no pueden duplicarse

## Tipos de Datos Utilizados

Todos los constructores, métodos y funciones incluyen anotaciones de tipos:

```python
def __init__(
    self,
    codigo: str,
    nombre: str,
    categoria: str,
    precio: float
) -> None:
    """..."""
```

Esto mejora:
- **Legibilidad:** El código es más claro
- **Mantenibilidad:** Es fácil entender qué espera cada función
- **Detección de errores:** IDEs y herramientas pueden detectar inconsistencias

## Comparación: Semana 7 vs Semana 8

| Característica | SEMANA_7 | SEMANA_8 |
|---|---|---|
| Clase Producto | Con @property/@setter | Con herencia |
| Clase Bebida | No existe | Hereda de Producto |
| Almacenamiento | Listas separadas | Lista común |
| Polimorfismo | No | Sí (en mostrar_informacion) |
| Principios SOLID | Responsabilidad única | S, O, L completos |
| Validación | En setters | En constructores |
| Menú opciones | 7 opciones | 6 opciones |

## Ventajas del Diseño Semana 8

1. **Escalabilidad:** Puede agregar nuevas clases que hereden de Producto sin modificar Restaurante
2. **Mantenibilidad:** Código más limpio sin condicionales tipo-específicos
3. **Reutilización:** Código común en Producto se hereda automáticamente
4. **Flexibilidad:** El polimorfismo permite diferentes implementaciones de mostrar_informacion()
5. **Principios SOLID:** Demuestra cómo usar herencia correctamente en POO

## Conclusión

El proyecto SEMANA_8 mejora significativamente sobre SEMANA_7 mediante la aplicación adecuada de herencia y polimorfismo. La clase Bebida no es una copia de Producto, sino una **especialización coherente** que demuestra los principios fundamentales de la Programación Orientada a Objetos.

El sistema es:
- ✅ Modular y bien organizado
- ✅ Fácil de entender y mantener
- ✅ Preparado para futuros cambios
- ✅ Demostrativo de principios SOLID
- ✅ Escalable para nuevas entidades

---

**Fecha de entrega:** Semana 8 - Programación Orientada a Objetos
