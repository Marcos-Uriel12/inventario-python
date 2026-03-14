# Plan de Pruebas - Sistema de Inventario

## Estado: ✅ COMPLETADO - 27/27 PRUEBAS PASARON

## 1. Casos de Uso Normales (Happy Path)

### 1.1 Agregar Producto
- [x] Agregar producto con datos válidos
- [x] Verificar que aparece en "ver productos"
- [x] Verificar que se guarda en Excel

### 1.2 Ver Productos
- [x] Ver lista vacía cuando no hay productos
- [x] Ver lista con productos existentes
- [x] Verificar formato de tabla correcto

### 1.3 Buscar Producto
- [x] Buscar producto existente por código
- [x] Buscar producto inexistente

### 1.4 Actualizar Precio
- [x] Actualizar precio de producto existente
- [x] Verificar cambio en "ver productos"

### 1.5 Actualizar Stock
- [x] Actualizar stock de producto existente
- [x] Verificar cambio en "ver productos"

### 1.6 Eliminar Producto
- [x] Eliminar producto con confirmación "S"
- [x] Cancelar eliminación con "N"
- [x] Verificar que ya no aparece en lista

---

## 2. Casos Extremos (Edge Cases)

### 2.1 Código
| Caso | Entrada | Resultado Esperado | Estado |
|------|---------|-------------------|--------|
| Código vacío | "" | "El código no puede estar vacío" | ✅ |
| Código con espacios | " P001 " | Aceptar (se recorta) | ✅ |
| Código duplicado | "P001" (ya existe) | "El código ya existe" | ✅ |
| Código inexistente | "XYZ999" | "El producto no existe" | ✅ |

### 2.2 Producto (Nombre)
| Caso | Entrada | Resultado Esperado | Estado |
|------|---------|-------------------|--------|
| Nombre vacío | "" | "El nombre del producto no puede estar vacío" | ✅ |
| Nombre con espacios | "  Producto  " | Aceptar (se recorta) | ✅ |

### 2.3 Precios
| Caso | Entrada | Resultado Esperado | Estado |
|------|---------|-------------------|--------|
| Precio negativo | -10 | "Los precios no pueden ser negativos" | ✅ |
| Precio cero | 0 | Aceptar | ✅ |
| Precio compra > venta | compra=100, venta=50 | "El precio de compra no puede ser mayor al precio de venta" | ✅ |
| Precio no numérico | "abc" | "Los precios y stock deben ser numéricos" | ✅ |

### 2.4 Stock
| Caso | Entrada | Resultado Esperado | Estado |
|------|---------|-------------------|--------|
| Stock negativo | -5 | "El stock no puede ser negativo" | ✅ |
| Stock cero | 0 | Aceptar | ✅ |
| Stock no entero | 5.5 | "El stock debe ser numérico" | ✅ |
| Stock no numérico | "abc" | "El stock debe ser numérico" | ✅ |

### 2.5 Excel
| Caso | Situación | Resultado Esperado | Estado |
|------|-----------|-------------------|--------|
| Archivo no existe | Eliminar inventario.xlsx | Crear automáticamente | ✅ |
| Archivo vacío | Excel sin datos | Mostrar "No hay productos" | ✅ |
| Excel corrupto | Archivo con formato inválido | Manejo de error apropiado | ✅ |

---

## 3. Pruebas de Validación de Datos

### 3.1 Tipos de Dato
- [x] Validar que precio_compra es float
- [x] Validar que precio_venta es float
- [x] Validar que stock es int

### 3.2 Rangos Válidos
- [x] Precios >= 0
- [x] Stock >= 0
- [x] precio_compra <= precio_venta

### 3.3 Campos Obligatorios
- [x] codigo no puede estar vacío
- [x] producto no puede estar vacío

---

## 4. Pruebas de Integración

### 4.1 Flujo Completo
- [x] Agregar 3 productos
- [x] Ver productos (deben aparecer 3)
- [x] Buscar uno de ellos
- [x] Actualizar precio de uno
- [x] Actualizar stock de otro
- [x] Eliminar el tercero
- [x] Ver productos (deben quedar 2)

### 4.2 Errores Consecutivos
- [x] Intentar agregar con código duplicado
- [x] Intentar eliminar producto inexistente
- [x] Intentar actualizar precio de producto inexistente
- [x] Validar mensajes de error correctos

---

## 5. Casos de Seguridad

- [x] Inyección de código malicioso en campos
- [x] Caracteres especiales en nombres de producto
- [x] Rutas de archivo manipuladas

---

## 6. Notas de Ejecución

Para ejecutar pruebas manualmente:
```bash
python main.py
```

Para ejecutar pruebas automatizadas:
```bash
python -c "
import inventory_manager
# ejecutar funciones de prueba
"
```

---

## 8. Pruebas - Aumentar Precios por Porcentaje (Nueva Funcionalidad)

### 8.1 Casos Normales
- [x] Aumentar precios con porcentaje válido (ej: 10%)
- [x] Verificar que los precios aumentan correctamente
- [x] Aumentar con 0% (no debe cambiar)
- [x] Aumentar con porcentaje decimal (ej: 5.5%)

### 8.2 Validaciones
- [x] Porcentaje negativo debe ser rechazado
- [x] Porcentaje no numérico debe ser rechazado
- [x] Inventario vacío debe mostrar mensaje

### 8.3 Confirmación
- [x] Confirmar con "S" aplica los cambios
- [x] Confirmar con "N" cancela la operación

---

## 7. Checklist de Funcionalidades

| # | Funcionalidad | Estado | Notas |
|---|---------------|--------|-------|
| 1 | Ver productos | ✅ | |
| 2 | Buscar producto | ✅ | |
| 3 | Agregar producto | ✅ | |
| 4 | Eliminar producto | ✅ | Con confirmación S/N |
| 5 | Actualizar precio | ✅ | |
| 6 | Actualizar stock | ✅ | |
| 7 | Aumentar precios por % | ✅ | Nueva funcionalidad |
| 8 | Validar código vacío | ✅ | |
| 9 | Validar precio compra > venta | ✅ | |
| 10 | Manejo de errores Excel | ✅ | |
| 11 | Normalizar inputs (strip) | ✅ | |
