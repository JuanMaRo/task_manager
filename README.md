# Task Manager API

## Descripción

Este proyecto es una API RESTful para un sistema de gestión de tareas simple. Se construye utilizando Python con **Django** y **Django REST Framework (DRF)**.

La API permite a los usuarios registrarse, iniciar sesión y administrar sus tareas. Los usuarios registrados pueden crear tareas y categorias que pueden ser vistas por otros usarios pero solo pueden editadas o eliminadas por el usuario que las creo.

Para construir esta aplicación utilice la ayuda de Gemini en VSCode. A pesar de usar un asistente de IA para contruir la aplicación, tenía que asegurarme que las sugerencias fueran adecuadas y supervisar la ejecución del proyecto desde su creación hasta su ejecución final con los reqremimientos previamente pactados.

## Caracteristicas

- El proyecto cuenta con una sola aplicación desde la que se manejan todos los modelos. Además se utilizo el modelo de usuario que Django trae integrado.
- En los serializadores se renderizaban los modelos, y se agrego un campo url para que se pudiera acceder al detalle de cada tarea.
- Para las vistas se cambio las funciones originales de Django por los ViewSets de DRF para evitar hacer el código más extenso y generar los endpoints más facil. También se asignaban los permisos de acuerdo al modelo y al usuario.
- Para la tabla de status se hizo una migración vacia desde la cual se agregaron los 3 estados para las tareas.
- Dentro de la aplicación se crearon los endpoints con la estructura que DRF proporciona a través de `DefaultRouter` y se renderizaron al proyecto dentro del arhivo principal de urls, esto dentro de `api/`.
- En este mismo archivo (`tasks\urls.py`) se obtiene el token de autenticación para hacer pruebas en Postman. Esto a través de la aplicación de authtoken de DRF.
- En el archivo principal de proyecto (`task_manager/urls.py`) se agrego el endpoint de `api-auth/` para hacer login y logout desde la API en el navegador.
- Para la documentación se agregaron los endpoints correspondientes al paquete `drf-yasg`. El primero tiene expresiones regulares para procesar la información para la API. Mientras que los otros dos cambian como se representa la información, uno en formato swagger otro en formato redoc.

## Paquetes instalados

Este proyecto utiliza los siguientes paquetes de Python:

- **Django**: El framework principal del proyecto. Es en este donde se crean los modelos, la interfaz de administración y el ciclo de las solicitudes y respuestas.
- **Django REST Framework (`djangorestframework`)**: Un poderoso y flexible toolkit para construir Web APIs sobre Django. Proporciona serializadores, viewsets, autenticación y exploración de la API desde el navegador.
- **Django Filter (`django-filter`)**: Este paquete añade filtros a los ViewSets de DRF. Se utilizó para filtrar las tareas por categoría y estatus.
- **DRF - Yet Another Swagger Generator (`drf-yasg`)**: Esta herramienta automáticamente documenta la API en base a OpenAPI/Swagger 2.0. Permite interactuar con la API desde una interfaz propia.

## Instalación

1. Es necesario crear un entorno virtual para aislar las dependenicias del proyecto y evitar conflictos con las versiones de los paquetes.

    python -m venv .env

2. Luego activa el entorno virtual. Sí es en macOS o Linux se utiliza `source .env/bin/activate`. Sí es Windows se usa `.env\Scripts\activate`.

3. Con el entorno virtual creado y activado (el nombre del entorno sale entre parentesis al principio de la linea de comandos), se instalan los paquetes listados en `requirements.txt`

    pip install -r requirements.txt

4. Para correr el proyecto se ejecuta desde la carpeta principal del proyecto:

    python manage.py runserver

Ahora en el navegador se va a `localhost:8000/api` para interactuar con la API con la interfaz de Django REST Framework o para ver la documentación se va a `localhost:8000/swagger/`
