# 🍴 Recetario Django

Aplicación web desarrollada con **Python**, **Django**, **PostgreSQL** y **Docker** como proyecto final de la **Diplomatura en Desarrollo Web**.

La aplicación permite gestionar un recetario de cocina mediante un sistema de autenticación con distintos tipos de usuarios, permitiendo administrar recetas con imágenes y videos.

---

# 📋 Características

- Registro de usuarios.
- Inicio de sesión personalizado.
- Recuperación de contraseña.
- Sistema de roles (Lector y Editor).
- Creación de recetas.
- Edición de recetas.
- Eliminación de recetas.
- Carga de imágenes.
- Carga de videos.
- Clasificación por categorías.
- Gestión de usuarios.
- Diseño responsive.
- Barra de navegación.
- Menú desplegable.

---

# 👤 Roles del sistema

La aplicación posee dos tipos de usuarios.

## 📖 Lector

Puede:

- Ver recetas.
- Ver imágenes.
- Ver videos.

No puede modificar información.

---

## ✏️ Editor

Puede:

- Crear recetas.
- Editar recetas.
- Eliminar recetas.
- Administrar usuarios.

Los usuarios con rol **Editor** se generan automáticamente cuando se crea un superusuario utilizando el comando:

```bash
docker compose exec web python manage.py createsuperuser
```

El sistema detecta que es un superusuario y crea automáticamente su perfil con el rol **Editor**.

---

# 🍽 Información de cada receta

Cada receta contiene:

- Título
- Categoría
- Ingredientes
- Preparación
- Imagen
- Video

Las categorías disponibles son:

- 🍰 Dulce
- 🍕 Salada

---

# 🔐 Sistema de autenticación

La aplicación utiliza el sistema de autenticación de Django.

Los usuarios pueden:

- Registrarse.
- Iniciar sesión.
- Recuperar contraseña.
- Cerrar sesión.

Al registrarse desde la aplicación, el sistema crea automáticamente un perfil con el rol **Lector**.

Al crear un superusuario mediante el comando `createsuperuser`, el sistema crea automáticamente un perfil con el rol **Editor**.

---

# 🛠 Tecnologías utilizadas

- Python 3
- Django
- PostgreSQL
- Docker
- HTML5
- CSS3
- JavaScript
- Git
- GitHub

---

# 📁 Estructura del proyecto

```
recetario/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── recetas/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── signals.py
│
├── media/
│
├── static/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

# ⚙ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/Gabrielortino22/recetario.git
```

Ingresar al proyecto.

```bash
cd recetario
```

---

## 2. Levantar Docker

```bash
docker compose up --build
```

---

## 3. Aplicar las migraciones

```bash
docker compose exec web python manage.py migrate
```

---

## 4. Crear un usuario Editor

```bash
docker compose exec web python manage.py createsuperuser
```

El sistema asignará automáticamente el rol **Editor** al usuario creado.

---

## 5. Ejecutar la aplicación

Abrir el navegador y acceder a:

```
http://localhost:8000
```

---

# 🚀 Primer uso

Una vez iniciado el proyecto:

1. Crear un superusuario.
2. Iniciar sesión.
3. El usuario tendrá automáticamente permisos de **Editor**.
4. Crear las primeras recetas.
5. Registrar nuevos usuarios desde la aplicación.

Los usuarios registrados desde la aplicación tendrán el rol **Lector** por defecto.

---

# 🗄 Base de datos

La aplicación utiliza PostgreSQL ejecutándose dentro de Docker.

Las migraciones permiten crear automáticamente todas las tablas necesarias.

---

# 📸 Funcionalidades principales

- Inicio de sesión.
- Registro de usuarios.
- Recuperación de contraseña.
- Listado de recetas.
- Creación de recetas.
- Edición de recetas.
- Eliminación de recetas.
- Visualización de imágenes.
- Reproducción de videos.
- Administración de usuarios.

---

# 🎯 Objetivo del proyecto

Desarrollar una aplicación web completa utilizando Django aplicando los conocimientos adquiridos durante la Diplomatura.

Se implementaron los siguientes conceptos:

- Arquitectura MVT.
- Modelos.
- Vistas.
- Templates.
- Sistema de autenticación.
- Permisos mediante roles.
- PostgreSQL.
- Docker.
- Archivos estáticos.
- Archivos multimedia.
- Signals de Django para crear automáticamente perfiles de usuario.

---

# 👨‍💻 Autor

**Gabriel Ortino**

Proyecto Final – Diplomatura en Desarrollo Web

Año: **2026**

---

# 📄 Licencia

Proyecto desarrollado con fines educativos.