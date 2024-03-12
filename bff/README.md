# Consulta de publicaciones (RF-005)

Este microservicio, identificado con el código RF-003, se ha diseñado para satisfacer la necesidad de los usuarios de consultar una de sus publicaciones, y que está contenga de manera ordenada descendente por utilidad, las ofertas que han realizado otros usuarios.

## Índice

1. [Estructura](#estructura)
2. [Ejecución](#ejecución)
3. [Uso](#uso)
4. [Pruebas](#pruebas)
5. [Autor](#autor)

## Estructura

La aplicación está desarrollada en python usando el framework FastApi y su estructura de carpetas es la siguiente:
```bash
├───src/
│   ├───commands/ #Logica de negocio
│   │   ├───base_command.py
│   │   ├───get_full_post_info.py
│   │   ├───get_offers_score.py
│   │   ├───get_post_offers.py
│   │   ├───get_post_route.py
│   │   ├───get_post.py
│   │   ├───get_user_id_by_token.py
│   │   ├───validate_user.py
│   │   └───__init__.py
│   ├───endpoints/ #Endpoints
│   │   ├───post_endpoints.py
│   │   └───__init__.py
│   ├───schemas/ #Esquemas de peticiones y respuestas
│   │   ├───post_schema.py
│   │   └───__init__.py
│   ├───utils/ #Librerias de utilidades
│   │   ├───config.py
│   │   ├───middleware.py
│   │   ├───validation_exception_handler.py
│   │   └───__init__.py
│   └───app.py #archivo de entrada de la aplicacion
├───test/
│   ├───endpoints_test/ #Test unitarios de los endpoints
│   │   └───test_get_posts_endpoints.py
│   └───__init__.py
├───Dockerfile #Archivo para el despliegue en docker
├───requirements.txt #Dependencias del proyecto
└───README.md #Usted está aquí
```
## Ejecución
Antes de ejecutar el proyecto es impórtate que cree un archivo ``.env`` en la raíz del proyecto, el cual deberá tener la siguiente estructura
```bash
TEST_MODE=True #True para correr las pruebas
POSTS_PATH=... #Url HTTP del servicio de autenticación de posts
OFFERS_PATH=... #Url HTTP del servicio de autenticación de offers
ROUTES_PATH=... #Url HTTP del servicio de autenticación de routes
SCORE_PATH=... #Url HTTP del servicio de autenticación de score
```


Para poder correr la aplicación de manera local siga los siguientes pasos, estando sobre la raíz de la carpeta ``posts/``.

```bash
# 1. Instale las dependencias del proyecto
pip install -r requirements.txt

# 2. Entre a la carpeta src
cd ./src

# 3. Dentro de la carpeta src, ejecute el comando para correr la aplicación
uvicorn app:app --reload

# 4. (Opcional), Si necesita correr la aplicación en un puerto en específico agregue el flag --port
uvicorn app:app --port 3001 --reload
```

## Uso

Una vez este ejecutado el proyecto puede ver su documentación navegando a la url http://localhost:8000/docs/ o ingresando al contrato que se encuentra en el siguiente [enlace](https://github.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-202411/wiki/Gestión-de-Publicaciones) 

## Pruebas

Para poder correr las pruebas siga los siguientes pasos, estando sobre la raíz de la carpeta ``posts/`` _**(Recuerde antes de correr las pruebas que la variable 'TEST_MODE' debe estar seteada en True)**_ .

```bash
# 1. Ejecute el comando (Nota, en mi ambiente py hace referencia al interprete, en su caso debe colocar el nombre de su interprete Ej. 'phyton, phyton3')
py -m unittest discover

# 2. (Opcional) Para revisar el porcentaje de coverage del proyecto, ejecute el siguiente comando
coverage run -m unittest discover

# 2.1 Seguido del comando para mostrar el reporte
coverage report
```

## Autor
Andres Felipe Martinez Castiblanco 

