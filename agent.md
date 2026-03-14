# Documentación del Agente - Sistema de Inventario

## 1. Visión General del Proyecto

**Nombre:** Sistema de Gestión de Inventario  
**Tipo:** Aplicación de consola en Python  
**Objetivo:** Crear un sistema de inventario básico que permita gestionar productos con operaciones CRUD, persistiendo datos en Excel.  
**Propósito educativo:** Aprender arquitectura de software y desarrollo asistido con IA.

---

## 2. Arquitectura del Proyecto

```
┌─────────────────────────────────────────────────────────────┐
│                        main.py                               │
│                    (Punto de entrada)                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                        menu.py                               │
│              (Interfaz de usuario - CLI)                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  inventory_manager.py                       │
│                   (Lógica del negocio)                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     excel_manager.py                         │
│               (Capa de acceso a datos)                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      inventario.xlsx                        │
│                   (Persistencia de datos)                    │
└─────────────────────────────────────────────────────────────┘
```

### Patrón de diseño: MVC simplificado

- **Model:** excel_manager.py (manejo de datos)
- **View:** menu.py (presentación en consola)
- **Controller:** inventory_manager.py (lógica de negocio)

---

## 3. Estructura de Datos

### Producto (fila en Excel)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| codigo | string | Identificador único del producto |
| producto | string | Nombre del producto |
| precio_compra | float | Costo de adquisición |
| precio_venta | float | Precio de venta al público |
| stock | int | Cantidad disponible |

---

## 4. Responsabilidades de Cada Archivo

### 4.1 main.py
- **Responsabilidad:** Punto de entrada del programa
- **Funciones:**
  - Inicializar la aplicación
  - Lanzar el menú principal
  - Manejar excepciones globales
- **No debe hacer:** Lógica de negocio ni acceso a datos

### 4.2 menu.py
- **Responsabilidad:** Interactuar con el usuario
- **Funciones:**
  - Mostrar menú principal con opciones
  - Recibir y validar input del usuario
  - Llamar a las funciones correspondientes del inventory_manager
  - Mostrar resultados de operaciones
  - **Confirmar eliminación (S/N)** antes de llamar a eliminar
- **No debe hacer:** Manipular datos directamente ni contener lógica de negocio

### 4.3 inventory_manager.py
- **Responsabilidad:** Lógica del negocio
- **Funciones:**
  - `agregar_producto(codigo, producto, precio_compra, precio_venta, stock)`
  - `eliminar_producto(codigo)`
  - `buscar_producto(codigo)` → dict o None
  - `actualizar_precio(codigo, nuevo_precio)`
  - `actualizar_stock(codigo, nueva_cantidad)`
  - `ver_productos()` → list
  - Validar datos de entrada
  - Validar reglas de negocio (ej: stock no negativo, precios positivos)
- **No debe hacer:** Lectura/escritura directa a Excel

### 4.4 excel_manager.py
- **Responsabilidad:** Acceso y persistencia de datos
- **Funciones:**
  - `cargar_datos()` → DataFrame
  - `guardar_datos(df)` → None
  - `existe_producto(codigo)` → bool
  - `leer_producto(codigo)` → dict o None
  - `escribir_producto(producto)` → None
  - `actualizar_producto(codigo, datos)` → None
  - `eliminar_producto(codigo)` → None
- **No debe hacer:** Validación de reglas de negocio

---

## 5. Flujo del Sistema

```
┌──────────────┐     ┌──────────────┐     ┌────────────────────┐     ┌───────────────┐
│   Usuario    │────▶│    menu.py   │────▶│ inventory_manager  │────▶│excel_manager  │
│  (Console)   │◀────│  (presenta)  │◀────│    (lógica)        │◀────│   (datos)     │
└──────────────┘     └──────────────┘     └────────────────────┘     └───────────────┘
                                                                    │
                                                                    ▼
                                                             ┌───────────────┐
                                                             │inventario.xlsx │
                                                             │  (archivo)     │
                                                             └───────────────┘
```

### Flujo detallado para cada operación:

**Ver productos:**
1. Usuario selecciona opción en menu.py
2. menu.py llama a `inventory_manager.ver_productos()`
3. inventory_manager llama a `excel_manager.cargar_datos()`
4. excel_manager retorna DataFrame
5. inventory_manager retorna lista de productos
6. menu.py formatea y muestra al usuario

**Agregar producto:**
1. Usuario ingresa datos en menu.py
2. menu.py valida formato básico y llama a `inventory_manager.agregar_producto()`
3. inventory_manager valida reglas de negocio
4. inventory_manager llama a `excel_manager.escribir_producto()`
5. excel_manager guarda en Excel
6. Retorna éxito/fracaso

**Eliminar producto:**
1. Usuario ingresa código en menu.py
2. menu.py verifica que existe el producto
3. **menu.py muestra confirmación "¿Está seguro de eliminar? (S/N)"**
4. Si usuario confirma con "S", menu.py llama a `inventory_manager.eliminar_producto(codigo)`
5. Retorna resultado de la operación

**Buscar/Actualizar:** Similar flujo, usando métodos específicos

---

## 6. Plan de Implementación

### Fase 1: Infraestructura base ✅

1. **Crear excel_manager.py** ✅
2. **Crear inventory_manager.py** ✅
3. **Crear menu.py** ✅
4. **Crear main.py** ✅

### Fase 2: Funcionalidades ✅

- Ver productos ✅
- Buscar producto ✅
- Agregar producto ✅
- Eliminar producto (con confirmación S/N) ✅
- Actualizar precio ✅
- Actualizar stock ✅

### Fase 3: Refinamiento

- Manejo de errores adicionales
- Mejoras de UX

---

## 7. Buenas Prácticas

### 7.1 Código limpio
- **Nombres descriptivos:** Usar nombres claros para variables y funciones
- **Funciones pequeñas:** Cada función hace una cosa
- **DRY (Don't Repeat Yourself):** No duplicar código

### 7.2 Manejo de errores
- Usar `try-except` para operaciones que pueden fallar
- Validar datos de entrada en inventory_manager (no en UI)
- Mostrar mensajes de error claros al usuario

### 7.3 Estructura
- Imports organizados al inicio del archivo
- Un archivo = una responsabilidad clara

### 7.4 Nomenclatura Python
- `snake_case` para funciones y variables
- Módulos con nombres en minúsculas

---

## 8. Confirmación de Eliminación

**Requisito implementado:** Antes de eliminar un producto, mostrar confirmación simple (S/N).

**Flujo en menu.py:**
```
1. Usuario elige opción eliminar
2. Ingresa código del producto
3. Sistema verifica que existe
4. Muestra: "¿Está seguro de eliminar? (S/N)"
5. Si ingresa "S" o "s" → procede a eliminar
6. Si ingresa "N" o "n" o cualquier otra cosa → cancela operación
```

---

## 9. Dependencias

```python
pandas>=1.5.0
openpyxl>=3.0.0
```

---

## 10. Extensiones Futuras

- Interfaz gráfica (GUI)
- Base de datos real (SQL)
- Reportes y estadísticas
- Categorías de productos
- API REST
