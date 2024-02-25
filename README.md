# pda_registry_service
Servicio de PDA que se utiliza para el registro de información.

## debe tener un archivo .env
tomar el archivo .env.example y renombrarlo .env, luego se deben colocar las variables correctas

## levantar la base de datos
el docker ya lee de variables de entorno si y solo si el archivo se llama .env, por lo tanto el paso anterior ya debe estár completado
```python
docker-compose -f "docker-compose.yml" up
```

## ejecutar el servidor
se deben cargar las variables de entorno en el ambiente
```python
export $(cat .env)
```
Luego se procede a levantar el servidor
```python
flask --app src/propiedadesDA/api run -p 3000
```