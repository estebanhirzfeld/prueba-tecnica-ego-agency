# EGO Motors - API

![1709857916696](image/readme/1709857916696.png)

## Descripción

Este proyecto es una API simple para la gestión de una agencia de autos, utilizando Django, un framework de desarrollo web en Python. La aplicación cuenta con la capacidad de:

- Creación de vehículos
- Creación de tipos de vehículos
- Creación de marcas de vehículos
- Búsqueda por filtrado de (año, marca, tipo, precio)
- Creación y gestión de features dinámicas para blog
- Documentación de la API con Redoc
- Capacidad de crear Backups remotos y locales
- Traducciones con gettext_lazy para futuras integraciones internacionales

## Requisitos Previos

- Python (3.11.2)   # Versión específica de Python requerida
- Django (django>=4.1.7)   # Versión específica de Django requerida
- Docker (Opcional)

## Instalación

1. Clona este repositorio en tu máquina local.
2. Abre una terminal y navega hasta el directorio raíz del proyecto.
3. Crea un entorno virtual para el proyecto (opcional, pero se recomienda).

   ```bash

   python -m venv venv   # Comando para crear un entorno virtual

   ```
4. Activa el entorno virtual.

   - En Windows:

     ```bash

     venv\Scripts\activate   # Comando para activar el entorno virtual en Windows

     ```
   - En macOS y Linux:

     ```bash

     source venv/bin/activate   # Comando para activar el entorno virtual en macOS y Linux

     ```
5. Instala las dependencias del proyecto.

   ```bash

   pip install -r requirements/local.txt   # Comando para instalar las dependencias del proyecto desde un archivo requirements.txt

   ```

## Configuración

1. En la versión local, las variables de entorno no están ocultas por lo que no es necesario configurar nada.

## Ejecución

1. En la terminal, navega hasta el directorio raíz del proyecto si aún no lo has hecho.
2. Ejecuta el siguiente comando para iniciar el servidor de desarrollo:

   ### Comando para iniciar el servidor de desarrollo de Django


   ```bash

   python manage.py runserver 8080   # Comando para iniciar el servidor de desarrollo de Django en el puerto 8080

   ```
3. Abre un navegador web y navega a `http://127.0.0.1:8080/` para ver la aplicación en funcionamiento.
4. En la seccion `http://127.0.0.1:8080/redoc/` podra ver los endpoints de la API de forma grafica.

## Instalación y Ejecución con Docker

- El proyecto también se puede desplegar localmente usando Docker con el siguiente comando:

  ```bash

  docker compose -f local.yml up --build -d --remove-orphans   # Comando para levantar el proyecto usando Docker

  ```

  Esto es escencialmente util si no se quiere instalar ni configurar muchas dependencias, a su vez mejora la capacidad de adaptacion a futuros miembros para contribuir en el mismo

  **IMPORTANTE modificar a partir de la linea 87 a la 94 modificar de la siguiente manera:**

```
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": ROOT_DIR / "db.sqlite3",
#     }
# }

DATABASES = {"default": env.db("DATABASE_URL")}
```

## Makefile

- En el archivo Makefile encontrará una variedad de comandos útiles para la mejora del código, creación de backups, entre otras tareas.
