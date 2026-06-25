

# SmartGastro 2.0

Sistema web inteligente para la gestión de Food Trucks desarrollado como Trabajo Práctico Integrador II de la carrera de Analista de Sistemas.

SmartGastro 2.0 permite administrar productos, controlar inventario, registrar ventas, consultar el clima en tiempo real y generar reportes PDF para asistir en la toma de decisiones comerciales y reducir pérdidas ocasionadas por condiciones climáticas.

---

# Descripción

El objetivo del proyecto es brindar una solución para pequeños emprendimientos gastronómicos móviles, permitiendo gestionar el inventario y las ventas desde una única aplicación web.

El sistema incorpora información climática en tiempo real para asistir al administrador en la planificación de la producción diaria, ayudando a minimizar pérdidas por sobreproducción durante jornadas de lluvia o condiciones meteorológicas adversas.

---

# Tecnologías utilizadas

* Python
* Flask
* SQLAlchemy
* SQLite
* Jinja2
* HTML5
* CSS3
* JavaScript
* Fetch API
* ReportLab
* Open-Meteo API
* Nominatim / OpenStreetMap
* Werkzeug Security
* Python Dotenv

---

# Funcionalidades

* Autenticación mediante login con sesiones.
* Contraseñas almacenadas utilizando hash seguro.
* Protección de rutas para usuarios autenticados.
* CRUD completo de productos.
* Baja lógica (Soft Delete).
* Registro de ventas.
* Actualización automática del stock.
* Historial persistente de ventas.
* Dashboard con estadísticas generales.
* Consulta climática en tiempo real.
* Geolocalización automática del usuario.
* Conversión de coordenadas GPS a ubicación legible.
* Exportación de reportes PDF.
* Operaciones asíncronas mediante Fetch API.
* Interfaz moderna con CSS personalizado y animaciones.

---

# Requisitos

* Python 3.10 o superior.
* pip.
* Navegador moderno.
* Conexión a Internet para consultar APIs externas.

---

# Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd SmartGastroMVP
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python app.py
```

---

# Usuario de prueba

Email

```
admin@smartgastro.com
```

Contraseña

```
admin123
```

---

# Modelo de datos

El sistema trabaja con tres entidades principales:

* Usuario
* Producto
* Venta

Relaciones:

* Un usuario puede registrar múltiples ventas.
* Un producto puede estar asociado a múltiples ventas.
* Cada venta pertenece a un usuario y a un producto.

Para preservar la integridad del historial comercial, los productos no se eliminan físicamente de la base de datos. En su lugar se implementa una baja lógica mediante el campo `activo`.

---

# Seguridad

El sistema implementa:

* Hash de contraseñas mediante Werkzeug Security.
* Login con sesiones de Flask.
* Protección de rutas mediante el decorador `login_requerido`.
* Variables de entorno utilizando `.env`.
* Exclusión del archivo `.env` mediante `.gitignore`.
* Persistencia utilizando SQLAlchemy ORM.

---

# APIs externas

## Open-Meteo

Se utiliza para obtener información meteorológica en tiempo real.

Datos consultados:

* Temperatura.
* Lluvia.
* Velocidad del viento.
* Código meteorológico.
* Riesgo climático para la producción.

## Nominatim (OpenStreetMap)

Se utiliza para convertir las coordenadas geográficas del usuario en una ubicación legible.

Información obtenida:

* Ciudad.
* Barrio.
* Provincia.

---

# Reportes PDF

El sistema permite exportar reportes de:

* Ventas del día.
* Ventas del mes.
* Ventas del año.
* Historial completo.

Cada reporte incluye:

* Resumen ejecutivo.
* Total facturado.
* Cantidad de ventas.
* Producto más vendido.
* Promedio por venta.
* Tabla detallada de operaciones.

---

# Operaciones asíncronas

Se utiliza Fetch API para evitar recargar la página en operaciones como:

* Alta de productos.
* Registro de ventas.
* Actualización del historial.
* Envío de la ubicación del usuario.

---

# Diagramas incluidos

La documentación técnica incorpora diagramas realizados con Mermaid:

* Diagrama de Clases.
* Diagrama Entidad-Relación.
* Casos de Uso.
* Flujo de Ventas.
* Arquitectura del Sistema.
* Diagrama de Secuencia.

---

# Alcance del proyecto

SmartGastro 2.0 se enfoca en:

* Gestión de productos.
* Control de inventario.
* Registro de ventas.
* Dashboard administrativo.
* Recomendaciones de producción según condiciones climáticas.
* Generación de reportes PDF.

El módulo de comandas hacia cocina queda planteado como una mejora para futuras versiones.

---

# Mejoras futuras

* Gestión de comandas.
* Estados de pedidos.
* Roles diferenciados (Administrador, Cajero y Cocina).
* Reportes gráficos.
* Dashboard analítico.
* Notificaciones por bajo stock.
* Modo oscuro.
* Integración con impresoras térmicas.
* Gestión de múltiples sucursales.

---

# Autor

Gabriel Toledo

Trabajo Práctico Integrador II

Carrera: Analista de Sistemas

Año: 2026
