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


## Endpoints
* POST /api/gastos/: Crear un nuevo gasto.
* GET /api/gastos/: Listar todos los gastos.
* GET /api/gastos/{id}/: Consultar un gasto específico.
* PUT /api/gastos/{id}/: Actualizar un gasto.
* DELETE /api/gastos/{id}/: Eliminar un gasto.
* POST /api/register/: Registrar un nuevo usuario.
* POST /api/token/: Obtener un token JWT.
* POST /api/token/refresh/: Refrescar el token JWT.