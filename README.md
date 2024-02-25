# pda_registry_service
Servicio de PDA que se utiliza para el registro de información.

## consideraciones previas
Este repositorio fue escrito en python v3.10.12, para instalar las librerias se debe lanzar
```python
pip install -r requirements.txt
```
## debe tener un archivo .env
tomar el archivo .env.example y renombrarlo .env, luego se deben colocar las variables necesarias y
cargar las variables de entorno en el ambiente
```python
export $(cat .env)
```

## levantar la base de datos
el docker ya lee de variables de entorno si y solo si el archivo se llama .env, por lo tanto el paso anterior ya debe estár completado
```python
docker-compose -f "docker-compose.yml" up
```

## ejecutar el servidor

Luego se procede a levantar el servidor
```python
flask --app src/propiedadesDA/api run -p 3000
```

## endpoint para crear una propiedad

endpoint: http://localhost:3000/propiedad

tipo: POST
body
```json
{
    "coordenadas": "{'lat': 32.23, 'lng': 32.34}",
    "direccion": "cra 132 N 122 - 22",
    "fecha_creacion": "2024-02-02 09:02:00",
    "nombre": "villeta"
}
```

## endpoint para consultar una propiedad a analizar

endpoint: http://localhost:3000/analisis/propiedad/<propiedad_id>

tipo: GET
