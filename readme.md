# 🍴 Recetario Django

Aplicación web desarrollada con **Python y Django** como proyecto final de la Diplomatura en Desarrollo Web.

Permite administrar un recetario de cocina mediante un sistema de usuarios con distintos roles.

---

# 📌 Características

- ✅ Registro de usuarios
- ✅ Inicio de sesión personalizado
- ✅ Recuperación de contraseña
- ✅ Dos tipos de usuarios:
  - 📖 Lector
  - ✏️ Editor
- ✅ Crear recetas
- ✅ Editar recetas
- ✅ Eliminar recetas
- ✅ Subir imágenes
- ✅ Subir videos
- ✅ Clasificación por categorías
  - 🍰 Dulces
  - 🍕 Saladas
- ✅ Interfaz responsive
- ✅ Barra de navegación
- ✅ Menú desplegable
- ✅ Gestión de usuarios

---

# 🛠 Tecnologías utilizadas

- Python 3
- Django
- PostgreSQL
- Docker
- HTML5
- CSS3
- JavaScript
- Bootstrap (componentes utilizados)
- Git
- GitHub

---

# 📂 Estructura del proyecto

```
recetario/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── recetas/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── media/
│
├── static/
│
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

---

# 👤 Roles del sistema

## 📖 Lector

Puede:

- Ver recetas
- Ver imágenes
- Ver videos

No puede modificar información.

---

## ✏️ Editor

Puede:

- Crear recetas
- Editar recetas
- Eliminar recetas
- Administrar usuarios

---

# 📸 Cada receta contiene

- Título
- Categoría
- Ingredientes
- Preparación
- Imagen
- Video

---

# 🔐 Sistema de autenticación

La aplicación utiliza el sistema de autenticación de Django.

Los usuarios pueden:

- Registrarse
- Iniciar sesión
- Recuperar contraseña
- Cerrar sesión

Cada usuario posee un perfil con un rol (Lector o Editor) que determina los permisos disponibles.

---

# 🗄 Base de datos

La aplicación utiliza PostgreSQL ejecutándose mediante Docker.

---

# ▶ Instalación

Clonar el repositorio

```bash
git clone https://github.com/Gabrielortino22/recetario.git
```

Ingresar al proyecto

```bash
cd recetario
```

Levantar Docker

```bash
docker compose up --build
```

Aplicar migraciones

```bash
docker compose exec web python manage.py migrate
```

Crear un superusuario

```bash
docker compose exec web python manage.py createsuperuser
```

Ejecutar la aplicación

```
http://localhost:8000
```

---

# 📷 Capturas

## Login

- Inicio de sesión
- Registro
- Recuperación de contraseña

## Inicio

- Listado de recetas

## Nueva receta

- Formulario para crear recetas

## Editar receta

- Modificación de datos

## Usuarios

- Administración de usuarios

---

# 🎯 Objetivo del proyecto

Desarrollar una aplicación web completa utilizando Django, aplicando los conceptos aprendidos durante la Diplomatura:

- Arquitectura MVT
- Modelos
- Vistas
- Templates
- Autenticación
- Permisos
- Base de datos PostgreSQL
- Docker
- Archivos estáticos
- Archivos multimedia

---

# 👨‍💻 Autor

**Gabriel Ortino**

Proyecto Final – Diplomatura en Desarrollo Web

Año: **2026**

---

# 📄 Licencia

Proyecto desarrollado con fines educativos.