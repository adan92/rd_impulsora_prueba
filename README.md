# API de Gestión de Gastos

Esta es una API REST para registrar, consultar y gestionar los gastos de los usuarios.

## Requisitos

- Python 3.8+
- Django 3.x+
- Django REST Framework
- djangorestframework-simplejwt

## Instrucciones de instalación

1. **Clonar el repositorio:**

   ```bash
   git clone <URL del repositorio>
   cd <directorio del proyecto>
    ```
2. Crear un entorno virtual (si no tienes uno):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
    ```
4. Realizar las migraciones:
   ```bash
    python manage.py migrate
    ```
5. Ejecutar el servidor de desarrollo:
   ```bash
    python manage.py runserver
    ```
## Instrucciones de instalación usando docker

1. <code>git clone https://github.com/adan92/rd_impulsora_prueba.git </code>
2. Ubicarse dentro de la carpeta <code> rd_impulsora_prueba </code>
3. Ejecutar el siguiente comando <code> docker-compose up --build -d </code>

De esta manera, docker se encargará de construir y levantar el servicio de manera local en la liga <code>http://127.0.0.1:8000</code>

## Instrucciones de Uso

### Archivos Adjuntos

He incluido los siguientes archivos para facilitar las pruebas con **Postman**:

- **Colección de Postman**: Esta colección contiene todas las peticiones a los endpoints de la API.
- **Entorno de Postman**: El entorno contiene variables necesarias (como la URL base de la API, tokens de autenticación, etc.) para realizar las peticiones de manera sencilla y rápida.

Estos archivos están contenidos en una carpeta llamada `Postman` dentro del repositorio.

### Instrucciones para usar los archivos de Postman

1. **Descargar los archivos de Postman**:  
   Dentro del repositorio, encontrarás una carpeta llamada `Postman`. Esta carpeta contiene los siguientes archivos:
   - `api-collection.json`: La colección de Postman con las peticiones configuradas para la API.
   - `api-environment.json`: El entorno de Postman con las variables configuradas (como la URL base y los tokens).

2. **Importar los archivos a Postman**:
   - Abre **Postman**.
   - Haz clic en **Importar** en la esquina superior izquierda.
   - Selecciona el archivo `api-collection.json` para importar la colección.
   - Luego, importa el archivo `api-environment.json` para configurar el entorno.

3. **Configurar el entorno**:
   - Una vez importado el entorno, selecciona el entorno adecuado desde el menú desplegable en la parte superior derecha de Postman.
   - Asegúrate de que las variables como `{{base_url}}` y `{{access_token}}` estén correctamente configuradas antes de realizar las peticiones.  
     El `{{access_token}}` será el token obtenido después de realizar el login en el endpoint `/api/token/`.

4. **Realizar peticiones**:
   - Con la colección y el entorno importados y configurados, podrás realizar todas las peticiones necesarias para probar los endpoints de la API, como:
     - Crear un gasto (POST `/api/gastos/`)
     - Listar todos los gastos (GET `/api/gastos/`)
     - Consultar un gasto específico (GET `/api/gastos/{id}/`)
     - Actualizar un gasto (PUT `/api/gastos/{id}/`)
     - Eliminar un gasto (DELETE `/api/gastos/{id}/`)
     - Refrescar el token de autenticación (POST `/api/token/refresh/`)
     - Registrar un nuevo usuario (POST `/api/register/`)
