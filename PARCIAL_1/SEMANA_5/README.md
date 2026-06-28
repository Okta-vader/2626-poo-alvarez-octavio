# Sistema de Gestión de Restaurante - SEMANA 5

**Estudiante:** Octavio Álvarez Quintero

---

## 📋 Descripción General del Sistema

Este proyecto implementa un **Sistema Básico de Gestión de Restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema demuestra la aplicación de conceptos fundamentales como clases, objetos, tipos de datos básicos, listas como estructuras de datos compuestas, e importaciones modulares.

El objetivo principal es mostrar comprensión de cómo aplicar identificadores descriptivos, tipos de datos adecuados y organización modular en un proyecto Python funcional.

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/                    # Carpeta que contiene las clases base
│   ├── __init__.py            # Archivo para declarar el paquete
│   ├── producto.py            # Clase que representa un producto
│   └── cliente.py             # Clase que representa un cliente
├── servicios/                 # Carpeta que contiene las clases de gestión
│   ├── __init__.py            # Archivo para declarar el paquete
│   └── restaurante.py         # Clase que gestiona restaurante
└── main.py                    # Punto de entrada del programa
```

### Responsabilidad de cada módulo:

- **`modelos/producto.py`**: Define la clase `Producto` que representa artículos disponibles en el restaurante.
- **`modelos/cliente.py`**: Define la clase `Cliente` que representa personas registradas en el sistema.
- **`servicios/restaurante.py`**: Define la clase `Restaurante` que administra listas de productos y clientes.
- **`main.py`**: Script principal que inicializa objetos, ejecuta operaciones y muestra resultados.

---

## 🎯 Clases Implementadas

### 1. Clase `Producto` (modelos/producto.py)

Representa un plato, bebida o artículo disponible en el restaurante.

**Atributos:**
- `identificador: int` - ID único del producto
- `nombre: str` - Nombre descriptivo del producto
- `descripcion: str` - Breve descripción
- `precio: float` - Precio unitario en pesos
- `disponible: bool` - Estado de disponibilidad

**Métodos:**
- `__init__()` - Constructor que inicializa los atributos
- `__str__()` - Método especial para representar el producto como texto
- `cambiar_disponibilidad()` - Actualiza el estado de disponibilidad
- `actualizar_precio()` - Modifica el precio del producto
- `obtener_informacion_resumida()` - Retorna datos resumidos

**Tipos de datos utilizados:**
- `str` para nombre y descripción
- `int` para identificador
- `float` para precio
- `bool` para disponibilidad

---

### 2. Clase `Cliente` (modelos/cliente.py)

Representa un cliente registrado en el sistema del restaurante.

**Atributos:**
- `identificador: int` - Número de documento único
- `nombre_completo: str` - Nombre completo del cliente
- `numero_contacto: str` - Teléfono de contacto
- `correo_electronico: str` - Correo electrónico
- `es_cliente_frecuente: bool` - Indica si es cliente frecuente
- `saldo_disponible: float` - Saldo en cuenta

**Métodos:**
- `__init__()` - Constructor que inicializa los atributos
- `__str__()` - Método especial para representar el cliente como texto
- `marcar_como_frecuente()` - Marca cliente como frecuente
- `actualizar_saldo()` - Modifica el saldo del cliente
- `obtener_informacion_contacto()` - Retorna datos de contacto
- `validar_saldo()` - Verifica si hay saldo suficiente

**Tipos de datos utilizados:**
- `str` para nombre, contacto y email
- `int` para identificador
- `float` para saldo
- `bool` para estado de cliente frecuente

---

### 3. Clase `Restaurante` (servicios/restaurante.py)

Administra productos y clientes del restaurante.

**Atributos:**
- `nombre_restaurante: str` - Nombre del restaurante
- `ubicacion: str` - Ubicación del restaurante
- `productos: list[Producto]` - **Lista de productos**
- `clientes_registrados: list[Cliente]` - **Lista de clientes**

**Métodos principales:**
- `__init__()` - Constructor que inicializa el restaurante
- `agregar_producto()` - Añade un producto a la lista
- `agregar_cliente()` - Registra un cliente en el sistema
- `obtener_producto_por_id()` - Busca un producto por ID
- `obtener_cliente_por_id()` - Busca un cliente por ID
- `listar_productos()` - Muestra todos los productos
- `listar_clientes()` - Muestra todos los clientes
- `productos_disponibles_para_venta()` - Filtra productos disponibles
- `clientes_frecuentes()` - Filtra clientes frecuentes
- `obtener_total_inventario()` - Retorna cantidad de productos
- `obtener_total_clientes()` - Retorna cantidad de clientes
- `mostrar_informacion_general()` - Muestra resumen del restaurante

**Uso de Listas:**
- `productos: list[Producto]` - Almacena múltiples objetos de tipo Producto
- `clientes_registrados: list[Cliente]` - Almacena múltiples objetos de tipo Cliente

---

## 📊 Tipos de Datos Utilizados

El proyecto implementa todos los tipos básicos solicitados:

| Tipo | Uso | Ejemplo |
|------|-----|---------|
| `str` | Nombres, descripciones, contactos | `"Arepa con Queso"`, `"Carlos Rodríguez"` |
| `int` | Identificadores únicos | `1001`, `123456` |
| `float` | Precios y saldos | `8500.00`, `150000.00` |
| `bool` | Estados de disponibilidad y tipo de cliente | `disponible=True`, `es_cliente_frecuente=False` |
| `list` | Colecciones de objetos | `productos: list[Producto]`, `clientes_registrados: list[Cliente]` |

---

## 🚀 Funcionamiento de la Aplicación

El programa `main.py` realiza las siguientes operaciones:

1. **Inicialización del Restaurante**
   - Crea instancia de Restaurante llamado "Sabor Authentic"

2. **Creación de Productos** (4 productos de ejemplo)
   - Arepa con Queso (entrada)
   - Bandeja Paisa (plato principal)
   - Jugo Natural (bebida)
   - Flan Casero (postre - no disponible)

3. **Creación de Clientes** (2 clientes de ejemplo)
   - Carlos Rodríguez García (cliente frecuente)
   - María López Martínez (cliente regular)

4. **Operaciones Demostrativas**
   - Búsqueda de productos por ID
   - Búsqueda de clientes por ID
   - Listado de productos disponibles
   - Listado de clientes frecuentes
   - Actualización de disponibilidad
   - Cambio de precios
   - Gestión de saldos

5. **Visualización de Resultados**
   - Mostrar información general del restaurante
   - Listar todos los productos con detalles
   - Listar todos los clientes con información

---

## 💻 Cómo Ejecutar el Programa

### Requisitos:
- Python 3.8 o superior

### Pasos:

1. Acceder a la carpeta del proyecto:
   ```bash
   cd restaurante_app
   ```

2. Ejecutar el programa:
   ```bash
   python main.py
   ```

### Salida esperada:
El programa mostrará:
- Información inicial del restaurante
- Confirmación de productos agregados
- Confirmación de clientes registrados
- Listado completo de productos con detalles
- Listado completo de clientes con información
- Operaciones adicionales ejecutadas
- Información final del restaurante

---

## 🎓 Aspectos Didácticos Importantes

### 1. **Identificadores Descriptivos**
- **Clases**: `Producto`, `Cliente`, `Restaurante` (PascalCase)
- **Métodos**: `agregar_producto()`, `obtener_cliente_por_id()` (snake_case)
- **Variables**: `nombre_completo`, `numero_contacto`, `saldo_disponible` (snake_case)
- **Archivos**: `producto.py`, `cliente.py`, `restaurante.py` (snake_case)

### 2. **Tipos de Datos Adecuados**
- Cada atributo utiliza el tipo de dato más apropiado para su naturaleza
- Se incluyen anotaciones de tipo para mayor claridad

### 3. **Uso de Listas**
El proyecto demuestra dos formas de usar listas:
- **Almacenamiento**: `productos` y `clientes_registrados` guardan múltiples objetos
- **Filtrado**: Métodos que retornan sublistas (`productos_disponibles_para_venta()`, `clientes_frecuentes()`)

### 4. **Importaciones Modulares**
- Cada módulo importa solo lo que necesita
- Las clases están organizadas en paquetes lógicos (`modelos`, `servicios`)
- El archivo principal (`main.py`) importa de los paquetes

### 5. **Método Especial `__str__()`**
- Implementado en `Producto` y `Cliente` para representación legible
- Facilita la visualización ordenada de información

### 6. **Constructor `__init__()`**
- Todas las clases principales implementan inicializadores
- Permiten crear instancias con parámetros específicos

---

## 🔍 Reflexión: Importancia de las Mejores Prácticas

### Identificadores Descriptivos
Los nombres claros y descriptivos hacen el código **autoexplicativo** y facilitan:
- **Mantenimiento**: Otros desarrolladores (o nosotros en el futuro) entendemos rápidamente qué hace cada variable/método
- **Depuración**: Errores más fáciles de identificar y corregir
- **Escalabilidad**: Proyectos grandes requieren nombres que comuniquen intención

### Tipos de Datos Adecuados
Utilizar el tipo correcto previene:
- **Errores de lógica**: Un número guardado como string puede causar problemas inesperados
- **Confusión**: El tipo de dato comunica qué se espera en cada campo
- **Validaciones**: Ciertos tipos permiten validaciones automáticas

### Listas en Proyectos Modulares
Las listas permiten:
- **Escalabilidad**: Manejar múltiples objetos sin crear variables individuales
- **Flexibilidad**: Operaciones sobre colecciones completas (filtrado, búsqueda, iteración)
- **Organización**: Agrupar datos relacionados de forma lógica
- **Reutilización**: Métodos genéricos que trabajan con cualquier cantidad de items

---

## 📝 Cumplimiento de Requisitos

✅ Estructura modular con carpetas `modelos` y `servicios`  
✅ Clases `Producto`, `Cliente` y `Restaurante` implementadas  
✅ Constructores `__init__()` en todas las clases  
✅ Identificadores descriptivos en clases, métodos, variables y archivos  
✅ Convenciones PascalCase para clases y snake_case para variables  
✅ Tipos de datos básicos: `str`, `int`, `float`, `bool`  
✅ Listas como tipo compuesto: `list[Producto]` y `list[Cliente]`  
✅ Anotaciones de tipo en atributos  
✅ Métodos para gestionar información  
✅ Método `__str__()` para representación de objetos  
✅ Importaciones correctas entre módulos  
✅ Al menos 2 objetos de cada modelo en main.py  
✅ Objetos agregados a listas administradas  
✅ Información mostrada de forma organizada  
✅ Comentarios explicativos en código  

---

## 📚 Conclusión

Este proyecto demuestra la correcta aplicación de Programación Orientada a Objetos en Python, respetando principios de modularidad, legibilidad y mantenibilidad del código. La estructura implementada sirve como base para sistemas más complejos de gestión empresarial.

---

**Fecha:** Junio 2026  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 5
