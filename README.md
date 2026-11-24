# API Gestión de Reuniones

API REST para registrar, consultar, actualizar y eliminar reuniones.

## Despliegue en Render

1. Sube este repositorio a GitHub.
2. En Render, crea un **Blueprint** y selecciona el repositorio. Render leerá `render.yaml`.
3. Revisa y despliega los recursos. El Blueprint crea el servicio web y una base de datos PostgreSQL, y configura `DATABASE_URL` automáticamente.
4. Cuando termine el despliegue, comprueba `/health` y consulta `/docs` para explorar la API.

El servicio inicia con Uvicorn y escucha en el puerto asignado por Render. No subas el archivo `.env`; en despliegues manuales configura `DATABASE_URL` como variable de entorno con la URL de conexión de PostgreSQL.

## Desarrollo local

Instala las dependencias con `pip install -r requirements.txt`, configura `DATABASE_URL` en un archivo `.env` local y ejecuta:

```bash
uvicorn main:app --reload
```
