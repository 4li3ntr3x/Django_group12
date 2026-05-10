# 🎣 Big Fish Blog

> Proyecto Django del **Grupo 12** — Curso Python Full Stack 2024 (Codo a Codo)

Blog de caza y pesca con sistema de etiquetas, comentarios, búsqueda y autenticación. Desarrollado con **Django 4.1** y **Bootstrap 5**.

## 🧑‍🤝‍🧑 Equipo

| Integrante | Rol |
|---|---|
| Marcelo Paganini | Full Stack |
| Horacio Peña | Full Stack |
| Daniel Marocchi | Full Stack |
| Leandro Pastori | Full Stack |
| Alejandro Migliaccio | Full Stack |

## 🛠️ Stack

| Tecnología | Uso |
|---|---|
| ![Django](https://img.shields.io/badge/Django-4.1-092E20?style=flat&logo=django) | Backend y templates |
| ![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python) | Lógica de negocio |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql) | Base de datos |
| ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat&logo=bootstrap) | Frontend responsive |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript) | Interactividad |
| ![jQuery](https://img.shields.io/badge/jQuery-3.7-0769AD?style=flat&logo=jquery) | DOM manipulation |

## ✨ Funcionalidades

### 📝 Gestión de Posts
- Creación de entradas con título, contenido y etiquetas
- Las etiquetas se crean **dinámicamente** desde el frontend (JS)
- Listado completo con truncado a 50 palabras + "Leer más"
- Vista detalle con contenido completo

### 🏷️ Sistema de Etiquetas
- Posts categorizados mediante relación **ManyToMany**
- Filtrado por etiqueta
- Creación de nuevas etiquetas sin recargar la página

### 💬 Comentarios
- Los visitantes pueden comentar sin registro
- Validación del lado del servidor
- Se muestran fecha, autor y contenido

### 🔍 Búsqueda
- Búsqueda por título (case-insensitive) via `ListView`
- Resultados en tiempo real desde el navbar

### 🔐 Autenticación
- **Registro** de usuarios con email
- **Login/Logout** con sesiones Django
- Protección: crear posts requiere estar logueado

### 📄 Páginas estáticas
- **Quiénes Somos** — Conoce al equipo
- **Trabaja con Nosotros** — Landing de recruitment
- **Perfil** — Página de perfil de usuario

## 🗺️ Diagrama de navegación

```
                    ┌─────────────┐
                    │   Home 🏠    │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┬────────────────┐
          ▼                ▼                ▼                ▼
   ┌──────────┐    ┌──────────────┐  ┌──────────┐   ┌────────────┐
   │  Todos   │    │  Quiénes     │  │  Login   │   │  Buscar    │
   │  Posts   │    │  Somos       │  │/Signup   │   │  Resultados│
   └────┬─────┘    └──────────────┘  └────┬─────┘   └────────────┘
        │                                  │
   ┌────┴─────┐                    ┌───────┴────────┐
   │  Detalle  │                    │  Crear Post ✏️  │
   │  +Coments │                    │  (auth only)   │
   └──────────┘                    └────────────────┘
```

## 📂 Estructura del proyecto

```
📦 Django_group12
├── 📄 manage.py
├── 📄 requirements.txt
├── 📁 group12/                 # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── 📁 blog/                    # App principal
│   ├── models.py               # Post, Comentario, Etiqueta
│   ├── views.py                # 11 views (FBV + 1 CBV)
│   ├── forms.py                # PostForm, CommentForm, SignupForm
│   ├── admin.py                # Admin personalizado
│   ├── urls.py                 # 13 rutas
│   └── templates/
│       ├── base.html
│       ├── homepage.html
│       ├── index.html
│       ├── post_detail.html
│       ├── crear_post.html
│       ├── login.html / signup.html
│       ├── buscar.html / etiquetas.html
│       ├── quienesSomos.html
│       ├── trabajaConNosotros.html
│       └── perfil.html
└── 📁 static/
    ├── style.css
    ├── blog/style.css
    ├── css/ (Bootstrap 5)
    ├── js/ (Bootstrap + jQuery + crearPost.js)
    └── images/
        ├── logo.png
        ├── 1.jpg / 2.jpg / 3.jpg
```

## 🧠 Modelos

```python
Etiqueta    → id, desc                # Tags categorización
Post        → titulo, autor, contenido, fecha, etiquetas (M2M)
Comentario  → autor, email, contenido, fecha, post (FK)
```

## 🚀 Cómo levantar el proyecto

```bash
# Clonar
git clone https://github.com/4li3ntr3x/Django_group12.git
cd Django_group12

# Entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Dependencias
pip install -r requirements.txt

# Configurar variables de entorno (.env)
SECRET_KEY=tu_secret_key
DATABASE_NAME=bigfish
DATABASE_USER=postgres
DATABASE_PASSWORD=tu_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Migrar y correr
python manage.py migrate
python manage.py runserver
```

## 📸 Capturas (concepto)

| Home | Post Detail | Crear Post |
|------|-------------|------------|
| Bienvenida + últimos 3 posts | Post completo + comentarios | Formulario con tags dinámicos |

## 📌 Mejoras pendientes

- [ ] Migrar a `ALLOWED_HOSTS` seguro y `DEBUG=False`
- [ ] Implementar reset de contraseña
- [ ] Subir imágenes a los posts
- [ ] Paginación en el listado
- [ ] Tests automatizados

---

<p align="center">
  <sub>Proyecto Grupo 12 · Codo a Codo Python Full Stack 2024</sub>
</p>
